# Задача 9. Ханойские башни


discs = int(input('Введите количество дисков: '))

count = 0

stack_1 = [[i, '', ''] for i in range(1, 2 ** discs)]

even = [i for i in range(1, discs + 1) if i % 4]

not_even = [i for i in range(discs, 0, -1) if i % 4]

for i_count in range(discs + 1):
    for i in range(0, 2 ** (discs - i_count), 2 ** i_count):
        count = -1
        for j in range(1, 3):
            count += 1
            if i % 2:
                stack_1[i][j] = not_even[count]
            else:
                stack_1[i][j] = even[count]

#
print(stack_1)
