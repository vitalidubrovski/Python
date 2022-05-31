# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
print('Задача 1 \n')
collection = [random.randint(1, 11) for i in range(1, 7)]
print(collection)


def SummOfOddsElements(arr):
    summ = 0
    for i in range(0, len(arr), 2):
        summ += arr[i]
    return summ


print('Сумма нечетных позиций: {}'.format(SummOfOddsElements(collection)))
print(sum(x for i, x in enumerate(collection) if i % 2 == 0), '\n')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
print('Задача 2 \n')
print(collection)


def ProductOfTwo(coll):
    size = len(coll)
    result = []
    left = 0
    while left < size / 2:
        right = (left + 1) * -1
        result.append(coll[left] * coll[right])
        left += 1
    return result


print('Произведение пар: {}'.format(ProductOfTwo(collection)))

# Задача 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное
print("Задача 4 \n")

number = int(input("Введите число: "))
count = ''
while number > 0:
    count = str(number % 2) + count
    number //= 2
print('Получите двоичное: {}'.format(count), '\n')

# Задача 3.Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
print('Задача 3')
my_list = [round(random.random(), 5) for i in range(1, 6)]
print(my_list)
print('Разница между макс и мин:', round(max(my_list) - min(my_list), 5), '\n')

# Задача 5.Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
print('Задача 5 \n')

N = int(input('Введите число: '))


def Fib(n: int) -> list:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    list1 = Fib(n-1)
    list1.append(list1[-1] + list1[-2])
    return list1


fib = Fib(N)
result = [i*-1 for i in fib[::-1]] + [0] + fib
for i in range(len(result) - N):
    if i % 2 != 0:
        result[i] *= -1
print(result, end='')
