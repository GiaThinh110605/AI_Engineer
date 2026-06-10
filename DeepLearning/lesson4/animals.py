from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import pickle
import os
import cv2
import numpy as np 
from torchvision.transforms import Resize, ToTensor, Compose
from PIL import Image


class MyAnimals(Dataset):
    def __init__(self, data_path, transform=None):
        self.images = []
        self.labels = []
        for folder_name in os.listdir(data_path):
            for image_name in os.listdir(os.path.join(data_path, folder_name)):
                image_path = os.path.join(data_path, folder_name, image_name)
                self.images.append(image_path)
                self.labels.append(folder_name)
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




if __name__ == "__main__":
    transform = Compose([
        ToTensor(),
        Resize((224, 224))
    ])
    dataset = MyAnimals(data_path="/Users/mac/Downloads/AI_Engineer/Dataset/animals/train", transform=transform)
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True, drop_last=True)
    for images, labels in dataloader:
        print(images.shape)
        print(labels)
