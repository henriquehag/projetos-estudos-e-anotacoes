texto = "PYTHON"

print(texto[0])  # Saída: "P" (Primeira letra)
print(texto[2])  # Saída: "T" (Terceira letra)

print(texto[-1]) # Saída: "N" (Última letra)
print(texto[-2]) # Saída: "O" (Penúltima letra)

# Pega da posição 0 até a 2 (lembre-se, o 3 fica de fora)
print(texto[0:3])  # Saída: "PYT"

# Pega da posição 2 até a 4 (o 5 fica de fora)
print(texto[2:5])  # Saída: "THO"

# Como não há início, ele começa do zero e vai até o índice 3 (exclusive)
print(texto[:3])   # Saída: "PYT"

# Como não há fim, ele começa no índice 3 e vai até a última letra
print(texto[3:])   # Saída: "HON"

# Sem início e sem fim, ele faz uma cópia inteira do texto
print(texto[:])    # Saída: "PYTHON"



alfabeto = "ABCDEFGHIJ"

# Do começo ao fim, pulando de 2 em 2
print(alfabeto[0:10:2]) 
# Saída: "ACEGI" (Pegou A, pulou B, pegou C, pulou D...)

# Atalho: você pode omitir o início e o fim e usar só o passo
print(alfabeto[::2]) 
# Saída: "ACEGI"


texto = "PYTHON"

# Lê do começo ao fim (omitidos), mas dando passos para trás (-1)
print(texto[::-1]) 
# Saída: "NOHTYP"