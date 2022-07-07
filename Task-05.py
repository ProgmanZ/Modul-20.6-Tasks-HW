# Задача 5. Ускоряем работу функции

def rec_num(number, user_dict=None):
    if user_dict is None:
        user_dict = dict()
    if number == 1:
        user_dict[number] = number
        return number
    else:
        user_dict[number] = number * rec_num(number - 1, user_dict)
        return user_dict[number]


numb = int(input('Введите число: '))
user_dict = dict()
rec_num(numb, user_dict)
user_dict = {key: (user_dict[key]/key**3)**10 for key in user_dict}
print(user_dict[numb])
print(user_dict)
