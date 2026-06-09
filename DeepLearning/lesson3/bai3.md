https://www.youtube.com/watch?v=AyUV1CdNCW4&list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&index=11
# Adaptive Gradient Descent
- xu hướng cập nhật learning rate càng ngày càng bé đi

# Backpropagation 
- lan truyền ngược giúp cập nhật trọng số và bias của mạng nơ-ron phía trước nó. 
- ví dụ forward propagation: 
    input: x, y
    output: z
- ví dụ backpropagation:
    input: z
    output: đạo hàm của loss(z), sau đó đạo hàm loss(x), đạo hàm loss(y)

# Parameters và Hyperparameters
- Parameters: là những cái có sẵn trong mô hình weight, bias
- Hyperparameters: là những cái chúng ta có thể tự chọn learning rate, metrics, cv,... 

# Epoch, Batch size, Iterations
- 1 epoch: là một lần đi qua toàn bộ dữ liệu huấn luyện.
- batch size: kích thước của mẫu dữ liệu dùng đưa qua mô hình. 
- batch size * iterations = số lượng mẫu dữ liệu trong tập huấn luyện
- ví dụ: nếu có 1000 mẫu dữ liệu, batch size là 100 thì số lượng iterations sẽ là 10 (1000/100 = 10).

# Cách train neural network trong Pytorch
- Step 1: Xây dựng 1 dataset từ tập ảnh
- Step 2: Định nghĩa mô hình 
- Step 3: Chọn/ tự xayaduwnjg 1 hay nhiều hàm loss
- Step 4: Chọn 1 optimizer để cập nhật trọng số
- Step 5: Huấn luyện mô hình với training data
- Step 6: Đánh gái tỏng quá trình huấn luyện với validation data
- Step 7: Đánh giá mô hình cuối cùng với test data

# Sự khác biệt giữa numpy và tensor
- numpy: chỉ chạy trên CPU, không hỗ trợ tính toán gradient
- tensor: có thể chạy trên CPU hoặc GPU, hỗ trợ tính toán gradient

# Có 2 thư viện làm việc chính với ảnh
- opencv
- PIL