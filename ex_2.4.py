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