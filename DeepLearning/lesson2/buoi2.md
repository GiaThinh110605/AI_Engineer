https://youtu.be/bbgRdaQocoE?si=qiM7FNE8qwoZATki
# Neuron = Linear Classifier + Activation function
- Linear Classifier: output = input * weight + bias
- Activation function: giúp mô hình học được các mối quan hệ phi tuyến tính giữa input và output.
- Nếu không có activation, thì hàm số sẽ suy biến Ax + b dù có nhiều layers thì vẫn chỉ là một hàm số tuyến tính.
-> để trích xuất những đặc trưng phức tạp

- input layer, hidden layer, output layer
- Các neuron của lớp trước được kết nối đến tất cả các neuron của lớp sau

- Lan truyền xuôi (forward propagation): quá trình tính toán output của mô hình dựa trên input và trọng số hiện tại.

- Loss function: đo lường sự khác biệt giữa output dự đoán và output thực tế để cập nhật trọng số mô hình. (tính toán dựa trên số lượng tham số của mô hình)

-> Người ta muốn tối ưu mô hình -> tối thiểu hóa hàm loss

- Gradient descent: để tính toán max độ dốc của hàm loss theo trọng số, sau đó cập nhật trọng số theo hướng giảm hàm loss.

- Dễ rơi vào local min

- Momentum: giúp mô hình có cơ hội thoát khỏi local min bằng cách thêm vận tốc vào trong quá trình học

- dataset để làm btvn, tải 10 classes bất kỳ để thử: https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap;tab=objects?pageSplit=&prefix=&forceOnObjectsSortingFiltering=false