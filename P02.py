# -*- coding: utf-8 -*-
"""P2: População em grupos iguais. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
populacao = 52
grupos = 4
grupo_excluido = 1  # Identificador de 1 a grupos; aqui, 1 representa ouros.

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
validar_inteiro(populacao, "população", 1)
validar_inteiro(grupos, "grupos", 1)
validar_inteiro(grupo_excluido, "grupo excluído", 1)
if grupos > populacao or grupo_excluido > grupos:
    raise ValueError("Quantidade de grupos ou identificador incompatível.")
if populacao % grupos != 0:
    raise ValueError("Não há divisão igual em grupos inteiros; informe tamanhos reais em outro modelo.")
tamanho_grupo = populacao // grupos
probabilidade = (populacao - tamanho_grupo) / populacao
print("Elementos por grupo:", tamanho_grupo)
mostrar("Não pertencer ao grupo escolhido", probabilidade)
