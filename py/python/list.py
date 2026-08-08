#As Listas no Python são coleções ordenadas e mutáveis (alteráveis). Isso significa que, diferente de outros tipos de dados, você pode modificar, adicionar, mover ou apagar elementos de uma lista diretamente na memória, sem precisar criar uma nova do zero.

#crição de listas

# Usando colchetes (Sintaxe direta)
frutas = ["maçã", "banana", "laranja"]

# Usando o construtor list() (Útil para converter outros iteráveis)
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
letras = list("Python")       # ['P', 'y', 't', 'h', 'o', 'n']


#adicionando elementos a uma lista 

times = ["Grêmio", "Inter"]
times.append("Juventude") #adiciona sempre no final da lista

print(times)  # ['Grêmio', 'Inter', 'Juventude']

#adicionando elementos em uma posição específica da lista

jogadores = ["Pelé", "Maradona"]
jogadores.insert(1, "Messi")  # Insere no índice 1

print(jogadores)  # ['Pelé', 'Messi', 'Maradona']

#adicionando uma lista dentro de outra lista

compras = ["arroz", "feijão"]
mais_compras = ["café", "açúcar"]

compras.extend(mais_compras)

print(compras)  # ['arroz', 'feijão', 'café', 'açúcar']


#removendo elementos de uma lista

fila = ["Ana", "Beto", "Carlos"]

atendido = fila.pop(0)  # Remove o primeiro ("Ana")

print(atendido) # Ana
print(fila)     # ['Beto', 'Carlos']

tarefas = ["estudar", "limpar", "estudar"]
tarefas.remove("estudar")  # Remove apenas a PRIMEIRA ocorrência

print(tarefas)  # ['limpar', 'estudar']

#apagar todos os elementos de uma lista

carrinho = ["notebook", "mouse"]
carrinho.clear()

print(carrinho)  # []


#organizando elementos de uma lista

valores = [42, 10, 5, 23]
valores.sort()

print(valores)  # [5, 10, 23, 42]

# Para ordenar de forma decrescente:
valores.sort(reverse=True)
print(valores)  # [42, 23, 10, 5]