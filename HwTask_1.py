# 1. Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.

# Пример:

# 6 -> да
# 7 -> да
# 1 -> нет


week = 7
day = int(input(f'Введите день недели цифрой: '))

while True:
    if day == 0 or day > week:
        day = int(
            input(f'Вы ввели {day} - это не день недели, повторите ввод: '))
    if day < 0:
        day *= -1
    else:
        if day == week - 1 or day == week:
            print(f'{day} -> да, этот день является выходным')
            break
        else:
            print(f'{day} -> нет, этот день НЕ является выходным')
            break
