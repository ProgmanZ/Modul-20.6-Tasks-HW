# Задача 8. Список списков 2

def rebuild(user_list):
    tmp_list = list()
    for element in user_list:
        if isinstance(element, list):
            tmp_list.extend(rebuild(element))
        else:
            tmp_list.append(element)
    return tmp_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(rebuild(nice_list))
