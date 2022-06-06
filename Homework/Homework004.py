# Задача 1. Ввычислить число пи,  c заданной точностью d
# (использовать Ряд Нилаканта или любой другой вариант расчета числа Пи)
import random
from decimal import Decimal, getcontext
print('Задача 1 \n')


def Pi(n):
    pi = 0
    i = 0
    while i < n:
        pi += (1/(16**i)) * (4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))
        i += 1
    return pi
d=20
print('Пи с заданной точностью: {}'.format(round(Pi(d), d)))
getcontext().prec=5
print('Пи с заданной точностью: ', Decimal(Pi(d)) * Decimal(1), '\n')

# Задача 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
print('Задача 2')


def SimpleMultiplier(n):
    divizor=2
    result=[]
    while divizor * divizor <= n:
        if n % divizor == 0:
            result.append(divizor)
            n //= divizor
        else:
            divizor += 1
    if n > 1:
        result.append(n)
    return result


print(SimpleMultiplier(int(input('Введите натуральное чило: '))), '\n')

# Задача 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
print('Задача 3')


numbers=list(map(int, input('Введите последовательность чисел: ').split()))
print(f'{numbers}')

# n = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9]
# print(n)


def NonRecurring(n):
    unique=[]
    size=len(n)
    flag=bool
    for i in range(size):
        flag=True
        for j in range(size):
            if n[i] == n[j] and i != j:
                flag=False
                break
        if flag == True:
            unique.append(n[i])

    return unique


print(NonRecurring(numbers), "\n")

# Задача 4. Задана натуральная степень n. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени
# пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0
print('Задача 4')

def GetPolynomial(n):
    num_lst=[str(random.randint(0, 100)) for i in range(n + 1)]
    result=''
    for i in range(0, n + 1):
        if i == n:
            result += num_lst[i] + ' = 0'
        elif i == n-1:
            result += num_lst[i] + 'x + '
        elif i < n-1:
            result += num_lst[i] + 'x^' + str(n - i) + ' + '
    return result

degree_1=int(input('Введите степень первого полинома: '))
degree_2=int(input('Введите степень второго полинома: '))

# with open('Polynominal_1.txt', 'w+') as data_1:
#     data_1.write((GetPolynomial(degree_1)))

# with open('Polynominal_2.txt', 'w+') as data_2:
#     data_2.write((GetPolynomial(degree_2)))
print(GetPolynomial(degree_1))
print(GetPolynomial(degree_2))
# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#  (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)
