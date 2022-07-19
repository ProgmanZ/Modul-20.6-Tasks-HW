# Задача 7. Продвинутая функция sum

def new_sum_func(user_list):
    all_sum = 0
    for element in user_list:
        if isinstance(element, int):
            all_sum += element
        else:
            all_sum += new_sum_func(element)
    return all_sum
