from datasets import MyAnimals
from model_training import AdvancedCNN
from torchvision.transforms import Compose, ToTensor, Resize
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
import torch 
from tqdm.autonotebook import tqdm

def train():
    image_size=224
    lr=1e-3
    batch_size=32
    momentum = 0.9
    num_epochs = 100
    
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

    model = AdvancedCNN(num_classes=len(train_dataset.categories)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)
    print(criterion)
    print(optimizer)

    # hàm enumerate() nó giúp giữ được index

    for epoch in range(num_epochs):
        model.train()
        progress_bar = tqdm(train_dataloader, colour="cyan")
        for i, (images, labels) in enumerate(progress_bar):
            images = images.to(device)
            labels = labels.to(device)
            # forward pass
            output = model(images)
            loss = criterion(output, labels)

            # backward + optimize
            optimizer.zero_grad() 
            loss.backward()
            optimizer.step()
            progress_bar.set_description("epoch {}/{}. loss: {:.4f}".format(epoch+1, num_epochs, loss.item()))

    # validation mode
    model.eval()
    progress_bar = tqdm(train_dataloader, colour="cyan")
    for i, (images, labels) in enumerate(progress_bar):
        images = images.to(device)
        labels = labels.to(device)
        # forward pass
        output = model(images)
        loss = criterion(output, labels)
        with torch.no_grad():
            output = model(images) 
        loss = criterion(output, labels)
        

if __name__ == "__main__":
    train()