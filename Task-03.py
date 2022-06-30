# Задача 3. Ряд Фибоначчи

def fibonacci(itr, buf=0, numb=1, count=-1):
    if count == itr:
        return numb
    else:
        return fibonacci(itr, buf + numb, buf, count + 1)


print('Число:', fibonacci(int(input('Введите позицию числа в ряде Фибоначчи: '))))
