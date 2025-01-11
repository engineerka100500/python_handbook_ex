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
cost, weight, money = int(input()), int(input()), int(input())
print(int(money - cost * weight)) """

# F вывод с помощью f-строк 
""" 
name, cost, weight, money = input(), int(input()), int(input()), int(input())

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
N, string = int(input()), input()
print(f"Я больше никогда не буду писать \"{string}\"!\n" * N) """

# I 
""" 
N, M = int(input()), int(input())
print(int(N * M // 2)) """

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
""" 
number1, number2 = input(), input()
if len(number2) > len(number1): 
    number1, number2 = number2, number1

if len(number1) > len(number2):
    number2 = "0" * (len(number1) - len(number2)) + number2

print("".join(map(lambda x, y: str((int(x) + int(y)) % 10), number1, number2)))
"""
"""
# второй способ
number1 = int(input())
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
children, sweets = int(input()), int(input())
print(sweets // children)
print(sweets % children)  # остаток"""

# N 
""" 
r, g, b = int(input()), int(input()), int(input())
print(r + b + 1) """

# O
""" 
N, M, T = int(input()), int(input()), int(input())
min = (T % 60 + M) % 60
hours = (T // 60 + N + (T % 60 + M) // 60) % 24
print(f"{hours:0>2}:{min:0>2}")
# (52+15)// 60
 """
# P 
# вывод с округлением до сотых 
# до второго знака после запятой 
""" 
A, B, C = int(input()), int(input()), int(input())
print(f"{(B - A) / C:.2f}")
 """

# Q 
# 1101 = 13
""" 
sum_before, binary_value = int(input()), int(input(), 2)
print(sum_before + binary_value)
"""

# R 
""" 
binary_value, bill = input(), int(input())
print(bill - int(binary_value, 2)) """

# S Украшение чека
""" 
name, cost, weight, money = input(), int(input()), int(input()), int(input())

print(f"{'Чек':=^35}")
print(f"Товар:{f'{name}': >29}")
print(f"Цена: {f'{weight}кг * {cost}руб/кг': >29}")
print(f"Итого: {f'{cost * weight}руб': >28}")
print(f"Внесено: {f'{money}руб': >26}")
print(f"Сдача: {f'{int(money - cost * weight)}руб': >28}")
print("=" * 35) """

# T котлеты 
""" 
N, M, K1, K2 = int(input()), int(input()), int(input()), int(input())
weight1 = (N * M - K2 * N) // (K1 - K2)
weight2 = N - weight1
print(weight1, weight2)
"""
# решение на основе матричной записи СЛАУ
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
print(int(*w[0]), int(*w[1]), sep=' ') """