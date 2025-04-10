# A Символическая выжимка

print("".join(set(input())))

# B Символическая разница

line1, line2 = input(), input()
chars1, chars2 = set(line1), set(line2)
print("".join(chars1 & chars2))

# C Зайка — 8

descriptions = []
for _ in range(int(input())):
    descriptions.extend(input().split())

print("\n".join(set(descriptions)))

# D Кашееды

N, L = int(input()), int(input())
porridge1 = []
porridge2 = []
for _ in range(N):
    porridge1.extend(input().split())
for _ in range(L):
    porridge2.extend(input().split())

if len(common := (set(porridge1) & set(porridge2))) != 0:
    print(len(common))
else:
    print("Таких нет") 

# E Кашееды — 2

N, M = int(input()), int(input())
porridge1 = []
for _ in range(N + M):
    porridge1.append(input())

people_porridge1 = len(set(porridge1)) - (len(porridge1) - len(set(porridge1)))

if people_porridge1 == 0:
    print("Таких нет")
else:
    print(people_porridge1)

# F Кашееды — 3

# что сделать? как сделать? 
# список - set = дубли фамилий 
# set - дубли 
# вывести список любителей одной каши -- пройти по элементам в цикле
# отсортировать по алфавиту .sort()

# если размер списка и множества совпадает = все любят одну кашу
# --> вывести весь список, отсортировав
# удалить все элементы множества из списка = остались  дубли 
# удалить из сета список дублей = разность множеств 
# преобразовать к списку и отсортировать, т.к. вывести нужно в алф порядке 

N, M = int(input()), int(input())
porridge1 = []
for _ in range(N + M):
    porridge1.append(input())

people_porridge1 = len(set(porridge1)) - (len(porridge1) - len(set(porridge1)))

if people_porridge1:
    porridge1 = sorted(porridge1)
    p2 = porridge1.copy()
    if len(set(porridge1)) == len(porridge1):
        print("\n".join(porridge1))
    else:
        for man in set(porridge1):
            porridge1.remove(man)
        print("\n".join(sorted(list(set(p2) - set(porridge1)))))
else:
    print("Таких нет")

# G Азбука Морзе

txt = input().upper().split()

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

for word in txt:
    word = ' '.join(map(morse_code.get, word))
    print(''.join(word))

# H Кашееды — 4

porridges = dict()

for _ in range(int(input())):
    surname, *porridge = input().split()
    porridges[surname] = porridge
query = input()
spisok = []

for surname in porridges:
    if query in porridges[surname]:
        spisok.append(surname)
if not spisok:
    print('Таких нет')
else:
    for i in range(len(spisok)):
        print(sorted(spisok)[i])

# I Зайка — 9

# метод get()
# принять строки-местности, до пустой строки 
# -- цикл while через морж
# разбить на слова -- split
# Если слово есть среди ключей, то get() возвращает список, 
# хранящийся по этому ключу, иначе get() возвращает пустой список. 
# добавить в список значение на 1 больше - инкремент.
obj = dict()

while (area := input()) != '':
    words = area.split()
    for element in words:
        obj[element] = obj.get(element, 0) + 1

for element in obj:
    print(element, obj[element])

# J Транслитерация

transliterate = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 
    'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'
}

trans_txt = ''

for char in input():
    char_copy = char.upper()
    if char_copy in transliterate:
        if char.isupper():
            char = transliterate[char_copy].capitalize()
        else:
            char = transliterate[char_copy].lower()
    trans_txt += char

print(trans_txt)