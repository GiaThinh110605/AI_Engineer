import cv2

img = cv2.imread("/Users/mac/Downloads/AI_Engineer/DeepLearning/lesson1/hocbong.png", 1)
print(type(img))
img[:200, :300, 0] = 135
# img[:, :, 1] = 0
# img[:, :, 2] = 0
cv2.imshow("Image", img)
print(img)
print(img.shape)
cv2.waitKey(0)
