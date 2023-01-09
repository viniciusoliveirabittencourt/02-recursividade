# Exercício 1
# Crie um algoritmo não recursivo para contar quantos números pares
# existem em uma sequência numérica (1 a n)


def count_even(n):
    counter = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            counter += 1

    return counter


print(count_even(12))
