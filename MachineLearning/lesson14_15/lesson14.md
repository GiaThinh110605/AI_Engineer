https://www.youtube.com/watch?v=Go_zzpcxWMw&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=1
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

    - feature selection: chỉ giữ lại những feature quan trọng (feature gốc ban đầu) 
    (sử dụng correlation cofficient: ma trận hệ số tương quan để chọn -> mô hình tuyến tính -> > 0.7 < > -0.7 thì quan trọng) (sử dụng ngưỡng phương sai -> giữ lại phương sai lớn) ()

    - feature extraction: chuyển đổi dữ liệu -> chiều không gian mới -> giảm chiều dữ liệu, chỉ giữ lại những feature quan trọng ở chiều không gian mới.
    (
        + Priciple component analyst(PCA: giảm chiều dữ liệu):  chọn những chiều càng phân tán thì phân biệt dữ liệu càng dễ
            + Bước 1: sử dụng standardize data để đưa về phân phối chuẩn
            + Bước 2: tính mức độ phân tán dữ liệu sử dụng convariance
            + Bước 3: tính mức độ phân tán bằng vector riêng, trị riêng độ lớn landa càng lớn thì độ phân tán càng cao 
            + Bước 4: sắp xếp giảm dần theo landa 
            + Bước 5: loại bỏ số chiều mình muốn
            + Bước 6: đưa về ma trận kích thước nxn
    
    )

# Lời nguyền về chiều dữ liệu
- Nếu có thêm 1 cột -> có gấp 10 lần số hàng nó mới hiệu quả
- Nếu số cột tăng thêm cấp số -> số hàng tăng theo cấp số nhân

# Variance(phương sai) trong dữ liệu (độ phân tán của 1 biến)
- mô hình và con người đều thích phân tán lớn 
- nếu variance bé, thì nó gần các giá trị trung bình(kỳ vọng) -> ít phân tán
- nếu variance lớn, thì xa giá trị trung bình(kỳ vọng) -> phân tán nhiều

# Covariance(hiệp phương sai) trong dữ liệu (độ phân tán của 2 biến)
- nằm trong khoảng [- vô cùng, + vô cùng]

# Vector
- được đặc trưng bởi hướng và độ lớn

# Giãn dữ liệu
- dùng để giãn ảnh theo chiều ngang và chiều dọc. 

# Lật ảnh
- giúp lật ảnh ngược, thực chất là phép nhân ma trận [(-1, 0), (0, 1)]

# Làm méo dữ liệu

# Trị riêng và vector riêng
- vector riêng là vector khi nhân với ma trận bất kỳ thì sẽ không thay đổi phương


# Recommendation systems
- nhiệm vụ gợi ý các sản phẩm, đưa ra các sản phẩm mà người dùng có thể quan tâm

- Popularity based recommendation systems
    - ưu điểm: là người dùng mới thì hiển thị gợi ý trending
    - nhược điểm: không có tính cá nhân hóa

- Content-based filtering
    - ưu điểm: gợi ý những chủ đề tương đồng với chủ đề người dùng xem 
    - nhược điểm: không có gì mới mẻ 

- Collaborative filtering
    - ưu điểm: dựa trên những người dùng khác, có những sở thích chung để gợi ý nội dung
    - nhược điểm: phức tạp

- Utility matrix
    - xây dựng dựa trên những click vào sản phẩm, xem rồi đi, khảo sát vài câu hỏi ... để điền vào cho đầy đủ ma trận này
    