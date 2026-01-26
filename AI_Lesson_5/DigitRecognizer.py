from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

#mnist = fetch_openml('mnist_784',version=1)

x = mnist['data'] / 255.0
y = mnist['target'].astype(int)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

model = LogisticRegression(max_iter=10000)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test,y_pred)
print(f"Test Accuracy:{accuracy}")

for i in range(5):
    plt.imshow(x_test.iloc[i].values.reshape(28,28),cmap=plt.cm.biinary)
    plt.title(f"Predicted:{y_pred[i]}, Actual:{y_test.iloc[i]}")
    plt.show()
