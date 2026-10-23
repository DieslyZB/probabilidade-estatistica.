# -*- coding: utf-8 -*-
"""P7: Probabilidade total e Bayes nos pedidos. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
origens = [0.10, 0.15, 0.15, 0.40, 0.20]
taxas = [0.01, 0.02, 0.005, 0.02, 0.08]
cliente_referencia = 5  # A=1, B=2, C=3, D=4, E=5.

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
if not origens or len(origens) != len(taxas):
    raise ValueError("As listas devem ter o mesmo tamanho positivo.")
for p in origens:
    validar_real(p, "proporção de origem", 0, 1)
for taxa in taxas:
    validar_real(taxa, "taxa condicional", 0, 1)
if not isclose(sum(origens), 1.0, rel_tol=0, abs_tol=1e-10):
    raise ValueError("As proporções de origem devem somar 1.")
# Remove apenas eventual diferença de arredondamento tolerada na soma.
soma = sum(origens)
origens = [p / soma for p in origens]
conjuntas = [p * taxa for p, taxa in zip(origens, taxas)]
probabilidade_evento = sum(conjuntas)
mostrar("Probabilidade total do evento", probabilidade_evento)
validar_inteiro(cliente_referencia, "cliente de referência", 1)
if cliente_referencia > len(origens):
    raise ValueError("Cliente inexistente.")
if probabilidade_evento == 0:
    print("Bayes indefinido: a condição erro tem probabilidade zero.")
else:
    mostrar("b) Cliente de referência dado erro", conjuntas[cliente_referencia - 1] / probabilidade_evento)
