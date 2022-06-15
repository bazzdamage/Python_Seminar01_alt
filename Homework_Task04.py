# Написать программу получающую набор произведений чисел от 1 до N.
n = 5


def factorial(n):
    res = [1]
    for i in range(2, n+1):
        res.append(res[i-2]*i)
    return res


print(factorial(n))