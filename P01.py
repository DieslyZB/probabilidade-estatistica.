# -*- coding: utf-8 -*-
"""P1: Operações entre conjuntos. Altere os dados no bloco ENTRADAS."""

# ENTRADAS: altere somente estes dados para fazer novos testes.
U = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {3, 4}
C = {2, 5}


# CÁLCULOS E RESULTADOS
if not all(isinstance(s, set) for s in (U, A, B, C)):
    raise ValueError("U, A, B e C devem ser conjuntos Python (set).")
if not (A <= U and B <= U and C <= U):
    raise ValueError("A, B e C devem estar contidos em U.")
# Ordenar as representações permite mostrar inclusive tipos diferentes.
def exibir(conjunto):
    return "{" + ", ".join(sorted(map(repr, conjunto))) + "}"
print("A união B =", exibir(A | B))
print("A interseção B =", exibir(A & B))
print("A interseção C =", exibir(A & C))
print("Complemento de A =", exibir(U - A))
