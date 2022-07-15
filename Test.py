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
result = str(site.values()).strip('"\' :',).split(' ')
find_word = 'iPhone'
new_word = 'Samsung'
new_result = list()
print('Before:', result)
if find_word in result:
    for word in result:
        if word == find_word:
            new_result.append(new_word)
            print('*** Replaced..(', word, ').')
        else:
            new_result.append(word)
            print(word)
    print('After:', new_result)
else:
    print('Word not found in String')



# dict_values([{'head': {'title': 'Куплю/продам iPhone недорого'}, 'body': {'h2': 'У нас самая низкая цена на iPhone', 'div': 'Купить', 'p': 'Продать'}}])