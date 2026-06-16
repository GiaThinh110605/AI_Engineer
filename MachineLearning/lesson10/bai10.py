from multiprocessing.resource_sharer import stop
from threading import local
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import re

# Tiền xử lý:
# cột 1: title: chuyển thành vector số, giúp hạ thấp những từ quá chung chung, tăng trọng số cho những từ trực
# tiếp ảnh hưởng đến output ví dụ: lead, developers...
# cột 2: location: chỉ lấy bang để gom cụm dữ liệu, giảm số lượng dòng, xử lý dữ liệu thưa thớt, sau đó onehot để đưa về số máy tính có thể hiểu được
# cột 3: description: sử dụng loại bỏ stopwords, unigram + bigram 
# cột 4: function: sử dụng onehot encoding vì để cho máy tính hiểu con số và chấp nhận được số lượng cột trong shape
# cột 5: industry: có thể sử dụng cả onehot encoding hoặc cả TF-idf
def filer_location(location):
    # 1. sử dụng hàm tự viết
    # if location[-4:-2] == ", " and location[-2:].isupper():
    #     return location[-2:]
    # else:
    #     return location

    # 2. sử dụng regular expression
    location_new = re.findall(pattern="\,\s[A-Z]{2}$", string=location)
    if len(location_new) == 0:
        return location
    else:
        return location[-2:]

    
data = pd.read_excel("/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson09/final_project.ods", dtype=str)
data = data.dropna(axis=0)
data["location"] = data["location"].apply(filer_location)
target = "career_level"

X = data.drop(columns=[target], axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# stratify = y để cho chia đều với tỷ lệ 80/20 cho từng classes
print(y_train.value_counts())

print(data.info())


preprocessor = ColumnTransformer(
    transformers=[
        ("title", TfidfVectorizer(), "title"),
        ("location", OneHotEncoder(handle_unknown='ignore'), ["location"]),
        ("description", TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.99, stop_words="english"), "description"),
        ("func", OneHotEncoder(handle_unknown='ignore'), ["function"]),
        ("ind", TfidfVectorizer(), "industry")
    ]
)
# unigram + bigram: (6458, 850808)
# unigram + bigram + min_df + max_df: (6458, 8043)

# output = preprocessor.fit_transform(x_train)
# print(output.shape)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestClassifier(random_state=42))
])

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))



