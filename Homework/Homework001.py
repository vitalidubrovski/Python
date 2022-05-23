# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
import random
from cmath import sqrt
print('Задача 1')
day = int(input('Введите число от 1 до 7 \n'))
if day in range(6, 7):
    print(f'Выходной')
else:
    if day in range(1, 5):
        print(f'Рабочий \n')
    else:
        print(f'Не верное значение, попробуй еще раз \n')

# Задача 2.Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
print('Задача 2')
x = 100
y = 100
if x == 0 or y == 0:
    print(f'В условии !=0 \n')
else:
    if x > 0 and y > 0:
        print(f'1 четверть \n')
    else:
        if x < 0 and y > 0:
            print(f'2 четверть \n')
        else:
            if x < 0 and y < 0:
                print(f'3 четверть \n')
            else:
                if x > 0 and y < 0:
                    print(f'4 четверть \n')


# Задача 3.Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
print(f'Задача 3')
quarter = int(input('Введите номер четверти \n'))
if quarter == 1:
    print(f'От x > 0 > y до бесконечности \n')
else:
    if quarter == 2:
        print(f'От x < 0 > y до бесконечности \n')
    else:
        if quarter == 3:
            print(f'От x < 0 < y до бесконечности \n')
        else:
            if quarter == 4:
                print(f'От x > 0 < y до бесконечности \n')
            else:
                print(f'Ввели не верное значение, попробуйте еще раз \n')

# Задача 4. Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
print('Задача 4')
a_x = random.randint(1, 11)
a_y = random.randint(1, 11)
b_x = random.randint(1, 11)
b_y = random.randint(1, 11)
print(
    f'Точка А с координатами ({a_x},{a_y})\n Точка B с координатами ({b_x},{b_y})')
result = sqrt((a_x - b_x)**2 + (a_y - b_y)**2)
result = complex(round(result.real, 2), round(result.imag))
print('Расстояние: {}'.format(result), end='\n')

# Задача 5. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Задача 5')
x = True
y = False
z = True
if not(x or y or z) == (not(x) and not(y) and not(z)):
    print(True)
else: print(False)