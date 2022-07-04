def inputData_stud():
    name = input('Введите имя ученика: ')
    last_name = input('Введите фамилию ученика: ')
    middle_name = input('Введите отчество ученика: ')
    birth_date = input('Введите дату рождения ученика: ')
    phone_number = input('Введите телефон ученика: ')
    with open('school_stud.txt', 'r', encoding='utf-8') as stud_file:
        id = stud_file.readlines()[-1].split(';')[0]

    with open('school_stud.txt', 'a+', encoding='utf-8') as stud_file:
        stud_file.write(
            f'{int(id) + 1}; {last_name} {name} {middle_name}; {birth_date}; {phone_number}\n')


def inputData_parents():
    last_name = input('Введите фамилию родителя: ')
    name = input('Введите имя родителя: ')
    phone_number = input('Введите телефон родителя: ')
    flag = False
    with open('school_stud.txt', 'r', encoding='utf-8') as stud_file:
        finde = stud_file.readlines()

    for i in finde:
        if last_name in i:
            flag = True
            id = i.split(';')[0]
            break
    else:
        print(f'Нет ученика с такой фамилией {last_name}')
    if flag:
        with open('parents.txt', 'a', encoding='utf-8') as parents_file:
            parents_file.write(f'{id}; {last_name} {name}; {phone_number}\n')
