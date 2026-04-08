import numpy as np
import matplotlib.pyplot as plt

def Simple_linear_regression(X,Y):
    X = np.c_[np.ones(X.shape[0]),X]

    theta = np.linalg.inv(X.T@X)@X.T@Y
    return theta
def predict(X,theta):
    X = np.c_[np.ones(X.shape[0]),X]
    return X@theta

np.random.seed(0)
X =2* np.random.rand(100,1)
Y =4+3*X + np.random.randn(100,1)

theta =Simple_linear_regression(X,Y)
print("Theta:",theta)
Y_pred = predict(X,theta)
 
plt.scatter(X, Y,color='blue',Label='datapoints')

plt.plot(X,Y_pred,color='red',Label='regression line')
plt.xlabel('X')
plt.ylabel('Y') 
plt.show()