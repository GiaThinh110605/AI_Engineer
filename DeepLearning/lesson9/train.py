from torchvision.models import ResNet18_Weights
import argparse
from datasets import MyAnimals
from model_training import AdvancedCNN
from torchvision.transforms import Compose, ToTensor, Resize
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
import torch 
from tqdm.autonotebook import tqdm
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
from torch.utils.tensorboard import SummaryWriter
import matplotlib.pyplot as plt
import argparse
from torchvision.models import resnet18
from ultralytics import YOLO

def plot_confusion_matrix(writer, cm, class_names, epoch):
    """
    Returns a matplotlib figure containing the plotted confusion matrix.
    
    Args:
       cm (array, shape = [n, n]): a confusion matrix of integer classes
       class_names (array, shape = [n]): String names of the integer classes
    """
    
    figure = plt.figure(figsize=(12, 12))
    # color map: https://matplotlib.org/stable/gallery/color/colormap_reference.html
    plt.imshow(cm, interpolation='nearest', cmap="Wistia")
    plt.title("Confusion matrix")
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)

    # Thêm số vào từng ô
    threshold = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, str(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > threshold else "black")
    
    plt.tight_layout()
    writer.add_figure("Confusion matrix", figure, epoch)
    plt.close(figure)

# Thiết lập tham số riêng biệt để sau khi triển khai
# có thể chỉnh dễ dàng hơn, khi để mặc định trong hàm
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", "-e", type=int, default=100)
    parser.add_argument("--lr", "-l", type=float, default=1e-3)
    parser.add_argument("--momentum", "-m", type=float, default=0.9)
    parser.add_argument("--batch-size", "-b", type=int, default=16)
    parser.add_argument("--image-size", "-s", type=int, default=224)
    parser.add_argument("--checkpoint", "-c", type=bool, default=False)
    return parser.parse_args()

def train():
    args = get_args()
    image_size=args.image_size
    lr=args.lr
    batch_size=args.batch_size
    momentum = args.momentum
    num_epochs = args.epochs
    
    transform = Compose([
        ToTensor(),
        Resize((image_size, image_size))
    ])
    train_dataset = MyAnimals(data_path="/Users/mac/Downloads/AI_Engineer/Dataset/animals/train", transform=transform)
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, drop_last=True)
    val_dataset = MyAnimals(data_path="/Users/mac/Downloads/AI_Engineer/Dataset/animals/val", transform=transform)
    val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, drop_last=False)

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")

    # model = AdvancedCNN(num_classes=len(train_dataset.categories)).to(device)
    model = resnet18(weights=ResNet18_Weights.DEFAULT).to(device)
    print(model)
    model.fc = nn.Linear(in_features=512, out_features=len(train_dataset.categories)).to(device)
    print(model)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)
    writer = SummaryWriter()

    # hàm enumerate() nó giúp giữ được index
    start_epoch=0
    if args.checkpoint:
        checkpoint = torch.load("last.pt")
        model.load_state_dict(checkpoint["model"])
        optimizer.load_state_dict(checkpoint["optimizer"])
        best_acc = checkpoint["best_acc"]
        start_epoch = checkpoint["epoch"]+1


    for epoch in range(start_epoch, num_epochs):
        model.train()
        progress_bar = tqdm(train_dataloader, colour="cyan")
        all_losses = []
        for i, (images, labels) in enumerate(progress_bar):
            images = images.to(device)
            labels = labels.to(device)
            # forward pass
            output = model(images)
            loss = criterion(output, labels)
            all_losses.append(loss.item())
            avg_loss = np.mean(all_losses)
            writer.add_scalar("training loss", avg_loss, global_step= i + epoch*len(train_dataloader))

            # backward + optimize
            optimizer.zero_grad() 
            loss.backward()
            optimizer.step()
            progress_bar.set_description("epoch {}/{}. loss: {:.4f}".format(epoch+1, num_epochs, loss.item()))

        # validation mode
        model.eval()
        progress_bar = tqdm(val_dataloader, colour="cyan")
        all_labels = []
        all_predictions = []
        all_losses = []
        best_acc = 0
        for i, (images, labels) in enumerate(progress_bar):
            images = images.to(device)
            labels = labels.to(device)
            # forward pass
            output = model(images)
            loss = criterion(output, labels)
            with torch.no_grad():
                output = model(images) 
            loss = criterion(output, labels)
            prediction = torch.argmax(output, dim=1).tolist()
            all_predictions.extend(prediction)
            all_labels.extend(labels.tolist())
            all_losses.append(loss.item())

        acc = accuracy_score(all_labels, all_predictions)
        avg_loss = np.mean(all_losses)
        print("Validation: Epoch {}/{} accuracy: {:.3f} loss: {:.3f}".format(epoch+1, num_epochs, acc, avg_loss))
        writer.add_scalar("validation loss", avg_loss, global_step=epoch)
        writer.add_scalar("validation accuracy", acc, global_step=epoch)
        plot_confusion_matrix(writer, confusion_matrix(all_labels, all_predictions), train_dataset.categories, epoch)

        checkpoint = {
            "model": model.state_dict(),
            "epoch": epoch,
            "best_acc": best_acc,
            "optimizer": optimizer.state_dict()
        }
        torch.save(model.state_dict(), "last.pt")

        if acc > best_acc:
            torch.save(model.state_dict(), "best.pt")
            best_acc = acc




if __name__ == "__main__":
    train()