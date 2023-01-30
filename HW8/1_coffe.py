""" Задача 1.
На заводе «Кофейный» открывается новое кафе. Изначально есть некоторое количество
кофейных зерен, молока и взбитых сливок.
Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
Бариста готовит наиболее предпочитаемый напиток из доступных.
Для Эспрессо требуется: 1 порция кофейных зерен.
Для Капучино требуется: 1 порция кофейных зерен и 3 порции молока.
Для Маккиато требуется: 2 порции кофейных зерен и 1 порция молока.
Для Кофе по-венски требуется: 1 порция кофейных зерен и 2 порции взбитых сливок.
Для Латте Маккиато требуется: 1 порция кофейных зерен, 2 порции молока и 1 порция взбитых
сливок.
Для Кон Панна требуется: 1 порция кофейных зерен и 1 порция взбитых сливок.
При приготовлении напитка ингредиенты расходуются.
Если недостаточно ингредиентов, то вернуть сообщение: «К сожалению, не можем предложить
Вам напиток»."""


def choose_coffee(*preference):
    global ingredients
    for pref in preference:
        if pref == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return pref
        if pref == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return pref
        if pref == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return pref
        if pref == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return pref
        if pref == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return pref
        if pref == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return pref
    return 'К сожалению, не можем предложить Вам напиток'






# resept = {
#     "Эспрессо": [1, 0, 0],
#     "Капучино": [1, 3, 0],
#     "Маккиато": [2, 1, 0],
#     "Кофе по-венски": [1, 0, 2],
#     "Латте Маккиато": [1, 2, 1],
#     "Кон Панна": [1, 0, 1],
# }


# def choose_coffee(*args):
#     global ingredients
#     for x in args:
#         need = resept[x]
#         if ingredients[0] - need[0] >= 0 and ingredients[1] - need[1] >= 0 and ingredients[2] - need[2] >= 0:
#             ingredients[0] -= need[0]
#             ingredients[1] -= need[1]
#             ingredients[2] -= need[2]
#             return x
#     else:
#         return "К сожалению, не можем предложить Вам напиток"