# -*- coding: utf-8 -*-
"""P3: Seleção proporcional de empresas. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
empresas = {"A": 20, "B": 15, "C": 7, "D": 5, "E": 3}
empresa_referencia = "A"

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
if not empresas or empresa_referencia not in empresas:
    raise ValueError("Informe empresas e uma referência existente.")
for nome, quantidade in empresas.items():
    validar_inteiro(quantidade, f"funcionários de {nome}")
total = sum(empresas.values())
if total == 0:
    raise ValueError("O total de funcionários deve ser positivo.")
for nome, quantidade in empresas.items():
    mostrar(f"a) Empresa {nome}", quantidade / total)
mostrar(f"b) Não selecionar {empresa_referencia}", 1 - empresas[empresa_referencia] / total)
