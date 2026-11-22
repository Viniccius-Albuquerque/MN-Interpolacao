def calcular_diferencas_divididas(x, y):
    n = len(x)

    if n != len(y):
        raise ValueError("As listas devem possuir o mesmo tamanho.")

    if n == 0:
        raise ValueError("É necessário informar pelo menos um ponto.")

    coeficientes = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            denominador = x[i] - x[i - j]

            if denominador == 0:
                raise ValueError("Os valores de x devem ser distintos.")

            coeficientes[i] = (
                coeficientes[i] - coeficientes[i - 1]
            ) / denominador

    return coeficientes


def interpolacao_newton(x, y, valor):
    coeficientes = calcular_diferencas_divididas(x, y)

    resultado = coeficientes[-1]

    for i in range(len(coeficientes) - 2, -1, -1):
        resultado = coeficientes[i] + (valor - x[i]) * resultado

    return resultado
