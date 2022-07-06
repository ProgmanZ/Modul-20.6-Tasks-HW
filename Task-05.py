# Задача 5. Ускоряем работу функции

def calculating_math_func(data, result=dict):
    if data in result:
        return result[data]
    else:
        result = ()
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


'''
{
1: 1,
2: 2,
3: 6,
4: 7}
'''

