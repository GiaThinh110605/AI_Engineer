# Model quantitation
- giúp giảm kích thước của model

# Sự đánh đổi trong machine learning
- Nếu model độ chính xác càng cao thì càng khó giải thích

# Tips cho chọn machine learning model
- Chọn những model baseline để chạy trước
- Tiền xử lý, với model khác làm những kỹ thuật khác để so sánh model baseline

# Underfitting và Overfitting
- Underfitting: chạy tốt trên tập train, nhưng chạy không tốt trên tập val/test
- Overfitting: chạy tốt trên tập train, và chạy tốt cả trên tập val/test

# Để ngăn chặn việc underfitting và overfitting sử dụng regularization
- Muốn dự đoán tốt -> mô hình phức tạp 
- Dự đoán vừa đủ tốt -> mô hình ít phức tạp hơn 

-> cân nhắc cân bằng cost

- L1: chọn lọc đặc trưng, ép cho trọng số một vài feature về 0 (Lasso)
- L2: ép cho trọng số một vài feature bé đi (Ridge)
- L1 + L2: Elastic net

# Giảm chiều dữ liệu
- Không phải nhiều feature là tốt, chọn những feature có thông tin quan trọng phù hợp với bài toán
- Có 2 nhóm:
    - feature selection: chỉ giữ lại những feature quan trọng (feature gốc ban đầu) (sử dụng correlation cofficient: ma trận hệ số tương quan để chọn -> mô hình tuyến tính -> > 0.7 < > -0.7 thì quan trọng) (sử dụng ngưỡng phương sai -> giữ lại phương sai lớn) ()
    - feature extraction: chuyển đổi dữ liệu -> chiều không gian mới, chỉ giữ lại những feature quan trọng ở chiều không gian mới.

# Lời nguyền về chiều dữ liệu
- Nếu có thêm 1 cột -> có gấp 10 lần số hàng nó mới hiệu quả
- Nếu số cột tăng thêm cấp số -> số hàng tăng theo cấp số nhân


