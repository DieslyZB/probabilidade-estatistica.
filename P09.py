# -*- coding: utf-8 -*-
"""P9: Confiabilidade dos dois sistemas. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
configuracao = 2  # 1 = figura esquerda; 2 = figura direita.
p1 = 0.01  # superior esquerdo
p2 = 0.02  # superior direito
p3 = 0.03  # inferior esquerdo
p4 = 0.04  # inferior direito

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
if configuracao not in (1, 2):
    raise ValueError("Escolha configuração 1 ou 2.")
for i, p in enumerate((p1, p2, p3, p4), start=1):
    validar_real(p, f"p{i}", 0, 1)
if configuracao == 1:
    ramo_superior = p1 * p2
    ramo_inferior = p3 * p4
    resultado = 1 - (1 - ramo_superior) * (1 - ramo_inferior)
else:
    primeiro_bloco = 1 - (1 - p1) * (1 - p3)
    segundo_bloco = 1 - (1 - p2) * (1 - p4)
    resultado = primeiro_bloco * segundo_bloco
mostrar(f"Funcionamento, configuração {configuracao}", resultado)
