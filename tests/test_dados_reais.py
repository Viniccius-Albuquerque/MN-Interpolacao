from metodos.newton import interpolacao_newton
from metodos.lagrange import interpolacao_lagrange

dados = {
    "SRV-01": {
        15.5: ([14, 15, 16], [49.75, 48.79, 49.97]),
        18.5: ([17, 18, 19], [51.28, 48.65, 48.65]),
        21.5: ([20, 21, 22], [51.37, 50.15, 48.30])
    },

    "SRV-02": {
        15.5: ([14, 15, 16], [54.77, 56.27, 58.12]),
        18.5: ([17, 18, 19], [58.54, 60.16, 62.66]),
        21.5: ([20, 21, 22], [66.74, 74.48, 75.37])
    },

    "SRV-03": {
        15.5: ([14, 15, 16], [58.99, 59.40, 63.77]),
        18.5: ([17, 18, 19], [71.24, 79.48, 79.81]),
        21.5: ([20, 21, 22], [71.37, 63.92, 59.21])
    }
}

for servidor, incidentes in dados.items():

    print("\n", servidor)

    for horario, pontos in incidentes.items():

        x, y = pontos

        temp_newton = interpolacao_newton(x, y, horario)
        temp_lagrange = interpolacao_lagrange(x, y, horario)

        print(
            f"Horário: {int(horario)}h30 | "
            f"Newton: {temp_newton:.5f} °C | "
            f"Lagrange: {temp_lagrange:.5f} °C | "
            f"Dif: {abs(temp_newton - temp_lagrange):.2e}"
        )
