# -*- coding: utf-8 -*-
"""P16: Vida útil exponencial. Altere os dados no bloco ENTRADAS."""
from math import exp, expm1
# ENTRADAS: altere somente estes dados para fazer novos testes.
taxa_falha = 0.012  # falhas por hora; deve ser positiva
C = 50.0  # horas
D = 100.0  # horas

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
validar_real(taxa_falha, "taxa de falha", 0)
validar_real(C, "C", 0)
validar_real(D, "D", 0)
if taxa_falha == 0 or C > D:
    raise ValueError("Exige-se taxa > 0 e 0 <= C <= D.")
sobrevive_C = exp(-taxa_falha * C)
sobrevive_D = exp(-taxa_falha * D)
mostrar("Sobreviver até C: P(T>C)", sobrevive_C)
mostrar("Sobreviver até D: P(T>D)", sobrevive_D)
# expm1 melhora a precisão quando D e C são próximos.
entre = sobrevive_C * (-expm1(-taxa_falha * (D - C)))
mostrar("Falhar entre C e D: P(C<T<D)", entre)
mostrar("Sobreviver até D dado que chegou a C", exp(-taxa_falha * (D - C)))
