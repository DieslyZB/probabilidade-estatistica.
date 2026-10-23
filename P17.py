# -*- coding: utf-8 -*-
"""P17: Normal do peso bruto. Altere os dados no bloco ENTRADAS."""
from math import hypot
from scipy.stats import norm
# ENTRADAS: altere somente estes dados para fazer novos testes.
media_liquido = 900.0
desvio_liquido = 10.0
media_embalagem = 100.0
desvio_embalagem = 4.0
referencia_superior = 1020.0
limite_inferior = 980.0
limite_superior = 1020.0

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
for m in (media_liquido, media_embalagem, referencia_superior, limite_inferior, limite_superior):
    validar_real(m, "média ou limite")
for d in (desvio_liquido, desvio_embalagem):
    validar_real(d, "desvio-padrão", 0)
if limite_inferior > limite_superior:
    raise ValueError("Limites em ordem incorreta.")
media = media_liquido + media_embalagem
desvio = hypot(desvio_liquido, desvio_embalagem)
print(f"Média: {media:.8f} g; desvio: {desvio:.8f} g")
if desvio == 0:
    # Caso limite: soma constante, e não uma normal não degenerada.
    print("Soma determinística: os dois desvios são zero.")
    acima = float(media > referencia_superior)
    entre = float(limite_inferior < media < limite_superior)
else:
    acima = norm.sf(referencia_superior, loc=media, scale=desvio)
    # Usa a cauda superior no lado direito para evitar subtrair números próximos de 1.
    if limite_inferior >= media:
        entre = norm.sf(limite_inferior, loc=media, scale=desvio) - norm.sf(limite_superior, loc=media, scale=desvio)
    else:
        entre = norm.cdf(limite_superior, loc=media, scale=desvio) - norm.cdf(limite_inferior, loc=media, scale=desvio)
mostrar("a) Peso acima da referência", acima)
mostrar("b) Peso entre os limites", entre)
