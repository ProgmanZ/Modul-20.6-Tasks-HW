# Задача 4. Поиск элемента 2

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_v2(user_dict, user_key, deep=-1):

    if user_key in user_dict:
        return user_dict[user_key]

    for key in user_dict.values():
        if isinstance(key, dict) and deep != 0:
            result = search_v2(key, user_key, deep - 1)
            if result:
                break
    else:
        result = None
    return result


search_key = input('Введите искомый ключ: ')
search_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if search_deep == 'y':
    user_deep = int(input('Введите глубину: '))
    print('Значение ключа:', search_v2(site, search_key, user_deep + 1))
else:
    print('Значение ключа:', search_v2(site, search_key))
