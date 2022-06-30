# Задача 3. Ряд Фибоначчи

def fibo_func(number_iter, first_numb=0, second_numb=1):
    result = [1]
    while len(result) != number_iter:
        result.append(first_numb + second_numb)
        first_numb += second_numb
        result.append(first_numb)
        second_numb += first_numb
    return result


print(fibo_func(8))

# 1, 1, 2, 3, 5, 8, 13

#  first: 0, 1, 2, 3, 5
# second: 1, 2, 3, 5, 8

