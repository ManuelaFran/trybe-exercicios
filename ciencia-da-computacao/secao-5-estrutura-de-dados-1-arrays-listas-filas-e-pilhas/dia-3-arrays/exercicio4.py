# Você têm dois arrays de números inteiros que representam:
# I - instantes de entrada e saídas em uma biblioteca
# II - um número que represente um instante a ser buscado
# Retorne quantas pessoas estudantes estão na biblioteca naquele instante.
# Considere que todo estudante entrou e saiu da biblioteca.
"""
entradas = [1, 2, 3]
saidas = [3, 2, 7]
instante_buscado = 4
resultado: 1

O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
e saiu no 2 e o último foi único a estar presente no instante 4.
"""


def students_in_instant(arrivals, departures, time_instant):
    return sum(
        arrival <= time_instant <= departure
        for arrival, departure in zip(arrivals, departures)
    )


# Faça a análise de complexidade da sua solução.
"""O algoritmo realiza um for, portanto possui Complexidade de Tempo O(n)"""