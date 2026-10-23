# -*- coding: utf-8 -*-
"""P5: Pelo menos uma pessoa resolver. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
probabilidades = [0.5, 0.7]

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
if not probabilidades:
    raise ValueError("Informe pelo menos uma pessoa.")
ninguem_resolve = 1.0
for i, p in enumerate(probabilidades, start=1):
    validar_real(p, f"probabilidade da pessoa {i}", 0, 1)
    ninguem_resolve *= 1 - p
mostrar("Pelo menos uma pessoa resolve", 1 - ninguem_resolve)
