# import cv2 

# img = cv2.imread("/Users/mac/Downloads/AI_Engineer/DeepLearning/lesson3/process.png", 1)
# print(type(img))
# img[:, :, 0] = 255
# img[:, :, 1] = 0
# img[:, :, 2] = 0
# print(img)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

import numpy as np
import torch

data = np.zeros((2, 4, 3))
print(type(data))
data = torch.from_numpy(data)
print(type(data))
