# A
while (word := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# B
cnt = 0 
while (word := input()) != "Приехали!":
    if "зайка" in word:
        cnt = cnt + 1
print(cnt)

# C
begin, end = int(input()), int(input())
for i in range(begin, end + 1, 1):
    print(i, end=' ')

# D
begin, end = int(input()), int(input())
if begin > end:
    for i in range(begin, end - 1, -1):
        print(i, end=' ')
else: 
    for i in range(begin, end + 1, 1):
        print(i, end=' ')

# E
sum = 0
while (number := float(input())) != 0:
    if number >= 500:
        number =  number * 0.9
    sum += number
print(sum)

# F НОД
a, b = int(input()), int(input())
while a != 0 and b != 0:
    if b > a:
        b = b % a
    else:
        a = a % b
print(a + b)

# G НОК
c, d = int(input()), int(input())
a = c
b = d
while a != 0 and b != 0:
    if b > a:
        b = b % a
    else:
        a = a % b
print((c * d) // (a + b))


# H автоматизация повторить строку нужное число раз 
var = input() + '\n'
N = int(input())
print(var * N)

# I Факториал 
a = int(input())
fact = 1
if a == 0:
    print(1)
else:
    for i in range(2, a + 1):
        fact *= i
    print(fact)

# J Маршрут 
x, y = 0, 0
while (direct := input()) != 'СТОП':
    step = int(input())
    match direct:
        case 'СЕВЕР':
            y += step
        case 'ЮГ':
            y -= step
        case 'ЗАПАД':
            x -= step
        case 'ВОСТОК':
            x += step
print(f"{y}\n{x}")

# K
numb = int(input())
sum = 0
while numb > 0:
    sum += numb % 10
    numb //= 10
print(sum)