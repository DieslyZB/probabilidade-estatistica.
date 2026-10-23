# -*- coding: utf-8 -*-
"""P4: Amostragem sem reposição. Altere os dados no bloco ENTRADAS."""
from math import comb
# ENTRADAS: altere somente estes dados para fazer novos testes.
grupo_alvo = 30
demais_estudantes = 10
quantidades_selecionadas = [2, 4]

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
validar_inteiro(grupo_alvo, "grupo alvo")
validar_inteiro(demais_estudantes, "demais estudantes")
total = grupo_alvo + demais_estudantes
if total == 0:
    raise ValueError("A população deve ser positiva.")
for n in quantidades_selecionadas:
    validar_inteiro(n, "selecionados")
    if n > total:
        raise ValueError("A amostra não pode exceder a população.")
    probabilidade = comb(grupo_alvo, n) / comb(total, n) if n <= grupo_alvo else 0.0
    mostrar(f"Todos do grupo, n={n}", probabilidade)
