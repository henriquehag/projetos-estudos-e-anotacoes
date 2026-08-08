print('contando de 1 a 10')

for i in range(10):
    print(i + 1)
#o range começa do 0, então para contar de 1 a 10, é necessário somar 1 ao valor de i.
numero = 10
print('contando de 10 a 20')
while numero <= 20:
    print(numero)
    numero +=1
#o while é utilizado para criar um loop que continua enquanto a condição for verdadeira. Nesse caso, o loop continua enquanto numero for menor ou igual a 20. A cada iteração, o valor de numero é incrementado em 1.

# Procura o número 3 e para a busca
for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        break  # Para tudo!
    print(numero)

# Saída: 1, 2

# Imprime todos os números, exceto o 3
for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        continue  # Pula o 3!
    print(numero)

# Saída: 1, 2, 4, 5


for numero in [1, 2, 3]:
    if numero == 2:
        pass  # Não faz nada, só preenche a linha
    print(numero)

# Saída: 1, 2, 3



#laços com o else junto

# Exemplo 1: O laço roda até o fim sem break -> O else RODA!
for numero in [1, 2, 3]:
    print(numero)
else:
    print("O laço terminou com sucesso, nenhum 'break' foi acionado!")


# Exemplo 2: O laço é interrompido por um break -> O else É IGNORADO!
for numero in [1, 2, 3]:
    if numero == 2:
        break
    print(numero)
else:
    print("Isso NÃO vai ser impresso!") 



#ternarios (resumo das funções), utilizar somente em casos simples, para não prejudicar a legibilidade do código.


#sem ternario (convencional)

nota = 8.5

if nota >= 7.0:
    status = "Aprovado"
else:
    status = "Reprovado"

print(status)  # Saída: Aprovado

#com ternario (mais enxuto)

nota = 8.5

# Atribuição direta usando o ternário
status = "Aprovado" if nota >= 7.0 else "Reprovado"

print(status)  # Saída: Aprovado


#exemplo em print()

idade = 16

print(f"Você é {"maior" if idade >= 18 else "menor"} de idade.")
# Saída: Você é menor de idade.