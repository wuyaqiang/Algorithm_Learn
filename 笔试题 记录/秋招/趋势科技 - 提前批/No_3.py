import numpy as np


def gradient_descent(X, y, lr=0.01, threshold=1e-3):
    params = np.array([0., 0., 0.])

    error = float('inf') # 当前误差，当误差小于阈值 threshold 时，停止更新参数
    while error > threshold:

        bias = np.array([params[2]] * X.shape[0])   # 取第三列参数 bias
        grad =  np.dot(X.T, (np.dot(X, params[:,0:2]) + bias - y)) / X.shape[0] # 计算梯度
        params = params - lr * grad # 根据学习率更新参数
        error = np.linalg.norm(np.dot(X, params) - y)   # 计算误差

    return params

#
# Please don't modify any code below.
#
if __name__ == "__main__":
    # Code to generate the data/test case
    n_samples = 10000
    x_1, x_2 = np.random.random(n_samples), np.random.random(n_samples)
    theta_1, theta_2, b = map(float, input().split())
    # print (theta_1, theta_2, b)
    X, y = np.vstack([x_1, x_2]).T, theta_1 * x_1 + theta_2 * x_2 + b
    # Solution
    params = gradient_descent(X, y)
    result = []
    for param in params:
        result.append('{:.02f}'.format(param))
    print(' '.join(result))