from DataInput import inputData_stud, inputData_parents
from DataOutput import output

print('Что сделать с данными? Ввод\Вывод')
select = str(input())
if select == 'Ввод':
    print('В какую таблицу занести данные? Ученик\Родители')
    about = str(input())
    if about == 'Ученик':
        inputData_stud()
    elif about == 'Родители':
        inputData_parents()
    else:
        print('Не корректно!Попробуйте еще раз')
elif select == 'Вывод':
    output()
else:
    print('Не корректно! Попробуйте еще раз')
