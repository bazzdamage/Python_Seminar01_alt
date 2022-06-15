# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def sequence_mult3(n):
    if n == 0:
        return 0
    elif n < 0:
        seq = [-1]
        for i in range((n-1)*-1):
            seq.append(seq[i] * -3)
    else:
        seq = [1]
        for i in range(n+1):
            seq.append(seq[i] * -3)
    return seq


print(sequence_mult3(-5))
