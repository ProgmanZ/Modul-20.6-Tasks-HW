# Задача 9. Ханойские башни

def two_numbers(user_list, user_flag=False):
    tmp_list = list()
    for element_user_list in user_list:
        for _ in range(2):
            tmp_list.append(element_user_list)
    if user_flag:
        tmp_list.remove(tmp_list[0])
    return tmp_list


discs = int(input('Введите количество дисков: '))

deep = 2 ** discs
count = 0

stack = [[0, '', ''] for i in range(0, deep-1)]


even = [i % 4 for i in range(1, deep + 1) if i % 4]
even = two_numbers(even, True)

not_even = [i % 4 for i in range(deep, 0, -1) if i % 4]
not_even = two_numbers(not_even)
not_even.insert(0, 1)


for number_disc in range(0, discs):
    count = 0

    for n_move in range(2 ** number_disc - 1, deep, 2 ** (number_disc+1)): # 0
        stack[n_move][0] = number_disc + 1

        for row in range(1, 3):
            if number_disc % 2:
                stack[n_move][row] = not_even[count]
            else:
                stack[n_move][row] = even[count]
            count += 1

for line in stack:
    print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(line[0], line[1], line[2]))

