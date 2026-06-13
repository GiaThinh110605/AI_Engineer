# from torchvision.datasets import CIFAR10

# dataset = CIFAR10("../../Dataset/", train=True, download=True)
import os
from torch.utils.data import Dataset
import pickle
import cv2
import numpy as np
from torch.utils.data import DataLoader
from torchvision.transforms import Resize, ToTensor, Compose
from PIL import Image


class MyAnimals(Dataset):
    def __init__(self, data_path, transform=None):
        self.images = []
        self.labels = []
        self.categories = []
        for category_id, folder_name in enumerate(os.listdir(data_path)):
            self.categories.append(folder_name)
            for image_name in os.listdir(os.path.join(data_path, folder_name)):
                image_path = os.path.join(data_path, folder_name, image_name)
                self.images.append(image_path)
                self.labels.append(category_id)
        self.transform = transform


    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        image_path = self.images[index]
        image = cv2.imread(image_path)
        # image = Image.open(image_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        label = self.labels[index]
        return image, label




# if __name__ == "__main__":
#     transform = Compose([
#         ToTensor(),
#         Resize((224, 224))
#     ])
#     dataset = MyAnimals(data_path="/Users/mac/Downloads/AI_Engineer/Dataset/animals/train", transform=transform)
#     dataloader = DataLoader(dataset, batch_size=8, shuffle=True, drop_last=True)
#     for images, labels in dataloader:
#         print(images.shape)
#         print(labels)


class Cifar10(Dataset):
    def __init__(self, data_path, is_train=True, transform=None):
        self.images = []
        self.labels = []
        if is_train:
            data_files = [os.path.join(data_path, "data_batch_{}".format(i)) for i in range(1, 6)]
        else:
            data_files = [os.path.join(data_path, "test_batch")]
        for data_file in data_files:
            with open(data_file, "rb") as fo:
                data = pickle.load(fo, encoding="bytes")
                self.images.extend(data[b"data"])
                self.labels.extend(data[b"labels"])
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        image_array = self.images[index]
        image_array = np.reshape(image_array, (3, 32, 32))
        image_array = np.transpose(image_array, (1, 2, 0))
        # Convert to PIL Image for transforms
        image = Image.fromarray(image_array)
        if self.transform:
            image = self.transform(image)

        label = self.labels[index]
        return image, label

if __name__ == "__main__":
    transform = Compose([
        Resize((224, 224)),
        ToTensor()
    ])
    data_path = "/Users/mac/Downloads/AI_Engineer/Dataset/cifar-10-batches-py"
    dataset = Cifar10(data_path, is_train=True, transform=transform)
    dataloader = DataLoader(dataset, batch_size=11, shuffle=True, drop_last=True)
    for images, labels in dataloader:
        print(images.shape)
        print(labels)


