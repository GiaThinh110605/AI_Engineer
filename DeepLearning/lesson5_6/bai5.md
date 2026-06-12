# Convolutional 
- size: kích thước của kernel
- stride: bước nhảy 
- padding: phần đệm

- nếu tăng kernel size lên -> số lượng tham số tăng lên
-> nó giúp giảm thiểu tham số theo cấp số cộng, trích xuất đặc trưng thông qua từng kernel đi qua. Chỉ cần nhìn vào khu vực con. 

Ưu điểm của convolutional hơn với fully connected truyền thống
- fully connected: train bức ảnh con mèo, trong tập train thì con mèo luôn ở bên trái bức ảnh. Thì nó sẽ học cả vị trí của con mèo đó. Khi triển khai thực tế, con mèo ở vị trí bên phải thì mô hình khó có thể dự đoán được
- conv layer: chỉ xem vật thể đó ở đâu, chứ không quan tâm về vị trí. Con mèo có hay không thôi -> đem triển khai thì hoạt động ổn

Khi nào kích thước feature map đủ nhỏ -> thường > 10x10


-> nó giảm feature map lâu -> cần giảm nhanh hơn


# Pooling layer
- max pooling, average pooling
-> nó giúp giảm thiểu tham số theo cấp số nhân.
- pooling không có tham số
- thường lấy 2x2, chọn feature map có bội số cho 2

- Lý tại sao max pooling lại được ưa chuộng hơn avg pooling: thường như các bài toán trong thực tế đều lấy max, ví dụ: việc lấy max scoring trong bài toán classification...

# Internal Covariate Shift
- phân bố của dữ liệu càng ngày càng khuếch đại lên

# Batch Normalization layer
- các cell cùng channel thì chuẩn hóa cùng bằng cách tính trung bình và độ lệch chuẩn để tính batchnorm

- Quá trình training: thì tính trung bình(kỳ vọng) và độ lệch chuẩn
- Quá trình inference: không cần tính bởi vì việc mỗi lần đưa 1 ảnh vào dự đoán -> không cần trung bình độ lệch chuẩn -> lấy trung bình và độ lệch chuẩn trong quá trình training sử dụng

# Normalization layer
- Batch Norm: thường dùng cho computer vision (dùng hiệu quả khi batch_size lớn)
- Layer Norm: thường dùng cho natural language processing
- Instance Norm: thường dùng cho nlp nhưng với batch_size nhỏ
- Group Norm: hybrid giữa layer norm và instance norm

# Dropout layer
- Vấn đề: nhiều nơ-ron cùng làm chung 1 việc, tốn tài nguyên, over-estimate
- Lúc training: thì có thể bỏ nơ-ron
- Lúc triển khai: lấy tất cả fully-connected 
-> để các nơ-ron có thể đóng góp ít hơn, hoặc nhiều hơn để tránh việc học cùng đặc trưng