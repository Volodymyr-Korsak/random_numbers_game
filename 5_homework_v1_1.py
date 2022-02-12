import random

pop = 1  # счетчик неверных вводов
all_games = 0  # счетчик всех сыграных игр
win_games = 0  # счетчик побед в игре
key_for_exit = "exit"  # слово для выхода с програмы


def chek_numbers(num_user, num_pas):
    '''Функция проверки числа на - угаданое
        :win_games - чисел угаданое
        :all_games - чисел введено от {1} до {6}
        :pop - ошибочних вводов'''

    global win_games,pop,all_games
    if num_user == num_pas:
        print("\nВуаля, УГАДАЛ!!!")
        win_games += 1
    else:
        print(f'Ваше число : {num_user} вне диапазона от 1 до 6')
        pop += 1
        all_games += 1


def chek_eror():
    '''Функция проверяет правильность ввода пользоватилемпроверки  числа на:
               - введен ли в строку ввода число а не дргие символы
               - введено ли число в диапазоне от 1 до 6
    на выходе функцыя возвращает:
                   True  - есть ошибка ввода
                   False - ошыбок нет'''
    global pop, num_user,all_games
    try:
        num_user = int(num_user)

    except ValueError:
        print("\nневерно!".upper())
        print(f"Количество неверных вводов - {pop}\n")
        print(f"Для вихода введите :{key_for_exit}")
        print("чтобы попробовать снова")
        pop += 1
        return True


print("Поиграем в угадайку!!!")
while True:
    num_user = input("Введите число от 1 до 6: ")
    if num_user.lower() == key_for_exit:
        print(f",\nИгр сыграно - {all_games}\n"
              f"Чисел угодано - {win_games}\n"
              f"неверных вводов  - {pop}\n!!! GAME OWER !!!")
        break
    if chek_eror():
        continue
    num_pas = random.randint(1, 6)
    chek_numbers(num_user, num_pas)
    print(f"\nДля вихода введите :{key_for_exit}")
    print("чтобы попробовать снова")