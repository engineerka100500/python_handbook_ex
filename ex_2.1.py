# A
""" 
print("Привет, Яндекс!") """

# B 
""" 
username = input("Как Вас зовут?")
print("Привет,", username) """

# C 
""" 
username = input()
print(username, "\n", username, "\n", username, "\n")"""

"""
username = input()
print(username)
print(username)
print(username) """

# D
"""  
money = int(input())
print(int(money - int(2.5 * 38))) """

# E
""" 
cost = int(input())
weight = int(input())
money = int(input())
print(int(money - cost * weight)) """

# F вывод с помощью f-строк 
""" 
name = input()
cost = int(input())
weight = int(input())
money = int(input())

print("Чек")
print(f"{name} - {weight}кг - {cost}руб/кг")
print(f"Итого: {cost * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {int(money - cost * weight)}руб")
 """

# G
""" 
N = int(input())
print("Купи слона!\n" * N)
 """

# H 
""" 
N = int(input())
string = input()
print(f"Я больше никогда не буду писать \"{string}\"!\n" * N) """

# I 
""" 
N = int(input())
M = int(input())
sausage = int(1 / 2 * N * M)
print(sausage) """

# J
""" 
name = input()
number = int(input())
print(f"Группа №{number // 100 % 10}.")
print(f"{number % 10}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {number // 10 % 10}.")

 """

# K
""" 
number = int(input())
a = str(number // 1000)
b = str(number // 100 % 10)
c = str(number // 10 % 10)
d = str(number % 10)

number1 = b + a + d + c
print(int(number1))
 """

# L 
# вычленить все цифры числа
""" number1 = int(input())
b1 = number1 // 100
c1 = number1 // 10 % 10
d1 = number1 % 10

number2 = int(input())
b2 = number2 // 100
c2 = number2 // 10 % 10
d2 = number2 % 10

b = str((b1 + b2) % 10)
c = str((c1 + c2) % 10)
d = str((d1 + d2) % 10)

print(int(b + c + d)) """

# M 
""" 
children = int(input())
sweets = int(input())

sweet_every = sweets // children
residue = sweets % children

print(sweet_every)
print(residue)
 """
# N 
""" 
r = int(input())
g = int(input())
b = int(input())
res = r + b + 1
print(res) """

# O
""" 
N = int(input()) # часы
M = int(input()) # минуты 
T = int(input())

min = (T % 60 + M) % 60
# (52+15)// 60
hours = (T // 60 + N + (T % 60 + M) // 60) % 24
if (hours < 10 and min < 10):
    print(f"0{hours}:0{min}")
elif (hours < 10):
    print(f"0{hours}:{min}")
elif (min < 10):
    print(f"{hours}:0{min}")
else:
    print(f"{hours}:{min}")
 """
# P 
# вывод с округлением до сотых 
# до второго знака после запятой 
""" 
A = int(input())
B = int(input())
C = int(input())

print(f"{(B - A) / C:.2f}")
 """

# Q 
# 1101 = 13
""" 
before = int(input())
binary_value = input()
last = int(binary_value, 2)
print(before + last)
 """

# R 
""" 
binary_value = input()
bill = int(input())

surrender = bill - int(binary_value, 2)
print(surrender) """

# S Украшение чека
""" 
name = input()
cost = int(input())
weight = int(input())
money = int(input())
print("=" * 16, "Чек", "=" * 16, sep="")
print(f"Товар:{f'{name}': >29}")
print(f"Цена: {f'{weight}кг * {cost}руб/кг': >29}")
print(f"Итого: {f'{cost * weight}руб': >28}")
print(f"Внесено: {f'{money}руб': >26}")
print(f"Сдача: {f'{int(money - cost * weight)}руб': >28}")
print("=" * 35) """

# T котлеты 
# K2 < K1 
""" 
# помоечка
# weight1 = int((N * M - K2 * (N - weight1)) / K1)
# weight2 = N - weight1 """

""" 
import numpy as np 
from scipy.linalg import solve

N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

A = np.array(
    [
        [K1, K2],
        [1, 1],
    ]
)
b = np.array([N * M, N]).reshape((2, 1))
w = solve(A, b)
print(round(*w[0]), round(*w[1]), sep=' ') """