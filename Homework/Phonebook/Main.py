import DataInput1 as data_1
import DataInput2 as data_2

print('Каким способом записать контакты? Список/Столбец')
dt1 = str(input())
if dt1 == 'Список':
    data_1.input1()
elif dt1 == 'Столбец':
    data_2.input2()
else:
    print('Некорректный ввод, попробуйте еще раз!')
