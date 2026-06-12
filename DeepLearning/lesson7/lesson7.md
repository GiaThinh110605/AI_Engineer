https://www.youtube.com/watch?v=PCxrXeWE3kU&list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&index=9

# Receptive Field (vùng nhận thức)
- nếu có receptive field lớn thì có thể dự đoán đúng hơn

- muốn tăng receptive field: tăng kích thước của kernel, tăng số lượng convolution ở cuối, tăng pooling, sử dụng dilated Conv, dep-wise Conv

- Tăng convolution thì nó ít tham số hơn chỉ tốn thêm ít bộ nhớ đệm
- Tăng kích thước kernel sẽ tăng nhiều tham số hơn so với convolution

# Effective Receptive Field
- Pixel càng ít tham gia vào thì càng ít quan trọng -> những pixel ở biên (vì chỉ quét qua 1 lần)
- Muốn tăng tầm quan trọng pixel biên -> thêm padding 

# Dialted Convolutions
- tốn ít tham số hơn nhưng vẫn tăng được receptive field
- ví dụ: 3x3 nhưng áp vào input 5x5 thì những điểm không được áp thì = 0

