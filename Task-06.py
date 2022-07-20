# Задача 6. Глубокое копирование
import copy


def check_values(dict_user):

    for i_value in dict_user.values():
        if not isinstance(i_value, str):
            return False
    return True


def search_in_value(user_dict, new_brand, search_brand_name='brand'):

    if isinstance(user_dict, dict) and check_values(user_dict):
        for key, value in user_dict.items():

            if search_brand_name in value:
                temp_line = user_dict[key]
                user_dict[key] = temp_line.replace(search_brand_name, new_brand)

    for key, value in user_dict.items():
        if isinstance(value, dict):
            search_in_value(value, new_brand)

site={
    'html': {
        'head': {
            'title': 'Куплю/продам brand недорого brand'
        },
        'body': {
            'h2': 'У нас самая низкая цена на brand',
            'div': 'Купить',
            'p': 'Продать brand'
        }
    }
}

brand_list = list()
for _ in range(int(input('Сколько сайтов: '))):
    brand_list.append(input('Введите название продукта для нового сайта: '))
    for brand in brand_list:
        tmp_site = copy.deepcopy(site)
        search_in_value(tmp_site, brand)
        print(tmp_site)


