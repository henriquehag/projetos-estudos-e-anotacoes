#Em Python, uma função lambda é uma pequena função anônima. Isso significa que é uma função criada "na hora", sem precisar de um nome formal definido pela palavra-chave def.

#Elas são perfeitas para operações curtas e simples, geralmente usadas apenas uma vez.


#Sintaxe básica de uma função lambda:
# 1. Jeito Tradicional
def dobrar(x):
    return x * 2

print(dobrar(5))  # Saída: 10


# 2. Usando Lambda
dobrar_lambda = lambda x: x * 2

print(dobrar_lambda(5))  # Saída: 10

#Nota: Atribuir uma lambda a uma variável (como fizemos acima) funciona, mas vai contra as boas práticas do Python. O verdadeiro poder das lambdas aparece quando as usamos diretamente dentro de outras funções.

#Exemplo de uso de lambda com a função map():
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6, 8]


#Exemplo de uso de lambda com a função filter():
palavras = ["abacaxi", "uva", "morango", "maçã"]
ordenadas = sorted(palavras, key=lambda palavra: len(palavra))

print(ordenadas)  # Saída: ['uva', 'maçã', 'abacaxi', 'morango']