https://www.youtube.com/watch?v=Dbvd-zaqJnQ&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=8
# Machine learning Algorithms
## 1. Supervised learning
- Huấn luyện với dữ liệu đánh nhãn
- Có 2 hướng: Regression (hồi quy) và Classification (phân loại)
- Regression: Dự đoán giá trị liên tục (ví dụ: dự đoán giá nhà, nhiệt độ ngoài trời,...)
- Classification: Dự đoán giá trị rời rạc

## 2. Unsupervised learning
- Huấn luyện với dữ liệu không đánh nhãn
- Có 2 hướng: Clustering và Association
- Clustering: Phân nhóm dữ liệu (mỗi cụm trong giống nhau trong cùng 1 nhóm, khác nhóm thì khác nhau)
- Association: Tìm mối quan hệ giữa các thuộc tính (ví dụ: khách hàng mua sản phẩm A thì cũng mua sản phẩm B)

## 3. Reinforcement learning
- Agent: sẽ tương tác với môi trường (nếu hành động tốt thì nhận thưởng, nếu hành động xấu thì bị phạt)

## Khi chỉ có dữ liệu:
- phải cần biết nó áp dụng trong bài toán gì mới biết dữ liệu đó là label hoặc unlabel

## Các loại đặc trưng phổ biến: 
- đặc trưng số: số rời rạc(-2, -1, 0, 1, 2...), số liên tục(1.2, 1.3...)
- đặc trưng phân loại:
    - nominal: định danh (ví dụ: quốc tịch, màu sắc)
    - ordinal: thứ tự (ví dụ: size s, size m, size l)
    - boolean: đúng sai 

## Phân chia dữ liệu:
- Training set: dùng để huấn luyện mô hình
- Validation set: dùng để điều chỉnh tham số của mô hình (trong quá trình huấn luyện)
- Test set: dùng để đánh giá mô hình sau khi đã điều chỉnh tham số (sau khi huấn luyện)

## Đánh giá mô hình:
- Loss: đo lường hiệu suất của mô hình (trong quá trình huấn luyện)
- Metric: đo lường hiệu suất của mô hình(sau khi huấn luyện)