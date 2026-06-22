# Tất cả cho công việc sau này: internship, engineer

# Cheatseat cho toàn bộ học có thể tham khảo:
- https://stanford.edu/~shervine/teaching/ -> chọn tiếng việt

### Tiếng anh luyện tập:
- luyện nói miễn phí: https://parroto.app/vi/practice-english-speaking
- Luyện đề toeic ets miễn phí: https://chamtoeic.edu.vn/tests?collection=890eb9a5-ebf1-43c3-9c4d-492ace3c5097
- Sử dụng Geimini hoặc AI khác, khi học không hiểu câu đó.

## Kỹ năng cứng

1. Thuật toán
   - [LeetCode problemset](https://leetcode.com/problemset/)

2. Kỹ năng Clean Code & Design Patterns
   - Tổ chức code dễ đọc, dễ bảo trì
   - Sử dụng SOLID, DRY, KISS

3. Ôn tập OOP
   - Lớp, đối tượng, kế thừa, đa hình, đóng gói

4. Hiểu các dạng dữ liệu trong mô hình deep learning và machine learning
   - SFT, DPO, RLHF

5. Tiền xử lý dữ liệu với:
   - `pandas`
   - `numpy`
   - `json`
   - regex

6. CI/CD cho ML (cơ bản)
   - Dùng GitHub Actions để tự động chạy test code
   - Tự động build Docker image khi push/merge PR vào nhánh `main`

7. Học machine learning
   - [Playlist Machine Learning](https://youtube.com/playlist?list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&si=HRfbLNkmB-wwJ8Ys)

8. Học deep learning
   - [Playlist Deep Learning](https://youtube.com/playlist?list=PL-DKonjOZsHYAnadxsrdwd4VkWKEHf0Pw&si=UAKnww9X4yEw6kIP)

9. Học Docker để đóng gói mô hình và triển khai thực tế
   - [Docker video 1](https://youtu.be/Gh1Sgknc6Fg?si=YtpMSvJV2wPSW4yS)
   - [Docker video 2](https://www.youtube.com/watch?v=o9Si96339Ig)

10. Học về Hugging Face để fine-tune mô hình
   - Làm chủ thư viện `transformers` và `datasets`
   - Fine-tuning với `PEFT`, `LoRA` / `QLoRA`
   - Đóng gói và triển khai lên Hugging Face Spaces

11. Học FastAPI để xây dựng backend đơn giản và triển khai
   - [FastAPI playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ)

12. Học AWS: các kiến thức cloud quan trọng để tận dụng AI
   - `EC2`, `S3`, `ECS`

13. Ôn tập cơ sở dữ liệu quan hệ
   - PostgreSQL

14. Ôn tập cơ sở dữ liệu phi quan hệ
   - MongoDB

15. Tối ưu hóa cơ sở dữ liệu
   - Indexing
   - Vector database

16. Học cách sử dụng AI coding tools
   - Claude Code, Codex, GitHub Copilot, ChatGPT, Grok

## Kỹ năng mềm

### Thái độ

- Tuần đầu tiên nên quan sát quy trình làm việc, văn hóa công ty và đồng nghiệp.
- Đến sớm hoặc ít nhất đúng giờ.
- Không xem máy tính cá nhân của người khác khi chưa được phép.
- Lắng nghe nhiều hơn trước khi phát biểu.
- Tránh kể về gia đình và đời sống cá nhân.
  - Ví dụ: “Dạ nhà em cũng bình thường ạ, cuối tuần em hay đá bóng/học code thôi.”
- Không hỏi về chuyện cá nhân của đồng nghiệp.
- Làm đúng task, estimate cho đúng và thêm dự phòng (~1.5x thời gian).
- Chủ động hỏi khi cần.
  - Quy tắc 15 phút: tự tìm, tự debug, tự prompt AI trong 15 phút, nếu vẫn bế tắc thì hỏi kèm cấu trúc rõ ràng.
- Có khả năng giao tiếp tiếng Anh trong công việc.
- Chuẩn bị nội dung quan trọng trước khi thực hiện task.

### Chuẩn bị

- CV: sử dụng [Overleaf](https://www.overleaf.com) và ChatGPT / Grok để kiểm tra.
  - [Video tham khảo](https://www.youtube.com/watch?v=2fqXC4RQyOw)
- Hiểu rõ công ty, khách hàng, nhiệm vụ và văn hóa để chuẩn bị giải pháp phù hợp.

### Kỹ năng tìm code và định vị lỗi

- `Ctrl + P` hoặc `Cmd + P`: tìm file nhanh.
- `Ctrl + F` hoặc `Cmd + F`: tìm text trong file.
- Khi đọc code, xem class/method gọi gì và làm gì, rồi prompt AI rõ ràng để sửa và tối ưu.

### Kỹ năng GitHub

- Tạo nhánh mới và chuyển sang nhánh đó:
  - `git checkout -b ten_nhanh_moi`
- Lấy code mới nhất từ `main`:
  - `git checkout main`
  - `git pull origin main`
- Tạo pull request (PR): đặt tên chuẩn, assign người review.
- Thêm file làm việc:
  - `git add <ten_file>`
- Commit nội dung:
  - `git commit -m 'feat: them file A...'`
- Push code:
  - `git push origin ten_nhanh_moi`
- Khi code bị lỗi:
  - Nếu chưa push: `git reset --hard HEAD`
  - Nếu đã push: báo Mentor/Senior và phối hợp xử lý an toàn.
- Xử lý Conflict (Xung đột code): Khi bạn và đồng nghiệp cùng sửa chung một file và push lên. Hãy học cách dùng VS Code hoặc Cursor để giải quyết conflict (Accept Incoming Change hoặc Accept Current Change).

- Viết Commit Message chuẩn (Conventional Commits): Đừng viết commit vô thưởng vô phạt. Hãy tuân thủ chuẩn:

    - feat(auth): add login validation using pydantic

    - fix(model): resolve cuda oom by reducing batch size to 4

    - docs(readme): update deployment instructions

### Kỹ năng đọc log bằng terminal / CMD

#### 1. Đọc log trạng thái phần cứng

- Lỗi kinh điển `RuntimeError: CUDA out of memory (OOM)`:
  - Dấu hiệu: log có dòng `Tried to allocate X MiB...`
  - Xử lý: giảm `batch_size`, dùng gradient accumulation, áp dụng quantization (8-bit, 4-bit), hoặc LoRA/QLoRA.
- Theo dõi GPU:
  - `watch -n 1 nvidia-smi`
  - Nếu `GPU-Util < 50%`: bottleneck có thể do CPU / DataLoader chậm.
  - Giữ VRAM ở mức an toàn ~85-90%.

#### 2. Đọc log tiến trình huấn luyện

- Dòng log tiêu chuẩn:
  - `Epoch 3/10 | Step 500/1000 | Loss: 0.4213 | Val_Loss: 0.5122 | Learning_Rate: 1e-4 | Accuracy: 85.3%`
- Phân loại lỗi:
  - Overfitting: train loss giảm nhưng val_loss tăng.
    - Xử lý: Early Stopping, data augmentation, dropout.
  - Underfitting: loss giảm chậm và vẫn cao.
    - Xử lý: dùng mô hình lớn hơn, tăng learning rate, thêm dữ liệu.
  - Loss = `nan` hoặc `inf`:
    - Xử lý: giảm learning rate, gradient clipping (`max_norm=1.0`), kiểm tra giá trị null/NaN.

#### 3. Đọc log khi đưa mô hình lên production

- Latency log:
  - Ví dụ: `POST /v1/predict - Status: 200 - Time: 2450ms`
  - Xử lý: tối ưu ONNX/TensorRT, dùng async FastAPI, chạy inference trên GPU.
- Lỗi input shape/type:
  - Ví dụ: `ValueError: Expected 4D tensor as input, but got 3D tensor instead.`
  - Nguyên nhân: thiếu chiều batch.
  - Sửa: `numpy.expand_dims(image, axis=0)` hoặc `torch.unsqueeze(tensor, 0)`.

## Pháp luật cần biết

Tham khảo:
- [Bộ luật Lao động 2019](https://thuvienphapluat.vn/van-ban/Lao-dong-Tien-luong/Bo-Luat-lao-dong-2019-333670.aspx)

### 1. Giấy tờ gốc
- Công ty không được giữ bản chính giấy tờ tùy thân (CCCD, hộ chiếu) hoặc bằng cấp.
- Không được bắt nộp tiền mặt hoặc tài sản để làm bảo đảm hợp đồng.

### 2. Lương thử việc
- Lương thử việc tối thiểu bằng 85% lương chính thức.
- Trong thời gian thử việc, mỗi bên có thể hủy bỏ thỏa thuận ngay lập tức mà không cần bồi thường.

### 3. Thời gian thử việc
- Tối đa 60 ngày: trình độ Cao đẳng, Đại học.
- Tối đa 30 ngày: trình độ Trung cấp, kỹ thuật.
- Tối đa 6 ngày: công việc phổ thông.

### 4. Quyền đơn phương nghỉ việc
- Bạn có quyền nghỉ việc theo nguyện vọng nếu tuân thủ thời gian báo trước.
- Thông thường:
  - 45 ngày với hợp đồng không thời hạn.
  - 30 ngày với hợp đồng có xác định thời hạn 12-36 tháng.
- Nếu nghỉ ngang không báo trước, có thể phải bồi thường nửa tháng lương.

### 5. Điều chuyển công tác
- Công ty chỉ được điều chuyển công tác tối đa 60 ngày trong 1 năm.
- Nếu quá 60 ngày, phải có sự đồng ý bằng văn bản.
- Nếu lương công việc mới thấp hơn cũ, vẫn được giữ nguyên mức lương cũ trong 30 ngày đầu.

### 6. Từ chối làm việc khi nguy hiểm
- Bạn có quyền từ chối làm việc nếu nguy cơ đe dọa tính mạng hoặc sức khỏe.
