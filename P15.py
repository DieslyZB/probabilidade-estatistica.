# -*- coding: utf-8 -*-
"""P15: Uniforme contínua. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
A = 0.0
B = 10.0
C = 2.0
D = 6.0

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
for nome, valor in (("A", A), ("B", B), ("C", C), ("D", D)):
    validar_real(valor, nome)
if A >= B or C > D:
    raise ValueError("Exige-se A < B e C <= D.")
media = (A + B) / 2
variancia = (B - A) ** 2 / 12
comprimento = max(0.0, min(B, D) - max(A, C))
print(f"Esperança: {media:.8f}")
print(f"Variância: {variancia:.8f}")
mostrar("P(C < X < D)", comprimento / (B - A))
