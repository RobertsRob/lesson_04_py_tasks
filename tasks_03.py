# 1.task
# Напишите программу, которая выводит таблицу умножения от 1 до 5, используя вложенные циклы.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
    print("----")

# 2.task
# Запросите у пользователя ширину и высоту прямоугольника и выведите прямоугольник из символов *.
width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()

# 3.task
# Запросите у пользователя высоту треугольника и выведите прямоугольный треугольник из символов *.
height = int(input("Введите высоту: "))
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()

# 4.task
# Запросите у пользователя размер доски и выведите "шахматную доску", где X и 0 чередуются.
size = int(input("Введите размер доски: "))
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("0", end="")
    print()

# 5.task
# Запросите у пользователя строку и выведите её символы в обратном порядке, используя цикл for и индексацию.
text = input("Введите строку: ")
for i in range(len(text)-1, -1, -1):
    print(text[i])

# 6.task
# Запросите у пользователя строку и выведите все гласные буквы этой строки (например, 'a', 'e', 'i', 'o', 'u'). Используйте также in.
text = input("Введите строку: ")
vowels = "aeiouAEIOU"
for i in range(len(text)):
    if text[i] in vowels:
        print(text[i])

# 7.task
# Запросите у пользователя строку и создайте новую строку, где каждый символ исходной строки повторяется дважды.
text = input("Введите строку: ")
result = ""
for i in range(len(text)):
    result += text[i] * 2
print(result)

# 8.task
# Запросите у пользователя строку и символ, затем найдите и выведите индекс первого вхождения этого символа в строке.
text = input("Введите строку: ")
char = input("Введите символ для поиска: ")
index = -1
for i in range(len(text)):
    if text[i] == char:
        index = i
        break
print("Индекс первого вхождения:", index)

# 9.task
# Запросите у пользователя строку и проверьте, является ли эта строка палиндромом (читается одинаково с обеих сторон).
text = input("Введите строку: ")
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break
print("Палиндром:", is_palindrome)

# 10.task
# Напишите программу, которая запрашивает у пользователя строку и создает квадратную матрицу, где размер матрицы равен длине строки.
# В этой матрице по диагонали от верхнего левого угла до нижнего правого угла будут размещены символы из строки по одному, а все остальные элементы матрицы будут заполнены пробелами.

text = input("Введите строку: ")
length = len(text)

for i in range(length):
    for j in range(length):
        if i == j:
            print(text[i], end=" ")
        else:
            print(" ", end=" ")
    print()

