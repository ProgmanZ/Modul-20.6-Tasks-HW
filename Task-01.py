# Задача 1. Challenge 2.

def number(num_end, num_start=1):
    print(num_start)
    if num_end != num_start:
        number(num_end, num_start + 1)


user_enter = int(input('Введите num: '))
number(user_enter)
