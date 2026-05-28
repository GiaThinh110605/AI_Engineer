https://www.youtube.com/watch?v=5Ii12ZuW7Pw&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=6
Quy trình xây dựng mô hình machine learning:
- 1. Thu thập dữ liệu
- 2. Thống kê
    + dữ liệu dạng bảng
        + số hàng, số cột
        + kiểu dữ liệu từng cột
        + số hàng/số ô bị khuyết dữ liệu
        + số hàng bị trùng lặp 
        + tỷ lệ mẫu giữa các class (nếu là bài toán classification)
        + min, max, mean, std/variance, median, quantiles(Q1, Q3, IQR)
        + Outliers
- 3. Tiền xử lý
    + xử lý missing values (features có thể điền trung bình, trung vị, mode, những target thì không được điền)
    + đồng nhất format (ví dụ: Việt Nam, Vietnam -> Việt Nam)
    + xóa trùng lặp
    + đưa dải giá trị khác nhau về cùng dải giá trị giống nhau(ví dụ: mét đổi sang km...)
    + xử lý numerical features: 
        + x_new = (x - min) / (max - min) -> đưa về dải [0,1] (bị ảnh hưởng bởi outliters)
        + x_new = (x - mean) / std -> đưa về dải có mean = 0, std = 1 (rất ít bị ảnh hưởng bởi outliers)
    + xử lý categorical features: 
        + ordinal features: (ví dụ: s, m, l -> 1, 2, 3)
        + nominal features: one-hot encoding (ví dụ: màu sắc -> đỏ, xanh, vàng -> 100, 010, 001)
        + word embedding: là vector biểu diễn từ ngữ trong không gian nhiều chiều, giúp máy tính hiểu được ngữ nghĩa của từ ngữ đó (ví dụ: word2vec, GloVe, FastText)
    + correlation: rxy = cov(x,y) / (std(x) * std(y)) [-1, 1]
        - rxy > 0: x và y có mối quan hệ thuận
        - rxy < 0: x và y có mối quan hệ nghịch
        - rxy = 0: x và y không có mối quan hệ tuyến tính
    => vì correlation cao(> 0.7, < -0.7) là bậc 1 -> sử dụng các thuật toán đơn giản, để chạy nhanh
    + collinearity: 