from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def create_recursive_data(data, window_size=5):
    i = 1
    while(i < window_size):
        data["co2_{}".format(i)] = data["co2"].shift(-i)
        i += 1
    data["target"] = data["co2"].shift(-window_size)
    data = data.dropna(axis=0)
    return data

df = pd.read_csv("/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson12/co2.csv")

# dùng các điểm xung quanh để nội suy giá trị bị thiếu
df["co2"] = df["co2"].interpolate()
print(df.info())

df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d")

# fig, ax = plt.subplots()
# ax.plot(df["time"], df["co2"])
# ax.set_xlabel("time")
# ax.set_ylabel("co2")

plt.show()

df = create_recursive_data(df, window_size=5)
print(df)
print("correlation: ", df.drop("time", axis=1).corr())


# chia tập dữ liệu
x = df.drop(["time", "target"], axis=1)
y = df["target"]

train_size = 0.8
num_sample = len(x)

x_train = x[:int(num_sample*train_size)]
y_train = y[:int(num_sample*train_size)]

x_test = x[int(num_sample*train_size):]
y_test = y[int(num_sample*train_size):]



# chọn mô hình
# -> bởi vì hệ số tương quan cao nên ta chọn mô hình tuyến tính
model = LinearRegression()
model.fit(x_train, y_train)

# dự đoán
y_pred = model.predict(x_test)
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
print(mean_absolute_error(y_test, y_pred))

# trực quan hóa
fig, ax = plt.subplots()
ax.plot(df["time"][:int(num_sample*train_size)], y_train, label="train")
ax.plot(df["time"][int(num_sample*train_size):], y_test, label="test")
ax.plot(df["time"][int(num_sample*train_size):], y_pred, label="pred")
ax.legend()
ax.set_xlabel("time")
ax.set_ylabel("co2")
ax.grid()
plt.show()