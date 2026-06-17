# Time Series Forecasting (Dự báo chuỗi thời gian)
- Dự đoán những thứ trong tương lai dựa trên những thứ xảy ra liên tiếp nhau trong quá khứ
- Ví dụ có 10 ngày: nhưng muốn sử dụng 5 ngày để dự đoán cho ngày thứ 6 -> sử dụng sliding window.

# Lỗi trong máy học
- Lỗi 1: Reducible Error (có thể giảm được)
    - Bias: sai lệch giữa prediction và actual label (càng bé càng tốt)
    - Variance: độ chính xác của dự đoán khi input thay đổi (càng bé càng tốt)
    -> muốn giảm bias thì tăng độ phức tạp của mô hình, thì variance tăng vì overfitting

    + Trường hợp chọn model machine learning dựa trên dữ liệu:
        + TH1: Low bias + high variance: Decision tree, Random Forest, K-nearest neighbours,
                Kernel SVM -> phù hợp khi có nhiều data, ít features
        + TH2: High bias + low variance: Linear regression, Logistic regression, Linear SVM
                -> phù hợp khi có ít data và nhiều features
        + TH3: Giảm chiều dữ liệu, sử dụng neural network -> nêu có nhiều data và nhiều features
- Lỗi 2: Inrreducible Error (không thể giảm được)
