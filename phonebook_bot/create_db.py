import csv
import os.path



db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("Не указано имя!")
        return
    if(surname == ''):
        print("Не указана фамилия!")
        return
    if(number == ''):
        print("Не указан номер!")
        return
    if(email == ''):
        print("Не указано мыло!")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("already exist")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result


