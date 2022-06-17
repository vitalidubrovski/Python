def input2():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    with open('bd2.md', 'a+', encoding='utf-8') as file:
        file.write('\n '.join([name, surname, phone, description]) + '\n')
