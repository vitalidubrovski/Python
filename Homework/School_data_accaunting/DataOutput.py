
def output():
    with open('school_stud.txt', 'r', encoding='utf-8') as stud_file:
        for i in stud_file:
            line = i.split(';')
            id = line[0]
            lastname = line[1].split()[0]
            name = line[1].split()[1]
            middle_name = line[1].split()[2]
            birth_date = line[-2]
            phone_number = line[-1]
            print(
                f'Запись {id}:\n ФИО: {lastname} {name} {middle_name}\n Дата рождения: {birth_date}\n Телефон: {phone_number}')

    with open('parents.txt', 'r', encoding='utf-8') as stud_file:
        for i in stud_file:
            line = i.split(';')
            id = line[0]
            lastname = line[1].split()[0]
            name = line[1].split()[1]
            phone_number = line[-1]
            print(
                f'Запись с ID {id}(Родитель):\n ФИО: {lastname} {name}\n Телефон: {phone_number}')
