from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_excel("/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson09/final_project.ods", dtype=str)
target = "career_level"
data = data.dropna(axis=0)

X = data.drop(columns=[target], axis=1)
y = data[target]


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# stratify = y để cho chia đều với tỷ lệ 80/20 cho từng classes
print(y_train.value_counts())

print(data.info())


vectorizer = TfidfVectorizer()
output = vectorizer.fit_transform(x_train["title"])
print(output.shape)