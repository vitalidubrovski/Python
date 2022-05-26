# Задача 1. Напишите программу, которая принимает на вход
#  число N и выдает набор произведений чисел от 1 до N.
import random
print('Задача 1')
n = int(input('Введите число: \n'))
print()
product = 1
for i in range(1, n+1):
    product *= i
    print(f'{product}')

# Задача 3. Реализуйте алгоритм перемешивания списка.
print('Задача 3')
my_list = ['Tanos', '1234', 'Tony Stark', 'BABA YAGA']
random.shuffle(my_list)
print(my_list)

# Задача 2.Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
print('Задача 2')
n = int(input('Введите число: '))
summ = 0
myList = [(1 + 1 / i)**i for i in range(1, n + 1)]
for j in myList:
    summ += j
print(myList)
print('Сумма:{}'.format(round(summ, 2)))
