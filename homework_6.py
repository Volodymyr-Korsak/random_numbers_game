import random
import argparse


all_games = 0  # счетчик всех сыграных игр
win_games = 0  # счетчик побед в игре
key_for_exit = "exit"  # слово для выхода с програмы
rand_num_range_from = rand_num_range_to = 0


def random_numbers():
    """Функцыя вывода рандомного числа
    с возможностю менять дипазон чисес с помощю
    аргументов при запуске скрипта"""

    global rand_num_range_from,rand_num_range_to
    parser = argparse.ArgumentParser(description='Параметрами можно указывать диапазон случайных чисел для угадывания')
    parser.add_argument("-f", default=1, type=int, help="аргумент 'f' начальное число")
    parser.add_argument("-t", default=6, type=int, help="аргумент 't' конечное число")
    args = parser.parse_args()
    rand_num_range_from = args.f
    rand_num_range_to = args.t
    return random.randint(args.f, args.t)



def chek_numbers(num_user, num_pas):
    '''Функция проверки числа на - угаданое
        :win_games - чисел угаданое
        :all_games - чисел введено загаданом диапазоне'''

    num_user = int(num_user)
    if num_user == num_pas:
        print("\nВуаля, УГАДАЛ!!!")




def chek_eror(num_user):
    '''Функция проверяет правильность ввода пользоватилемпроверки  числа на:
               - введен ли в строку ввода число а не дргие символы
               - введено ли число в диапазоне от 1 до 6
    на выходе функцыя возвращает:
                   True  - есть ошибка ввода
                   False - ошыбок нет'''

    try:
        num_user = int(num_user)

    except ValueError:
        print("\nневерно!".upper())
        print("Вы ввели не числовое значение")
        print(f"Для вихода введите :{key_for_exit}")
        print("\nЧтобы попробовать снова")
        return True
    else:
        if num_user < rand_num_range_from or num_user > rand_num_range_to:
            print(f'Ваше число : {num_user} вне диапазона от '
                  f'{rand_num_range_from} до {rand_num_range_to}')
            return True
        elif num_pas > num_user and num_user > rand_num_range_from:
            print(f"Число меньше загаданого! =( ,загадоное чисто : {num_pas}")
            return True
        elif num_pas < num_user and num_user < rand_num_range_to + 1:
            print(f"Число больше загаданого! =( ,загадоное чисто : {num_pas}")
            return True


print("Поиграем в угадайку!!!")
while True:
    num_pas = random_numbers()
    num_user = input(f"Введите число от {rand_num_range_from} до {rand_num_range_to}: ")
    if num_user.lower() == key_for_exit:
        print(f",\nИгр сыграно - {all_games}\n"
              f"Чисел угодано - {win_games}\n"
              f"!!!!!!GAME OWER!!!!!!")
        break
    if chek_eror(num_user):
        all_games += 1
        continue
    chek_numbers(num_user, num_pas)
    win_games += 1
    print(f"\nДля вихода введите :{key_for_exit}")
    print("чтобы попробовать снова")