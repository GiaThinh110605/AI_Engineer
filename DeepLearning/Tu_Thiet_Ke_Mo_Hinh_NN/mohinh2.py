import torch.nn as nn
import torch

class Model2(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features=8, out_features=9),
            nn.Tanh(),
            nn.Linear(in_features=9, out_features=9),
            nn.Tanh(),
            nn.Linear(in_features=9, out_features=9),
            nn.Tanh(),
            nn.Linear(in_features=9, out_features=9),
            nn.Tanh(),
            nn.Linear(in_features=9, out_features=4),
        )
    def forward(self, x):
        x = self.layers(x)
        return x

if __name__ == "__main__":
    model = Model2()
    fake_data = torch.tensor([[0.8, -2.0, 1.5, 0.7, 0.6, 1.0, -2.5, 0.3]])
    print("Fake input: ", fake_data)
    print(model(fake_data))