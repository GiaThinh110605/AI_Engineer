https://www.youtube.com/watch?v=wRJacx9IfRI&list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&index=8

# Universal Approximation Theorem
- Trong machine learning: thì việc có x -> ta phải đi tìm fx để gần với các điểm dữ liệu
- Trong deep learning: thì việc có x -> có thể tạo mạng nơ-ron có thể sấp xỉ với các fx phức tạp

# Muốn thêm layer vào không tốt hơn được thì không nên làm tồi đi
- x -> weight layer -> relu -> weight layer -> tổng F(x) + x -> relu
     (              F(x)                     )
( Nếu F(x) = 0 -> vẫn là x )

# Vanishing Gradient 
 - đạo hàm ở cuối thông qua backpropagation thì nó lớn
 - đạo hàm ở gần input thông qua backprogation thì nhỏ
 -> bởi vì một vài gradients sấp xỉ 0 -> gây ra hiện tưởng biến mất gradients

 