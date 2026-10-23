# -*- coding: utf-8 -*-
"""P13: Chegadas: Poisson. Altere os dados no bloco ENTRADAS."""
from scipy.stats import poisson
# ENTRADAS: altere somente estes dados para fazer novos testes.
taxa_por_minuto = 5.0
casos = [(60.0, 2), (30.0, 1)]  # (duração em segundos, chegadas exatas)

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
validar_real(taxa_por_minuto, "taxa por minuto", 0)
for segundos, chegadas in casos:
    validar_real(segundos, "duração em segundos", 0)
    validar_inteiro(chegadas, "chegadas")
    media_intervalo = taxa_por_minuto * segundos / 60
    print(f"Intervalo {segundos:g} s; média = {media_intervalo:g}")
    mostrar(f"Exatamente {chegadas} chegadas", poisson.pmf(chegadas, media_intervalo))
