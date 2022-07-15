# Задача 6. Глубокое копирование

def search_in_value(user_dict, search_word, new_word=None):
    result = False
    if search_word in user_dict.values() and isinstance(user_dict, dict):
        print('Funk!Here!')
        print(user_dict.values())
        result = True
        return result

    for key, value in user_dict.items():
        if isinstance(value, dict):
            if result:
                print('Break here')
                break
            else:
                search_in_value(value, search_word)


#
# def recreate_value(user_list, search_key):
#     if isinstance(user_list)


#   функция ищет искомое значение в значениях ключей словаря
#
# def search_v2(user_dict, user_key):
#     result = False
#     if user_key in user_dict.values() and isinstance(user_dict, dict):
#         print('Funk!Here!')
#         result = True
#         return result
#     for key, value in user_dict.items():
#         if isinstance(value, dict):
#             if result:
#                 break
#             else:
#                 search_v2(value, user_key)
#







site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


search_in_value(site, 'Продать')



