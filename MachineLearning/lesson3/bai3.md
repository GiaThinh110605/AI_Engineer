https://www.youtube.com/watch?v=bpK8oQyaVJE&list=PL-DKonjOZsHZJ3PCSLE3fE9sFMZ_zWkXO&index=7

### Bài toán binary Classification: có 2 lớp
+ balanced dataset, unbalanced dataset
+ thông thường trong thực tế quan tâm là class ít hơn

+ Với bộ dữ liệu cân bằng thì có thể dùng accuracy để đánh giá 
+ Với bộ dữ liệu không cân bằng thì cần dùng precision, recall, F1 score để đánh giá

+ confusion matrix: TP, FP, TN, FN

+ precision = TP / (TP + FP) (trong tất cả dự đoán là positive thì mô hình dự đoán đúng là bao nhiêu -> chất lượng) 
(tiếng anh cho pv: Out of all predicted positives, how many did the model predict correctly? -> Quality / Correctness)

+ recall = TP / (TP + FN) (trong tất cả thực tế là positive thì mô hình dự đoán đúng là bao nhiêu -> về mặt số lượng)
(tiếng anh cho pv: Out of all actual positives, how many did the model predict correctly? -> Quantity / Completeness)

+ F1 score = 2 * (precision * recall) / (precision + recall) (trong bài toán thực tế mà không thể  chọn precision hay recall thì dùng F1 score để đánh giá)
(tiếng anh cho pv: In a real-world scenario, if we don't distinguish between precision and recall, we choose the F1 score.)

+ accuracy = (TP + TN) / (TP + FP + TN + FN)

+ Ví dụ về nên chọn precision (chất lượng) hay recall (số lượng):
    + Mình đang tán bạn gái thì chọn một vài quán ăn, và chọn duy nhất 1 quán để đến đó ăn 
    -> chọn precision
    + Lúc covid thì có 2 loại: positive (có bệnh) và negative (không bệnh)
    -> chọn recall (vì có thể lây nhiễm nên bắt tất cả người có liên quan)

+ Threshold: ngưỡng để phân loại (ví dụ: 0.5)
    + Nếu dự đoán >= threshold thì dự đoán là positive
    + Nếu dự đoán < threshold thì dự đoán là negative

+ ROC curve: Receiver Operating Characteristic curve
    + TPR (True Positive Rate) = recall = TP / (TP + FN)
    + FPR (False Positive Rate) = FP / (FP + TN)
    + AUC (Area Under the Curve): diện tích dưới đường cong ROC, giá trị từ 0 đến 1, càng gần 1 thì mô hình càng tốt
-> giúp chọn ngưỡng(threshold) phù hợp để phân loại (TPR - FPR cao nhất) 