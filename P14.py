# -*- coding: utf-8 -*-
"""P14: Bits com erro. Altere os dados no bloco ENTRADAS."""
from scipy.stats import binom, poisson
# ENTRADAS: altere somente estes dados para fazer novos testes.
numero_bits = 10000
probabilidade_erro = 0.0002
limite_erros = 4

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
validar_inteiro(numero_bits, "número de bits")
validar_real(probabilidade_erro, "probabilidade de erro", 0, 1)
validar_inteiro(limite_erros, "limite de erros")
if limite_erros > numero_bits:
    raise ValueError("Limite deve estar entre 0 e o número de bits.")
exata = binom.sf(limite_erros, numero_bits, probabilidade_erro)
media = numero_bits * probabilidade_erro
aproximada = poisson.sf(limite_erros, media)
mostrar("Binomial exata: mais que o limite", exata)
print(f"Média para Poisson: {media:.8f}")
mostrar("Poisson: aproximação, avaliar adequação", aproximada)
print(f"Diferença absoluta: {abs(exata - aproximada):.10f}")
