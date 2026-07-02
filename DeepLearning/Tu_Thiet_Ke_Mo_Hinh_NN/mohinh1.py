import torch.nn as nn
import torch

class Model1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features=3, out_features=4),
            nn.Tanh(),
            nn.Linear(in_features=4, out_features=2),
        )
    def forward(self, x):
        x = self.layers(x)
        return x

if __name__ == "__main__":
    model = Model1()
    fake_data = torch.randn((1,3))
    print("Fake input: ", fake_data)
    print(model(fake_data))