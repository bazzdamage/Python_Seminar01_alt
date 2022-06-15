# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
initial = 'Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.'
contain = 'ст'


def string_contain(initial: str, contain: str):
    count = initial.count(contain)
    return count


print(string_contain(initial, contain))
