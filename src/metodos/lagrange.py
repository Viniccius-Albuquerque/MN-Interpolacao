def calcular_polinomio_base_lagrange(x, i, valor):
    n = len(x)
    resultado = 1.0

    for j in range(n):
        if i != j:
            denominador = x[i] - x[j]

            if denominador == 0:
                raise ValueError("Os valores de x devem ser distintos.")

            resultado *= (valor - x[j]) / denominador

    return resultado


def interpolacao_lagrange(x, y, valor):
    n = len(x)

    if n != len(y):
        raise ValueError("As listas devem possuir o mesmo tamanho.")

    if n == 0:
        raise ValueError("É necessário informar pelo menos um ponto.")

    resultado = 0.0

    for i in range(n):
        termo_l = calcular_polinomio_base_lagrange(x, i, valor)
        resultado += y[i] * termo_l

    return resultado
