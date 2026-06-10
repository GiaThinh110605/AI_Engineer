# from torchvision.datasets import CIFAR10

# dataset = CIFAR10("../../Dataset/", train=True, download=True)
import os
from torch.utils.data import Dataset
import pickle
import cv2
import numpy as np
from torch.utils.data import DataLoader
from torchvision.transforms import Resize
from PIL import Image


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
        # Reshape CIFAR-10 data from (3072,) to (3, 32, 32) then to (32, 32, 3)
        image_array = np.reshape(image_array, (3, 32, 32))
        image_array = np.transpose(image_array, (1, 2, 0))
        # Convert to PIL Image for transforms
        image = Image.fromarray(image_array)
        if self.transform:
            image = self.transform(image)

        label = self.labels[index]
        return image, label

if __name__ == "__main__":
    transform = Resize((24, 24))
    data_path = "/Users/mac/Downloads/AI_Engineer/Dataset/cifar-10-batches-py"
    dataset = Cifar10(data_path, is_train=True, transform=transform)
    # # test_dataset = Cifar10(data_path, is_train=False)
    # print(dataset.__len__())
    # image, label = dataset[12456]
    # print(image)
    # print(label)
    # print(image.shape)
    # image = np.reshape(image, [3, 32, 32])
    # image = np.transpose(image, [1, 2, 0])
    # image = image[:, :, ::-1]
    # image = cv2.resize(image, (320, 320))
    # cv2.imshow("image", image)
    # cv2.waitKey()
    dataloader = DataLoader(dataset, batch_size=11, shuffle=True, drop_last=True)
    for images, labels in dataloader:
        print(images.shape)
        print(labels)


