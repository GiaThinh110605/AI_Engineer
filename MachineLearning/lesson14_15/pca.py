import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

with np.load("/Users/mac/Downloads/AI_Engineer/MachineLearning/Datasets/mnist.npz") as f:
    x_train, y_train = f["x_train"], f["y_train"]
    x_test, y_test = f["x_test"], f["y_test"]

x_train = np.reshape(x_train, (x_train.shape[0], -1))
x_test = np.reshape(x_test, (x_test.shape[0], -1))

pca_2d = make_pipeline(StandardScaler(), PCA(n_components=2))
x_pca_2d = pca_2d.fit_transform(x_train)

pca_model = pca_2d.named_steps["pca"]
explained_variance = pca_model.explained_variance_ratio_ * 100

plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    x_pca_2d[:, 0],
    x_pca_2d[:, 1],
    c=y_train,
    cmap="tab10",
    s=8,
    alpha=0.6,
)

plt.title("Truc quan hoa MNIST bang PCA 2D")
plt.xlabel(f"Thanh phan chinh 1 ({explained_variance[0]:.2f}% phuong sai)")
plt.ylabel(f"Thanh phan chinh 2 ({explained_variance[1]:.2f}% phuong sai)")
plt.grid(alpha=0.25)

colorbar = plt.colorbar(scatter, ticks=range(10))
colorbar.set_label("Chu so")

plt.tight_layout()
plt.savefig("/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson14_15/pca_mnist_2d.png", dpi=200)
plt.show()
