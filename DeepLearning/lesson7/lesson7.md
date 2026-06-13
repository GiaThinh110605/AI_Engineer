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

# Bình thường thì nên tận dụng tất cả mô hình có sẵn để huấn luyện
- sử dụng transfer learning hoặc fine tuning để làm model học nhanh hơn

# Những trường hợp không sử dụng được cả kiến trúc và weight có sẵn
- kích thước rất là bé so với kích thước có sẵn của mô hình -> mô hình có sẵn tốn nhiều tài nguyên -> do đó mình tự code model kiến trúc mới

# Làm thế nào để thiết kế kiến trúc CNN:
- Rule 1: Sử dụng những cái có sẵn trước.
- Rule 2: Nếu rule 1 không làm được, cân nhắc câu hỏi:
        - Mô hình nên có bao nhiêu layer?
        - Mỗi layer nên có parameter như thế nào?
            - Convolutional có bao nhiêu channel? Kernel size là bao nhiêu?
            - Nên dùng activation function gì?
            - Pooling nên có kernel size là bao nhiêu?
            - Nên flatten feature map ở đâu?
            - Nên có bao nhiêu fully connected layer?
            - Có nên dùng Batchnorm, Dropout,...?