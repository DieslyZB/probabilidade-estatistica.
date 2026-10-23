# -*- coding: utf-8 -*-
"""P12: Mulheres sorteadas: hipergeométrica. Altere os dados no bloco ENTRADAS."""
from math import comb
# ENTRADAS: altere somente estes dados para fazer novos testes.
mulheres = 60
homens = 40
sorteados = 2
mulheres_desejadas = 1

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
validar_inteiro(mulheres, "mulheres")
validar_inteiro(homens, "homens")
validar_inteiro(sorteados, "sorteados")
validar_inteiro(mulheres_desejadas, "mulheres desejadas")
total = mulheres + homens
if total == 0 or sorteados > total:
    raise ValueError("População vazia ou amostra maior que a população.")
k, n = mulheres_desejadas, sorteados
# Evento fora do suporte é impossível, mas a amostra ainda pode ser válida.
if k > n or k > mulheres or n - k > homens:
    probabilidade = 0.0
else:
    probabilidade = comb(mulheres, k) * comb(homens, n - k) / comb(total, n)
mostrar("Exatamente a quantidade desejada de mulheres", probabilidade)
