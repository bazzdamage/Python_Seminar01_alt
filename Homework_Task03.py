# Подсчитать сумму цифр в вещественном числе

num = 484.1203


def sum_of_digits_real(real_num: float):
    temp = str(real_num).split('.')
    res = list(temp[0] + temp[1])
    summ = 0
    for item in res:
        summ += int(item)
    return summ


print(sum_of_digits_real(num))
