from torchvision.datasets import MNIST

dataset = MNIST("Dataset", train=True, download=True)
index = 500

image, label = dataset[index]
print(image)
print(label)