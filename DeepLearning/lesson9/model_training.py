import torch.nn as nn
import torch

class SimpleNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=3072, out_features=16),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=32),
            nn.ReLU(),
            nn.Linear(in_features=32, out_features=10)
        )
        self.fc1 = nn.Sequential(
                                nn.Drop_out(p=0.5),
                                nn.Linear(in_features=25088, out_features=512)
                                , nn.LeakyReLU()
        )
        self.fc2 = nn.Sequential(
                                nn.Linear(in_features=512, out_features=128)
                                , nn.LeakyReLU()
        )
        self.fc3 = nn.Sequential(
                                nn.Linear(in_features=128, out_features=10)
                                , nn.LeakyReLU()
        )

        


    def forward(self, x):
        x = self.layers(x)
        print(x)
        return x
    
class AdvancedCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = self.create_block(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = self.create_block(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv3 = self.create_block(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.conv4 = self.create_block(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1)
        self.conv5 = self.create_block(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Sequential(
                                nn.Linear(in_features=25088, out_features=512)
                                , nn.LeakyReLU()
        )
        self.fc2 = nn.Sequential(
                                nn.Linear(in_features=512, out_features=128)
                                , nn.LeakyReLU()
        )
        self.fc3 = nn.Sequential(
                                nn.Linear(in_features=128, out_features=num_classes)
                                , nn.LeakyReLU()
        )

    def create_block(self, in_channels, out_channels, kernel_size, stride, padding):
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding ), # output thường là 2^ và tăng dần hoặc giữ nguyên, input thì theo kích thước ảnh
            nn.BatchNorm2d(num_features=out_channels),
            nn.LeakyReLU(),
            nn.Conv2d(in_channels=out_channels, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding ), # output thường là 2^ và tăng dần hoặc giữ nguyên, input thì theo kích thước ảnh
            nn.BatchNorm2d(num_features=out_channels),
            nn.LeakyReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )


    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = x.view(x.shape[0], -1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)

        return x
if __name__ == "__main__":
    fake_data = torch.randn((8,3,224,224))
    model = AdvancedCNN()
    output = model(fake_data)
    print(output.shape)

