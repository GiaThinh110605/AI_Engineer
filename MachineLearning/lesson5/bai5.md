https://www.youtube.com/watch?v=xSM0L4Hxsw0&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=5

# Balance data: Undersampling và Oversampling
- Undersampling: giảm số lượng mẫu của lớp nhiều hơn để cân bằng với lớp ít hơn
- Oversampling: tăng số lượng mẫu của lớp ít hơn để cân bằng với lớp nhiều hơn (tạo ra các mẫu tổng hợp từ các mẫu hiện có)
-> tiếp xúc với dữ liệu từng class nhiều hơn, giúp mô hình học tốt hơn

-> Phân chia dữ liệu rồi mới áp dụng cân bằng dữ liệu chỉ cho bộ train.

# Visualize data
- Matplotlib, Seaborn: thư viện trực quan hóa dữ liệu phổ biến trong Python
- Biểu đồ trực quan: histogram, boxplot, density plot, scatter plot, heatmap, correlation matrix

# Thuật toán và Mô hình
- Thuật toán: Linear Regression, Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Naive Bayes
- Mô hình: mô hình học máy được xây dựng dựa trên thuật toán, có thể được huấn luyện và đánh giá trên dữ liệu

- Linear Regression: tìm đường thẳng gần những điểm dữ liệu nhất
y = w1*x1 + w2*x2 + ... + wn*xn + b
- dễ bị ảnh hưởng bởi outliers, dễ bị ảnh hưởng bởi đa cộng tuyến, hoạt động kém với dữ liệu phi tuyến tính
- muốn biết đặc trưng nào ảnh hưởng lớn thì nhìn vào weight(w) 

- Polynomial Regression: hàm số bậc > 1
y = w1*x1 + w2*x2^2 + ... + wn*xn^n + b

Thuật toán quá phức tạp nhưng dữ liệu quá đơn giản -> overfitting

- Logistic Regression: dự đoán xác suất của một mẫu thuộc về một lớp cụ thể
y = 1 / (1 + exp(-(w1*x1 + w2*x2 + ... + wn*xn + b)))

là output của linear regression, sau đó đưa qua hàm sigmoid để chuyển đổi thành xác xuất [0, 1]