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
2: Tinh chỉnh mô hình (Fine-tuning)
3: Đóng gói và Triển khai lên hugging face spaces

- 8. Học fastapi để xây dựng backend đơn giản để triển khai, hiểu để vibe code làm frontend tương ứng
https://www.youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ


- 9. Học AWS những kiến thức cloud quan trọng cốt lỗi để tận dụng AI 

- 10. Ôn tập cơ sở dữ liệu quan hệ(Postgresql)

- 11. Ôn tập cơ sở không quan hệ(MongoDB)

## Kỹ năng mềm: 
- Thái độ
    - Khi đi làm 1-2 tuần đầu tiên nên xem quy trình làm việc của công ty, văn hóa của công ty, các anh chị đồng nghiệp. Để biết làm theo, nên đến sớm hoặc ít nhất đúng giờ

    - Không được xem máy tính cá nhân của người khác khi chưa được cho phép

    - Lắng nghe nhiều hơn, trước khi nói 1 điều gì đó. 

    - Đừng kể về gia đình và cuộc sống cá nhân -> Dạ nhà em cũng bình thường ạ, cuối tuần em hay đá bóng/học code thôi

    - Làm đúng task, estimate cho đúng trước khi bước vào làm việc.

    - Chủ động hỏi: Đừng giấu dốt. Nhưng trước khi hỏi Senior/Mentor, hãy áp dụng quy tắc 15 phút: Tự tìm câu trả lời, tự debug, tự prompt AI trong 15 phút. Nếu vẫn bế tắc, hãy đến hỏi kèm theo cấu trúc: "Em đang làm task X, gặp lỗi Y, em đã thử cách A và B nhưng chưa được, anh/chị xem giúp em đoạn này với". Nhà tuyển dụng cực kỳ thích cách hỏi có tư duy này.

    - Có thể giao tiếp được tiếng anh trong công việc liên quan

    - Gợi ý cần tìm hiểu gì để thực hiện task đó...

    - Không hỏi việc cá nhân của đồng nghiệp

- Chuẩn bị
    - cv: có thể làm cv theo https://www.overleaf.com sử dụng chat gpt, grok... để kiểm tra cv ổn chưa
    https://www.youtube.com/watch?v=2fqXC4RQyOw

    - Hiểu rõ hơn về công ty, khách hàng của họ là ai, nhiệm vụ của mình là gì, văn hóa là gì, tập trung vào cái gì -> có thể chúng ta cần đáp ứng gì?
    
- Kỹ năng tìm code, định vị lỗi:
    - control + P hoặc cmd + P: tìm file
    - control + F hoặc cmd + F: tìm text trong file
    - khi đọc code cần xem class đó gọi class gì, làm những gì, và prompt cho AI cái mình muốn fix, và tối ưu công việc

- Kỹ năng github:
    - tạo nhánh: git branch -b ten_nhanh_moi
    - lấy code về từ main/master: git checkout main/master  -> git pull 
    - tạo pull request đặt tên cho đúng theo quy định của công ty, assign đúng người review hoặc có thể hỏi những đồng nghiệp xung quanh
    - muốn quay về code ban đầu khi code push lên bị hư: git revert ... (hỏi AI để làm cho nhanh nếu hư trên nhiều nhánh thì nhớ gộp lại rồi push lên, tất cả các test cases pass mới được merge)
    - thêm code mới làm vào: git add (ten file)
    - thêm nội dung vào cái mình thêm: git commit -m 'them file A...'
    - push code: git push (lần đầu tiên thì nó có hiển thị khi mình nhấn git push, copy đó bỏ vào terminal)

