# Tất cả cho công việc sau này: internship, engineer

## Kỹ năng cứng: 
- 1. Thuật toán
https://leetcode.com/problemset/

- 2. Hiểu tất cả các dạng dữ liệu trong mô hình deep learning, machine learning (SFT, DPO, RLHF...)

- 3. Tiền xử lý dữ liệu với pandas, numpy, json, regrex

- 4. Học machine learning
https://youtube.com/playlist?list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&si=HRfbLNkmB-wwJ8Ys

- 5. Học deep learning
https://youtube.com/playlist?list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&si=UAKnww9X4yEw6kIP

- 6. Học docker để đóng gói mô hình, triển khai thực tế
https://youtu.be/Gh1Sgknc6Fg?si=YtpMSvJV2wPSW4yS
https://www.youtube.com/watch?v=o9Si96339Ig

- 7. Học về Hugging face để finetune mô hình (transformers, dataset)
  1: Làm chủ thư viện transformers & datasets
  2: Tinh chỉnh mô hình (Fine-tuning với PEFT, LoRA/QLoRA)
  3: Đóng gói và Triển khai lên hugging face spaces

- 8. Học fastapi để xây dựng backend đơn giản để triển khai, hiểu để vibe code làm frontend tương ứng
https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ

- 9. Học AWS những kiến thức cloud quan trọng cốt lỗi để tận dụng AI (EC2, S3, ECS)

- 10. Ôn tập cơ sở dữ liệu quan hệ(Postgresql)

- 11. Ôn tập cơ sở không quan hệ(MongoDB)

## Kỹ năng mềm: 
- Thái độ
    - Khi đi làm 1-2 tuần đầu tiên nên xem quy trình làm việc của công ty, văn hóa của công ty, các anh chị đồng nghiệp. Để biết làm theo, nên đến sớm hoặc ít nhất đúng giờ.
    - Không được xem máy tính cá nhân của người khác khi chưa được cho phép.
    - Lắng nghe nhiều hơn, trước khi nói 1 điều gì đó. 
    - Đừng kể về gia đình và cuộc sống cá nhân -> Trả lời khéo: "Dạ nhà em cũng bình thường ạ, cuối tuần em hay đá bóng/học code thôi".
    - Không hỏi việc cá nhân của đồng nghiệp.
    - Làm đúng task, estimate cho đúng (nên nhân 1.5 thời gian dự phòng) trước khi bước vào làm việc.
    - Chủ động hỏi: Đừng giấu dốt. Áp dụng quy tắc 15 phút: Tự tìm câu trả lời, tự debug, tự prompt AI trong 15 phút. Nếu vẫn bế tắc, đến hỏi kèm theo cấu trúc: "Em đang làm task X, gặp lỗi Y, em đã thử cách A và B nhưng chưa được, anh/chị xem giúp em đoạn này với".
    - Có thể giao tiếp được tiếng anh trong công việc liên quan.
    - Gợi ý cần tìm hiểu gì để thực hiện task đó...

- Chuẩn bị
    - CV: Làm cv theo https://www.overleaf.com sử dụng chat gpt, grok... để kiểm tra cv ổn chưa.
    https://www.youtube.com/watch?v=2fqXC4RQyOw
    - Hiểu rõ hơn về công ty, khách hàng của họ là ai, nhiệm vụ của mình là gì, văn hóa là gì, tập trung vào cái gì -> chuẩn bị giải pháp đáp ứng yêu cầu doanh nghiệp.
    
- Kỹ năng tìm code, định vị lỗi:
    - Control + P hoặc Cmd + P: Tìm file nhanh.
    - Control + F hoặc Cmd + F: Tìm text trong file.
    - Khi đọc code cần xem class đó gọi class gì, làm những gì, và prompt cho AI cái mình muốn fix, và tối ưu công việc.

