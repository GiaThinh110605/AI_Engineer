https://www.youtube.com/watch?v=JGe0YB9Wq74&list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&index=13
# Machine learning phù hợp với dạng bảng
- input
- feature extraction
- classification
- output

# Deep learning phù hợp với dạng phi cấu trúc (hình ảnh, âm thanh, văn bản)
- input
- feature extraction + classification
- output

(phải cần nhiều dữ liệu để sử dụng deep learning)

- cho computer vision: sử dụng webcam/camera để tiếp nhận hình ảnh, chip xử lý thông tin phân tích kết quả

- Classification: phân loại hình ảnh
- Object detection: phân loại hình ảnh + vị trí của đối tượng 
- Segmentation: phân loại hình ảnh + vị trí của đối tượng đúng với từng pixel

- Neural network: người ta thường nói nó là kiến trúc, bao gồm 1 tầng input layer, 1 tầng hidden layer, 1 tần output layer
- Deep learning: có 1 tầng input layer, nhiều tầng hidden layer, 1 tần output layer

- mỗi 1 pixel: biểu diễn [0, 255]
- mỗi 1 pixel màu: vector 3 chiều biểu diễn [R, G, B] --> mỗi giá trị R, G, B có thể là 0-255

### Linear Classifier 
ví dụ tập MNIST: bức ảnh có 28x28 pixel, mỗi pixel có giá trị từ 0-255, có 10 lớp (0-9)
- input: vector 784 chiều (28x28)
- output: vector 10 chiều (tương ứng với 10 lớp)
- weight: ma trận 784x10 
- bias: vector 10 chiều
- output = input * weight + bias
- output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (giá trị càng lớn thì khả năng dự đoán càng cao)

Ví dụ như số 6: thì weight đi qua số 6 thì sẽ lớn, nếu weight đi qua số khác thì sẽ bé hơn khi đi qua số 6, còn các trọng số những vùng khác thì bao nhiêu cũng được ( 0 x weight = 0 )