- Kỹ năng đọc Log bằng terminal/ cmd:
    - 1. Đọc Log Trạng Thái Phần Cứng (Hardware Logs)   

    + Lỗi kinh điển RuntimeError: CUDA out of memory (OOM):

        Dấu hiệu: Log hiện một bảng dài các block bộ nhớ kèm dòng chữ Tried to allocate X MiB....

        Cách xử lý: Đây không phải lỗi code, mà do GPU hết RAM. Bạn cần hạ batch_size xuống (ví dụ từ 32 xuống 16), sử dụng kỹ thuật Gradient Accumulation, áp dụng Quantization (8-bit, 4-bit), hoặc dùng LoRA/QLoRA (peft) nếu đang fine-tune LLM.

    + Theo dõi GPU theo thời gian thực:

        Khi chạy script training ngầm, hãy mở một Terminal khác và gõ: watch -n 1 nvidia-smi.

        Cần nhìn vào đâu?

        GPU-Util (Hiệu suất sử dụng): Nếu con số này quá thấp (< 50%) trong khi đang train, chứng tỏ có hiện tượng Bottleneck ở CPU (CPU xử lý/tiền xử lý dữ liệu với Pandas/Dataloader quá chậm, không kịp "mớm" cho GPU ăn). Bạn cần tăng num_workers trong DataLoader lên.

        Memory-Usage: Giữ mức an toàn khoảng 85-90% dung lượng VRAM, đừng để sát nút 100% vì rất dễ crash giữa chừng khi gặp các sample dữ liệu dài hơn.

    -   2. Đọc Log Tiến Trình Huấn Luyện (Training/Fine-tuning Logs)

        + Một dòng log tiêu chuẩn thường có dạng:

            Epoch 3/10 | Step 500/1000 | Loss: 0.4213 | Val_Loss: 0.5122 | Learning_Rate: 1e-4 | Accuracy: 85.3%

            Kỹ năng "bắt bệnh" qua chỉ số:
            Mô hình bị Overfitting (Quá khớp):

            Dấu hiệu: Loss (trên tập train) liên tục giảm rất đẹp, nhưng Val_Loss (trên tập validation) sau một vài epoch bắt đầu đứng im rồi tăng ngược trở lên.

            Hành động: Bạn phải dừng train sớm (Early Stopping), tăng cường dữ liệu (Data Augmentation), hoặc thêm Dropout/Regularization vào mô hình.

        + Mô hình bị Underfitting (Chưa đủ tốt):

            Dấu hiệu: Cả Loss và Val_Loss đều giảm cực kỳ chậm và dừng lại ở một con số rất cao, độ chính xác (Accuracy/mAP) lẹt đẹt.

            Hành động: Mô hình quá bé hoặc bài toán quá khó. Cần đổi sang kiến trúc mô hình lớn hơn, tăng learning_rate, hoặc train thêm nhiều epoch nữa.

            Lỗi Loss: nan hoặc Loss: inf (Nổ gradient / Triệt tiêu gradient):

            Dấu hiệu: Đột nhiên chỉ số Loss biến thành nan (Not a Number) hoặc inf (Infinity). Mô hình chính thức bị hỏng hoàn toàn từ step đó.

            Hành động: Giảm learning_rate xuống ngay lập tức (thường là chia 10), áp dụng Gradient Clipping (max_norm=1.0), và kiểm tra lại xem dữ liệu đầu vào có bị dính giá trị Null/NaN nào sau khi dùng Pandas xử lý không.

    -   3. Đọc Log Khi Đưa Mô Hình Lên Production (Inference Logs)
        Khi bạn đóng gói mô hình Hugging Face vào FastAPI và chạy thực tế, log lúc này sẽ phục vụ cho việc giám sát (Monitoring).

        - Log về Thời gian phản hồi (Latency Log):

            + Ví dụ: POST /v1/predict - Status: 200 - Time: 2450ms

                Phân tích: Thời gian xử lý mất tận 2.4 giây là quá chậm cho một ứng dụng thực tế. Nhìn vào log này, bạn biết mình cần phải tối ưu hóa: Chuyển mô hình sang định dạng ONNX hoặc TensorRT, sử dụng Async trong FastAPI, hoặc chuyển từ chạy Inference trên CPU sang GPU.

            + lỗi định dạng dữ liệu đầu vào (Input Shape/Type Error):

                Lỗi phổ biến: ValueError: Expected 4D tensor as input, but got 3D tensor instead.

                Phân tích: Mô hình DL luôn đòi hỏi dữ liệu theo dạng Batch (ví dụ: [batch_size, channels, height, width]). Log này báo hiệu bạn đã quên không "add batch dimension" trước khi truyền ảnh vào mô hình.

                Cách sửa: Dùng numpy.expand_dims(image, axis=0) hoặc torch.unsqueeze(tensor, 0).