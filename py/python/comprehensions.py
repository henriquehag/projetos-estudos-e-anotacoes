#As Comprehensions (Compreensões) são uma das sintaxes mais famosas e elegantes do Python. Elas oferecem uma forma curta, legível e de altíssima performance para criar novas coleções (Listas, Dicionários e Conjuntos) a partir de coleções já existentes em apenas uma única linha de código.


#convencional
numeros = [1, 2, 3, 4, 5, 6]
quadrados_pares = []

for x in numeros:
    if x % 2 == 0:
        quadrados_pares.append(x ** 2)

print(quadrados_pares)  # [4, 16, 36]


#comprehension
numeros = [1, 2, 3, 4, 5, 6]

quadrados_pares = [x ** 2 for x in numeros if x % 2 == 0]

print(quadrados_pares)  # [4, 16, 36]


#Dicionários com Comprehensions

produtos = ["arroz", "feijão", "café"]

# Cria um dicionário com o produto em maiúsculas e o tamanho do nome
tamanho_produtos = {p.upper(): len(p) for p in produtos}

print(tamanho_produtos)  
# Saída: {'ARROZ': 5, 'FEIJÃO': 6, 'CAFÉ': 4}


#Conjuntos com Comprehensions

palavras = ["python", "java", "python", "c++", "java"]

# Pega apenas o tamanho das palavras sem repetir tamanhos
tamanhos_unicos = {len(p) for p in palavras}

print(tamanhos_unicos)  # Saída: {6, 4, 3}

#laço                || condicao
[x for x in range(10) if x > 5]  # [6, 7, 8, 9]


# condicao                       || laço
["Par" if x % 2 == 0 else "Ímpar" for x in range(4)]
# Saída: ['Par', 'Ímpar', 'Par', 'Ímpar']