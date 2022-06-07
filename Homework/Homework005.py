# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
from functools import reduce
print('Задача 1')
text = 'АБВГДейка, АБВГДейка —  Это учёба и игра, АБВГДейка, АБВГДейка, Азбуку детям знать пора.'
a = text.lower().split()


def delete_char(some_text):
    return ' '.join(filter(lambda x: x.lower().find('абв') == -1, some_text))


print(delete_char(a), '\n')

# Задача 3. Крестики-нолики.

# -*- coding: utf-8 -*-

print('X_O Задача 3')
board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def take_input(x_or_o):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + x_or_o+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Вы уверены, что ввели число? Введите число от 1 до 9!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = x_or_o
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Введите число от 1 до 9 чтобы походить.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_coord:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных.
print('\n Задача 4')


def main():
    rle = "11111 22222 WWWWW BBB 3333333 5555 66666 777 xxxxx sssss"
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Исходные данные: " + rle)

    print("Сжатие: " + formatOutput(encoded))

    print("Восстановление: " + decoded)


def encode(sequence):
    count = 1
    result = []

    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(sequence):

    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def formatOutput(sequence):

    result = []

    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)


if __name__ == "__main__":
    main()
