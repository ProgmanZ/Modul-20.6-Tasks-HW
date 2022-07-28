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

stack_1 = [[0, '', ''] for i in range(0, deep-1)]
# Общее количество перемещений == 2 ** (общее количество дисков)

even = [i % 4 for i in range(1, deep + 1) if i % 4]
even = two_numbers(even, True)

# генераторы должны вернуть количество строк == 2 ** №диска, по 2 значения

not_even = [i % 4 for i in range(deep, 0, -1) if i % 4]
not_even = two_numbers(not_even)
not_even.insert(0, 1)

# общий список содержит списки из 3-х элементов: [№перемещения, значение из генератора, второе значение из генератора]
# Необходимо продумать связку номера диска - генератор(в зависимости от: четный или не четный номер диска
# Необходимо продумать связку номера диска - номер индекса перемещения

for number_disc in range(0, discs):
    count = 0
    for n_move in range(2 ** number_disc - 1, deep, 2 ** (number_disc+1)): # 0
        stack_1[n_move][0] = number_disc + 1
        for row in range(1, 3):

            if number_disc % 2:
                stack_1[n_move][row] = not_even[count]
            else:
                stack_1[n_move][row] = even[count]

            count += 1

for i in stack_1:
    print(i)

# for i_count in range(0, discs + 1): #1
#     count = 0
#     for i in range(2 * i_count, deep+1, 2 if i_count == 0 or i_count == 1 else 2 ** i_count): # 0
#
#         for j in range(1, 3):
#
#             if i_count % 2:
#                 stack_1[i-1][j] = even[count]
#             else:
#                 stack_1[i-1][j] = not_even[count]
#             count += 1

#
print(stack_1)
