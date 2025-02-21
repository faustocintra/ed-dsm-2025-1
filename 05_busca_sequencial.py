def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista,
    procurando por val.
    Se val for encontrado, retorna a posição de val na lista.
    Caso contrário, retorna o valor convencional -1.
    """
    # Percorre a lista do início ao fim, usando range() e len()
    # (é necessário ter acesso às posições dos elementos)
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    
    # <-- CUIDADO COM A INDENTAÇÃO AQUI
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1

###############################################################

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# pos30 = busca_sequencial(nums, 30)
# print(f"Elemento 30 encontrado na posição {pos30}.")

# pos_menos3 = busca_sequencial(nums, -3)
# print(f"Elemento -3 encontrado na posição {pos_menos3}.")

# pos4 = busca_sequencial(nums, 4)
# print(f"Elemento 4 encontrado na posição {pos4}.")

vals = [30, -3, 4]

for v in vals:
    pos = busca_sequencial(nums, v)
    if pos >= 0:
        print(f"Elemento {v} encontrado na posição {pos}.")
    else:
        print(f"Elemento {v} não encontrado na lista.")

#############################################################

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

# TESTES COM AS LISTAS DE NOMES
from data.nomes_completos import nomes

buscas = [
    "EDSON PEREIRA",
    "MARIA FERREIRA",
    "VALDIR SILVA",
    "GILCINEIA GARCIA"
]

for b in buscas:
    hora_ini = time()
    pos = busca_sequencial(nomes, b)
    hora_fim = time()
    if pos >= 0:
        print(f"Nome {b} encontrado na posição {pos}.")
    else:
        print(f"Nome {b} não encontrado na lista.")
    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")