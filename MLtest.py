import numpy as np
import matplotlib.pyplot as plt
import time

data = np.loadtxt('MLdata.txt')
#data 第一列为温度信息 第二列为人口信息
X = data[:,0].reshape(-1,1)
#data 第三列为用电量信息
Y = data[:,2].reshape(-1,1)

def preprocess_data(X):
    """输入预处理 在X前面加一列1
    参数：
        X:原始数据，shape为 mx1
    返回：
        X_train: 在X加一列1的数据，shape为 mx2
    """

    m = X.shape[0]   # m 是数据X的行数
    ### START CODE HERE ###
    One = np.ones(m).reshape(-1,1)
    X_train = np.hstack((One, X))
    X = []
    
    ### END CODE HERE ###
    return X_train

preprocess_data(X)
print(X)
