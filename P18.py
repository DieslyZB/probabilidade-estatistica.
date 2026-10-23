# -*- coding: utf-8 -*-
"""P18: Intervalos na normal padrão. Altere os dados no bloco ENTRADAS."""
from math import isnan
from scipy.stats import norm
# ENTRADAS: altere somente estes dados para fazer novos testes.
intervalos = [(0.0, 1.73), (0.81, float("inf")), (-1.25, -0.63)]

from math import isfinite, isclose

def validar_real(valor, nome, minimo=None, maximo=None):
    # Rejeita também NaN e infinito em parâmetros finitos.
    if not isinstance(valor, (int, float)) or isinstance(valor, bool) or not isfinite(valor):
        raise ValueError(f"{nome}: informe um número finito.")
    if minimo is not None and valor < minimo:
        raise ValueError(f"{nome}: mínimo permitido = {minimo}.")
    if maximo is not None and valor > maximo:
        raise ValueError(f"{nome}: máximo permitido = {maximo}.")

def validar_inteiro(valor, nome, minimo=0):
    if not isinstance(valor, int) or isinstance(valor, bool) or valor < minimo:
        raise ValueError(f"{nome}: informe um inteiro >= {minimo}.")

def mostrar(rotulo, probabilidade):
    print(f"{rotulo}: {probabilidade:.10f} = {100 * probabilidade:.8f}%")

# CÁLCULOS E RESULTADOS
def validar_limite(valor):
    # Infinito é permitido como limite; NaN não é.
    if not isinstance(valor, (int, float)) or isinstance(valor, bool) or isnan(valor):
        raise ValueError("Limite deve ser numérico e não pode ser NaN.")

def probabilidade_intervalo(a, b, media, desvio):
    validar_limite(a)
    validar_limite(b)
    if a > b:
        raise ValueError("O limite inferior não pode exceder o superior.")
    if a >= media:
        return norm.sf(a, loc=media, scale=desvio) - norm.sf(b, loc=media, scale=desvio)
    return norm.cdf(b, loc=media, scale=desvio) - norm.cdf(a, loc=media, scale=desvio)
for i, (a, b) in enumerate(intervalos, start=1):
    mostrar(f"Intervalo {i}: {a} a {b}", probabilidade_intervalo(a, b, 0, 1))
