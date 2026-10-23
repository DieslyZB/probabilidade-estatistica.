# -*- coding: utf-8 -*-
"""P11: Itens defeituosos: binomial. Altere os dados no bloco ENTRADAS."""
from scipy.stats import binom
# ENTRADAS: altere somente estes dados para fazer novos testes.
tamanho_lote = 20
probabilidade_defeito = 0.05
referencia = 2

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
validar_inteiro(tamanho_lote, "tamanho do lote")
validar_real(probabilidade_defeito, "probabilidade de defeito", 0, 1)
validar_inteiro(referencia, "referência")
if referencia > tamanho_lote:
    raise ValueError("A referência deve estar entre 0 e o tamanho do lote.")
n, p, k = tamanho_lote, probabilidade_defeito, referencia
mostrar("a) Pelo menos um defeituoso", binom.sf(0, n, p))
mostrar(f"b) Exatamente {k} defeituosos", binom.pmf(k, n, p))
mostrar(f"c) Mais de {k} defeituosos", binom.sf(k, n, p))
print(f"d) Esperança de defeituosos: {n * p:.8f}")
print(f"d) Esperança de bons: {n * (1 - p):.8f}")
print(f"e) Variância de defeituosos: {n * p * (1 - p):.8f}")
