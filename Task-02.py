# Задача 2. Свой zip 2

def my_zip(elem_a, elem_b):
    scope = min(len(elem_a), len(elem_b))
    elem_a = list(elem_a)
    elem_b = list(elem_b)
    return [(elem_a[i], elem_b[i]) for i in range(scope)]
