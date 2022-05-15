conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
# unindo dois conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
# itens em comum em dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
# itens diferentes em dois conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)
conjunto_diferenca = conjunto2.difference(conjunto)
print(conjunto_diferenca)

# Direfenca simetrica, oque nao tem nos dois conjuntos
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferenca simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_b)
print(conjunto_superset)

#Transformando uma lista em um conjunto, assim removendo a duplucidade
lista = ['cachorro', 'gato', 'gato']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
#Retornando o conjunto para lista agora sem duplicidade
lista = list(conjunto_animais)
print(lista)

# conjunto = {1 , 2 ,3 , 4}
# print(type(conjunto))
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)