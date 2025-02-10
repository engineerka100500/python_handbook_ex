# A Таблица умножения
n = int(input())
for i in range(n):
    for j in range(n): 
        print((i + 1) * (j + 1), end=' ')
    print()   

# B Не таблица умножения
n = int(input())
for i in range(n):
    for j in range(n): 
        print(f"{j + 1} * {i + 1} = {(i + 1) * (j + 1)}")

# C Новогоднее настроение
n = int(input())
num = 1
cnt = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if cnt < n:
            print(num, end=' ')
            num += 1
            cnt += 1
    print()

# D Суммарная сумма
n = int(input())
sum = 0
for i in range(n):
    numb = int(input())
    while numb > 0:
        sum += numb % 10
        numb //= 10
print(sum)

# F НОД 2.0
n = int(input())
b = 0
for i in range(n):
    a = int(input())
    while b > 0:
        a, b = b, a % b
    b += a
print(b)

# G На старт! Внимание! Марш!
n = int(input())
for cnt_start in range(1, n + 1):
    for i in range(cnt_start + 3 - 1, 0, -1):
        print(f"До старта {i} секунд(ы)")
    print(f"Старт {cnt_start}!!!")

# H Максимальная сумма
n = int(input())
win_name = ''
max_sum = 0
for i in range(n):
    name = input()
    numb = int(input())
    sum = 0 
    while numb:
        sum += numb % 10
        numb //= 10
    if sum >= max_sum:
        win_name = name
        max_sum = sum
print(win_name)

# I Большое число
n = int(input())
res = 0
for i in range(n):
    numb = int(input())
    max = 0 
    while numb > 0:
        if numb % 10 > max:
            max = numb % 10
        numb //= 10
    res = res * 10 + max
print(res)

# J Мы делили апельсин
n = int(input())
print("А Б В")
for a in range(1, n - 1):
    for b in range(1, n - a):
        v = n - a - b
        print(a, b, v)

# K Простая задача 3.0
count = int(input())
cnt = 0 
for i in range(count):
    n = int(input())
    simple = "YES"
    if n - 1:
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                simple = "NO"
                break
    else:
        simple = "NO"
    if simple == "YES":
        cnt += 1
print(cnt)

# L Числовой прямоугольник
n, m = int(input()), int(input())
width = len(str(n * m))
num = 1
for i in range(n):
    for j in range(m):
        print(f"{num:>{width}}", end=' ')
        num += 1    
    print()

# M Числовой прямоугольник 2.0
n, m = int(input()), int(input())
width = len(str(n * m))
num = 1
for i in range(n):
    num = i + 1
    for j in range(m):
        print(f"{num:>{width}}", end=' ')
        num += n    
    print()

# N Числовая змейка
n, m = int(input()), int(input())
width = len(str(n * m))
if n and m: 
    for i in range(n):
        for j in range(m):
            if (i % 2) == 0:
                num = i * m + j + 1
            else:
                num = (i + 1) * m - j
            print(f"{num:>{width}}", end=' ')
        print() 
        
# O Числовая змейка 2.0
n, m = int(input()), int(input())
width = len(str(n * m))
if n and m: 
    for i in range(n):
        for j in range(m):
            if (j % 2) == 0:
                num = j * n + i + 1
            else:
                num = (j + 1) * n - i
            print(f"{num:>{width}}", end=' ')
        print() 