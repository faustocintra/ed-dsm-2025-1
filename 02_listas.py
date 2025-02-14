"""
LISTA é uma estrutura de dados nativa da linguagem Python.
Ela permite que vários valores sejam associados a uma
única variável.
"""

# Lista de strings
frutas = ["maçã", "morango", "laranja", "uva", "manga", "goiaba"]

# Lista de números
nums = [3, 10, -7, 12.8, -0.5, 4, 22]

# Lista com valores de vários tipos (pouco comum)
mistureba = ["Joaquim", 37, 1.81, 79, True]

#### OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um dos seus
# itens e fazer algo com ele. No exemplo a seguir, vamos
# dar print() em cada uma das frutas da lista
for f in frutas:
    print(f)

# Traço separador
print("-" * 80)

# Percorrendo a lista de números e exibindo o próprio
# número e seu valor elevado a 2
for num in nums:
    print(f"{num} => {num ** 2}")

print("-" * 80)

# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
print("frutas, ANTES:", frutas)
print("nums, ANTES:", nums)

# Inserindo novos itens ao final das listas
frutas.append("maracujá")
nums.append(19)

print("frutas, DEPOIS:", frutas)
print("nums, DEPOIS:", nums)

print("-" * 80)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º ~> a posição onde será feita a inserção (A CONTAGEM COMEÇA
#          EM ZERO!)
#    2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na PRIMEIRA posição
frutas.insert(0, "melancia")

print("Após inserir melancia na posição 0:", frutas)

# Inserindo um novo elemento na QUARTA posição
frutas.insert(3, "amora")

print("Após inserir amora na posição 3:", frutas)

print("-" * 80)


