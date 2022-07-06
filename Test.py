def calculating_math_func(data):
    res = list()
    result = 1
    for index in range(1, data + 1):
        result *= index
        res.append(result)

    return res


print(calculating_math_func(10))

'''
1. принять в программе значение предела data
2. передать в функцию data
3. передать в функцию список
3. проверить индекс data в списке, если есть - вернуть
3. если нет - рассчитать все возможные результаты до дата и вернуть результат индекса == data

Числовой ряд: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


'''