- Kỹ năng github:
    - Tạo nhánh mới và chuyển sang luôn: git checkout -b ten_nhanh_moi
    - Lấy code mới nhất từ main về: git checkout main -> git pull origin main
    - Tạo pull request (PR): Đặt tên chuẩn quy định công ty, assign đúng người review hoặc hỏi đồng nghiệp xung quanh.
    - Thêm file làm việc: git add <ten_file>
    - Commit nội dung: git commit -m 'feat: them file A...'
    - Push code: git push origin ten_nhanh_moi (Lần đầu tiên copy lệnh gợi ý upstream của Terminal).
    - Quy trình khi code bị hư:
        + Nếu lỗi ở máy cục bộ (chưa push): Dùng `git reset --hard HEAD` để quay về trạng thái an toàn gần nhất.
        + Nếu đã lỡ push lên nhánh chung: Báo ngay cho Mentor/Senior để được phối hợp hướng dẫn xử lý an toàn, không tự ý merge/revert bừa bãi.

- Kỹ năng đọc Log bằng terminal/ cmd:
    - 1. Đọc Log Trạng Thái Phần Cứng (Hardware Logs)   
        + Lỗi kinh điển RuntimeError: CUDA out of memory (OOM):
            * Dấu hiệu: Log hiện một bảng dài các block bộ nhớ kèm dòng chữ `Tried to allocate X MiB....`
            * Cách xử lý: GPU hết RAM. Cần hạ batch_size, sử dụng kỹ thuật Gradient Accumulation, áp dụng Quantization (8-bit, 4-bit), hoặc dùng LoRA/QLoRA (peft).
        + Theo dõi GPU theo thời gian thực:
            * Câu lệnh: watch -n 1 nvidia-smi
            * GPU-Util < 50%: Nghẽn cổ chai (Bottleneck) ở CPU do tiền xử lý dữ liệu Pandas/Dataloader quá chậm. -> Sửa: Tăng `num_workers` trong DataLoader.
            * Memory-Usage: Giữ mức an toàn khoảng 85-90% dung lượng VRAM để tránh đột tử khi gặp sample dữ liệu dài hơn.

    - 2. Đọc Log Tiến Trình Huấn Luyện (Training/Fine-tuning Logs)
        + Dòng log tiêu chuẩn: Epoch 3/10 | Step 500/1000 | Loss: 0.4213 | Val_Loss: 0.5122 | Learning_Rate: 1e-4 | Accuracy: 85.3%
        + Kỹ năng "bắt bệnh":
            * Overfitting (Quá khớp): Loss tập train liên tục giảm đẹp, nhưng Val_Loss đứng im hoặc tăng ngược trở lên. -> Xử lý: Dùng Early Stopping, Data Augmentation, hoặc thêm Dropout.
            * Underfitting (Chưa đủ tốt): Cả Loss và Val_Loss giảm cực kỳ chậm và neo ở mức rất cao. -> Xử lý: Đổi sang kiến trúc mô hình lớn hơn, tăng learning_rate, hoặc bổ sung dữ liệu.
            * Lỗi Loss: nan hoặc Loss: inf: Chỉ số Loss biến thành nan hoặc inf (Nổ/triệt tiêu gradient). -> Xử lý: Giảm learning_rate (chia 10), áp dụng Gradient Clipping (max_norm=1.0), kiểm tra giá trị rác Null/NaN từ đầu vào.

    - 3. Đọc Log Khi Đưa Mô Hình Lên Production (Inference Logs)
        + Log về Thời gian phản hồi (Latency Log):
            * Ví dụ: POST /v1/predict - Status: 200 - Time: 2450ms (2.4 giây -> Quá chậm).
            * Phân tích: Cần tối ưu hóa bằng cách chuyển mô hình sang định dạng ONNX hoặc TensorRT, sử dụng Async/Await trong FastAPI, hoặc cấu hình chạy Inference trên GPU.
        + Lỗi định dạng dữ liệu đầu vào (Input Shape/Type Error):
            * Ví dụ: ValueError: Expected 4D tensor as input, but got 3D tensor instead.
            * Phân tích: Thiếu chiều dữ liệu Batch (batch_size).
            * Cách sửa: Dùng `numpy.expand_dims(image, axis=0)` hoặc `torch.unsqueeze(tensor, 0)`.