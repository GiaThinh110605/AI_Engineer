https://www.youtube.com/watch?v=PTMX--mheCQ&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=5

###  Thuật toán
- Random Forest  sử dụng nhiều cây quyết định (decision trees) để cải thiện hiệu suất dự đoán và giảm thiểu overfitting.

- Vector Machine: 
    - đảm bảo rằng khoảng cách đều giữa 2 điểm dữ liệu gần nhất
    - tìm kiếm đường thẳng có khoảng cách lớn nhất đến 2 điểm đó
    - nếu không vẽ được đường thẳng thì mình tăng thêm chiều để phân tách dữ liệu

- Knearest Neighbor(supervised learning):
    - chọn k lẻ để tránh trường hợp có 2 lớp bằng nhau
    - tính khoảng cách giữa các điểm dữ liệu
    - gán lớp vói khoảng cách nhỏ nhất
    - dự đoán lớp của điểm dữ liệu mới dựa trên lớp của k điểm dữ liệu gần nhất

- Kmean-Clustering(unsupervised learning):
    - chọn k trung tâm ngẫu nhiên
    - gán mỗi điểm dữ liệu vào trung tâm gần nhất
    - cập nhật lại vị trí của các trung tâm bằng cách tính trung bình của các điểm dữ liệu được gán vào mỗi trung tâm
    - lặp lại quá trình gán và cập nhật cho đến khi các trung tâm không thay đổi hoặc đạt được một số lần lặp tối đa

### Các kỹ thuật 
- Bootstrapping (lấy mẫu hoàn lại): mỗi một cây sử dụng bộ dữ liệu con(khoảng 70% tập dữ liệu gốc) khác nhau để huấn luyện

- Ensample learning: dùng nhiều mô hình để cải thiện chất lượng, sau đó lấy 1 mô hình để dự đoán

- Bagging (Bootstrap Aggregating): mỗi cây được huấn luyện trên một bộ dữ liệu con khác nhau, và kết quả dự đoán cuối cùng được lấy trung bình (cho bài toán hồi quy) hoặc đa số phiếu (cho bài toán phân loại).

- Boosting: các cây được huấn luyện tuần tự, mỗi cây mới tập trung vào việc sửa lỗi của cây trước đó. Kết quả dự đoán cuối cùng được tính bằng cách kết hợp các dự đoán của tất cả các cây.

- Stacking: sử dụng một mô hình thứ hai (meta-model) để kết hợp các dự đoán của nhiều mô hình cơ sở (base models) khác nhau.

