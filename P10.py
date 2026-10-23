# -*- coding: utf-8 -*-
"""P10: Média e desvio do peso bruto. Altere os dados no bloco ENTRADAS."""
from math import sqrt
# ENTRADAS: altere somente estes dados para fazer novos testes.
medias = [900.0, 100.0]
desvios = [10.0, 4.0]

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
if not medias or len(medias) != len(desvios):
    raise ValueError("Informe uma média e um desvio por peso.")
for m in medias:
    validar_real(m, "média")
for d in desvios:
    validar_real(d, "desvio-padrão", 0)
media_total = sum(medias)
variancia_total = sum(d ** 2 for d in desvios)
print(f"Média do peso bruto: {media_total:.8f} g")
print(f"Variância: {variancia_total:.8f} g²")
print(f"Desvio-padrão: {sqrt(variancia_total):.8f} g")
