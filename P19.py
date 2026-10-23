# -*- coding: utf-8 -*-
"""P19: Normal com média e desvio configuráveis. Altere os dados no bloco ENTRADAS."""
from math import isnan
from scipy.stats import norm
# ENTRADAS: altere somente estes dados para fazer novos testes.
media = 48.0
desvio = 3.0
consultas = [("entre", 42.0, 49.0), ("acima", 52.0), ("abaixo", 45.0)]

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
validar_real(media, "média")
validar_real(desvio, "desvio-padrão", 0)
if desvio == 0:
    raise ValueError("Para a normal não degenerada, o desvio deve ser positivo.")
for consulta in consultas:
    tipo = consulta[0]
    if tipo == "entre" and len(consulta) == 3:
        a, b = consulta[1:]
    elif tipo == "acima" and len(consulta) == 2:
        a, b = consulta[1], float("inf")
    elif tipo == "abaixo" and len(consulta) == 2:
        a, b = -float("inf"), consulta[1]
    else:
        raise ValueError("Consulta inválida: use entre, acima ou abaixo com os limites adequados.")
    resultado = probabilidade_intervalo(a, b, media, desvio)
    mostrar(str(consulta), resultado)
