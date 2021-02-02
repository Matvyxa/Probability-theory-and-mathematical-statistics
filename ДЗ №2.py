# 1.Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial


def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


A = arg(100, 85, 0.8, 0.2)
print("%.3f" % A)
# Ответ 0,048

# 2.Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

import numpy as np


def arg(m, n, p):
    return float((n * p) ** m / np.math.factorial(m)) * np.exp(-(n * p))


B1 = arg(0, 5000, 0.0004)
print("%.3f" % B1)


# Ответ 0,135

def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


B2 = arg(5000, 2, 0.0004, 0.9996)
print("%.3f" % B2)


# Ответ 0,271 Попробовал решить 2 способами с помощью Пуассона и Бернули ответы одинаковые

# 3.Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


C = arg(144, 70, 0.5, 0.5)
print("%.3f" % C)


# Ответ 0,063


# 4.В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


D1 = arg(10, 7)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


D2 = arg(10, 2)

D = D2 / D1


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


E1 = arg(11, 9)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


E2 = arg(11, 2)

E = E2 / E1


def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


F = arg(4, 4, D, E)

print("%.3f" % F)


# Ответ 0,02

# Какова вероятность того, что ровно два мяча белые?

def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


G11 = arg(10, 7)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


G12 = arg(10, 0)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


G13 = arg(10, 1)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


G14 = arg(10, 2)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


H11 = arg(11, 9)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


H12 = arg(11, 2)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


H13 = arg(11, 1)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


H14 = arg(11, 0)


def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


J1 = arg(4, 2, G12 / G11, H12 / H11)
J2 = arg(4, 2, G13 / G11, H13 / H11)
J3 = arg(4, 2, G14 / G11, H14 / H11)
J = J1 + J2 + J3
print("%.3f" % J)


# Ответ 0,002

# Какова вероятность того, что хотя бы один мяч белый?

def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


K11 = arg(10, 7)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


K12 = arg(10, 0)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


K13 = arg(10, 1)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


L11 = arg(11, 9)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


L12 = arg(11, 1)


def arg(n, k):
    return float(factorial(n) / (factorial(k) * factorial(n - k)))


L13 = arg(11, 0)


def arg(n, k, p, q):
    return float(factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * q ** (n - k))


M1 = arg(4, 2, K12 / K11, L12 / L11)
M2 = arg(4, 2, K13 / K11, L13 / L11)

M = M1 + M2
print("%.5f" % M)
# Ответ 0,00003
