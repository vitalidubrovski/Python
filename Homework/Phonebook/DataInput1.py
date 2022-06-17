def input1():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    with open('bd1.txt', 'a+', encoding='utf-8') as file:
        file.write(', '.join([name, surname, phone, description]) + '\n')
