# Entrada e Saída em Python
# A função print() é usada para exibir informações na tela.
#print mais simples, apenas texto único
print("Olá, Mundo!")

#print com múltiplos textos
print("Bem-vindo"    " ao "    "Python!")
print("Bem-vindo"+" ao "+"Python!")
print("Bem-vindo","ao","Python!")

#print com calculos
print("O resultado de 2 + 3 é:", 2 + 3)

#print com variáveis
mult = 5 * 4
print("O resultado de 5 * 4 é:", mult)

#print com f-strings (formatação de strings)
mult2 = 10 * 3
print(f"O resultado de 10 * 3 é: {mult2}")

# A função input() é usada para receber informações do usuário.
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao Python!")

# Recebendo múltiplas informações em uma única linha
nome, sobrenome = input("Digite seu nome e sobrenome: ").split()

print(f"Primeiro nome: {nome}")
print(f"Último nome: {sobrenome}")

# Recebendo uma lista de números
numeros_digitados = input("Digite vários números: ").split()

print(f"Você digitou {len(numeros_digitados)} itens.")