# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла
# (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
import numpy as np
# x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110], dtype=np.float64)
# y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832], dtype=np.float64)
# b= (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)- np.mean(x)**2)
# b = 2.62054
# a = np.mean(y)-b*np.mean(x)
# a = 444.17736
# Y_hat = a + b*x
# [535.89626 562.10166 942.07996 968.28536 548.99896 627.61516 585.68652
#  837.25836 758.64216 732.43676]
# import matplotlib.pyplot as plt
# "%matplotlib inline"
# plt.scatter(x, y)
# plt.plot(x, a+b*x)
# plt.show()

from sklearn.linear_model import LinearRegression

# x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]).reshape((-1, 1))
# y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# r_sq = 0.78763
# 'intercept:' = 444.17736
# 'slope:' = 2.62054
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)

# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept). *3.
# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import seaborn as sns

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


# X = x.reshape((10, 1))
# Y = y.reshape((10, 1))
# X = np.hstack([np.ones((10, 1)), X])
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)


def mse_(B1, y=y, x=x, n=10):
    return np.sum((B1 * x - y) ** 2) / n


alpha = 1e-7
B1 = 0.5
n = 10

mse = (2 / n) * np.sum((B1 * x - y) * x)
for i in range(100):
    B1 = alpha * (2 / n) * np.sum((B1 * x - y) * x)
    ('B1={}'.format(B1))

for i in range(100):
    B1 = alpha * (2 / n) * np.sum((B1 * x - y) * x)
    if i % 10 == 0:
        print('iteration: {i}, B1 ={B1}, mse={mse}'.format(i=i, B1=B1, mse=mse_(B1)))
# mse_ = 537071.4149