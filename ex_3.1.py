# A Азбука
contains = True
for i in range(int(input())):
    str = input()
    if str[0] not in "абв":
        contains = False
print("YES") if contains else print("NO")

# B Кручу-верчу
list_symb = list(input())
for i in range(len(list_symb)):
    print(f"{list_symb[i]}")

# C Анонс новости
L, n = int(input()), int(input())
for i in range(n):
    news = input()
    if len(news) <= L:
        print(f"{news}")
    else:
        print(f"{news[0:L - 3]}...")

# D Очистка данных
while str := input():
    if not str.endswith('@@@'):
        if str.startswith('##'):
            str = str[2:]
        print(str)
# E А роза упала на лапу Азора 4.0
str = input()
print("YES") if str == str[::-1] else print("NO")

# F Зайка — 6
n = int(input())
cnt = 0
for i in range(n):
    word = input()
    cnt += word.count("зайка")
print(f"{cnt}")

# G А и Б сидели на трубе
numb = input().split()
print(int(numb[0]) + int(numb[1]))

# H Зайка — 7
for i in range(int(input())):
    str = input()
    print(str.index("зайка") + 1) if "зайка" in str else print("Заек нет =(")

# L Меню питания
porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(int(input())):
    print(porridge[i % 5])

# I Без комментариев
while (str := input()):
    if not (symb := str.find('#')) + 1:
        print(str)
    elif str[:symb].strip():
        print(str[:symb].rstrip())

# J Частотный анализ на минималках
txt = ''
while (str := input()) != 'ФИНИШ':
    txt += str.lower()
txt = txt.replace(' ', '')

cnt_max_freq_symb = 0
max_freq_symb = ''
for symb in txt:
    cnt_symb = txt.count(symb)
    if cnt_symb > cnt_max_freq_symb:
        cnt_max_freq_symb = cnt_symb
        max_freq_symb = symb   
    elif cnt_symb == cnt_max_freq_symb:
        if symb < max_freq_symb:
            max_freq_symb = symb
print(max_freq_symb.lower())

# K Найдётся всё
title = []
for _ in range(int(input())):
    title.append(input())
query = input()
for word in title:
    if query.lower() in word.lower():
        print(word)

# L Меню питания
porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(int(input())):
    print(porridge[i % 5])

# M Массовое возведение в степень
numbs = []
for i in range(int(input())):
    numbs.append(int(input()))
p = int(input())
for numb in numbs:
    print(numb ** p)

# N Массовое возведение в степень 2.0
numbs = input().split()
p = int(input())
for numb in numbs:
    print(int(numb) ** p, end=' ')

# O НОД 3.0
str = input().split()
numb = []
for digit in str:
    numb.append(int(digit))
a = numb[0]
for b in numb[1:]:
    while b > 0:
        a, b = b, a % b
    b += a
print(b)

# P Анонс новости 2.0 !!!
L, n = int(input()), int(input())
str = [input().strip() for _ in range(n)]
text = '\n'.join(str)

if L == 0:
    pass
else:
    if len(text) - 1 <= L:
        reduced_text = text
        print(reduced_text)
    else:
        if text[L - 3] == '\n':
            print(f"{text[:L + 1 - 3 + 1]}...")
        else:
            reduced_text = text[:L + 1 - 3] + '...' 
            print(reduced_text)

#L, n = int(input()), int(input())
#text = []
#for i in range(n):
#    str = input() + '\n'
#    text.append(str)
#txt = "".join(text)
#reduced_txt = txt[0:L + 1 - 3]
#itog = txt[0:L - reduced_txt.count('\n') - 1]
#itog2 = txt[0:L - reduced_txt.count('\n') - 1 + 3]
#if len(txt) <= L:
#    print(f"{txt}")
#else:
#    if txt[L + 1 - 3 + reduced_txt.count('\n') - 1] == '\n':
#        print(f"{itog2}...")
#    else:
#        print(f"{itog}...")

# Q А роза упала на лапу Азора 5.0
str = input()
str_1 = str.lower().replace(' ', '')
print("YES") if str_1 == str_1[::-1] else print("NO")

# R RLE
str = input()
current_symb = str[0]
current_length = 1
for symb in str[1:]:
    if current_symb == symb:
        current_length += 1
    else:
        print(current_symb, current_length)
        current_symb = symb
        current_length = 1
print(current_symb, current_length)

# S Польский калькулятор
ceil = input().split(' ')
mem = []

for i in range(len(ceil)):
    numb_sign = ceil.pop(0)
    if numb_sign.isdigit():
        mem.append(int(numb_sign))
    else: 
        match numb_sign:
            case '+':
                mem.append(mem.pop() + mem.pop())
            case '-':
                mem.append(mem.pop(-2) - mem.pop())
            case '*':
                mem.append(mem.pop() * mem.pop())
            case '/':
                mem.append(mem.pop(-2) / mem.pop())    
print(mem[-1])

# T Польский калькулятор — 2
ceil = input().split()
stack = []

binary = ['+', '-', '*', '/']
unary = ['~', '!', '#']
ternary = ['@']

for i in range(len(ceil)):
    numb_sign = ceil.pop(0)
    if numb_sign in binary:
        a, b = stack.pop(), stack.pop()
        match numb_sign:
            case '+':
                stack.append(b + a)
            case '-':
                stack.append(b - a)
            case '*':
                stack.append(b * a)
            case '/':
                stack.append(b // a)
    elif numb_sign in unary:
        a = stack.pop()
        match numb_sign:
            case '~':
                stack.append(-a)
            case '!':
                fact = 1
                for i in range(a, 1, -1):
                    fact *= i
                stack.append(fact)
            case '#':
                stack.append(a)
                stack.append(a)
    elif numb_sign in ternary:
        a, b, c = stack.pop(), stack.pop(), stack.pop()
        match numb_sign:
            case '@':
                stack.append(b)
                stack.append(a)
                stack.append(c)
    else:
        stack.append(int(numb_sign))

print(stack[-1])