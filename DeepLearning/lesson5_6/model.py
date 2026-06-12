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


    def forward(self, x):
        x = self.layers(x)
        print(x)
        return x
    
if __name__ == "__main__":
    fake_data = torch.randn((8, 3, 32, 32))
    model = SimpleNeuralNetwork()
    output = model(fake_data)
    print(output.shape)

