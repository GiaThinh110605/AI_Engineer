import torch

output = torch.rand(4, 6)
prediction = torch.argmax(output, dim=1).tolist()
print(output)
print(prediction)