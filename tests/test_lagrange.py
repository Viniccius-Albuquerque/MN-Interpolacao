from metodos.lagrange import interpolacao_lagrange


def testar_lagrange():
    x = [0, 1, 2]
    y = [58.99, 59.40, 63.77]

    valor = 1.5

    resultado = interpolacao_lagrange(x, y, valor)

    esperado = 61.09

    print("Resultado obtido:", repr(resultado))
    print("Resultado esperado:", esperado)

    assert abs(resultado - esperado) < 0.0001

    print("Teste aprovado!")


if __name__ == "__main__":
    testar_lagrange()
