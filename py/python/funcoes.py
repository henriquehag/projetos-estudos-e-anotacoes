#No Python, a instrução def é usada para criar funções — blocos de código reutilizáveis projetados para realizar uma tarefa específica.

#Em vez de repetir a mesma lógica ao longo do código, você encapsula o algoritmo dentro de uma função e a invoca quando necessário.

def nome_da_funcao(parametro1, parametro2):
    # Bloco de código (indentado)
    resultado = parametro1 + parametro2
    return resultado

nome_da_funcao(3, 5)  # Chamada da função com argumentos 3 e 5
print(nome_da_funcao(3, 5))  # Saída: 8

#Exemplo de função que calcula o desconto de um produto com base no preço e no percentual de desconto:

def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    return preco - desconto

# O valor retornado é guardado na variável
preco_final = calcular_desconto(100, 15)
print(preco_final)  # Saída: 85.0


#sem return, a função apenas executa uma ação (como imprimir algo na tela) sem retornar um valor específico. Nesse caso, o valor retornado é None.

def saudar(nome):
    print(f"Olá, {nome}!")  # Apresenta algo na tela, mas não 'retorna' dados

resultado = saudar("Carlos")  # Saída visual: Olá, Carlos!
print(resultado)              # Saída: None


#Funções podem ter parâmetros opcionais, permitindo que você forneça valores padrão caso nenhum argumento seja passado durante a chamada da função. Isso é útil para criar funções mais flexíveis e reutilizáveis.

def boas_vindas(nome, mensagem="Seja bem-vindo"):
    return f"{mensagem}, {nome}!"

print(boas_vindas("Ana"))                 # Usa o padrão: "Seja bem-vindo, Ana!"
print(boas_vindas("Beto", "Bom dia"))     # Sobrescreve: "Bom dia, Beto!"


#utilizando os nomes dos parâmetros na chamada da função, você pode passar os argumentos em qualquer ordem, desde que especifique o nome do parâmetro correspondente. Isso aumenta a legibilidade e a flexibilidade do código.

def criar_perfil(nome, idade, cargo):
    return f"{nome} ({idade} anos) - {cargo}"

# A ordem não importa se você nomear os parâmetros:
print(criar_perfil(cargo="Dev", nome="Lucas", idade=30))


#Funções podem retornar múltiplos valores, que são automaticamente empacotados em uma tupla. Isso permite que você retorne várias informações de uma única função de forma organizada.

def min_e_max(lista):
    return min(lista), max(lista)  # Retorna uma tupla (menor, maior)

menor, maior = min_e_max([10, 5, 20, 8])
print(f"Menor: {menor}, Maior: {maior}")  # Menor: 5, Maior: 20



# Em vez de aninhar múltiplos 'if', valide cedo:
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"  # Para aqui mesmo
    
    return a / b


