from lazypredict.Supervised import LazyClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV


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

params = {
    "n_estimators": [100, 500, 1000],
    "criterion": ["gini", "entropy"]
}

model = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=params,
    verbose=2,
    cv=5,
    n_jobs=3,
    scoring="recall_macro"
)
model.fit(X_train, y_train)
predict = model.predict(X_test)
print(model.best_params_)
print(model.best_score_)
print(classification_report(y_true=y_test, y_pred=predict))
