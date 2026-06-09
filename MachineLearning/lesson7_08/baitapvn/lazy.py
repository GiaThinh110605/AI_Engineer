from lazypredict.Supervised import LazyClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson7/baitapvn/csgo.csv")
print(data.head())
print(data.info())

col = ["rownames", "day", "month", "year", "date", "wait_time_s", "match_time_s", "team_a_rounds", "team_b_rounds"]
X = data.drop(columns=col)
Y = data["result"]
print(X.corr(numeric_only = True))

map_counts = data["map"].value_counts()
small_counts = map_counts[map_counts < 5].index
X["map"] = X["map"].replace(small_counts, "Other")
X_encoded = pd.get_dummies(X, dtype=int)


X_train, X_test, y_train, y_test = train_test_split(X_encoded,Y, test_size=0.15, random_state=42, stratify=Y)

standard = StandardScaler()
X_train = standard.fit_transform(X_train)
X_test = standard.transform(X_test)

lazy = LazyClassifier(verbose=1, random_state=42)
model, predict = lazy.fit(X_train, X_test, y_train, y_test)

print(model)
