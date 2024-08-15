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

# 8.task

# 9.task

# 10.task
