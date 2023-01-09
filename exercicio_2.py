# Exercício 2
# Transforme o algoritmo anterior em recursivo.


def counter_even_recursive(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + counter_even_recursive(n - 1)
    else:
        return counter_even_recursive(n - 1)


print(counter_even_recursive(5))
