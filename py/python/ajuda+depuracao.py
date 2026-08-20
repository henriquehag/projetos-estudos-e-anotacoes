#help(obj) — O Manual Integrado

# Quero saber como a função 'len' funciona
help(len)

# Quero ver os detalhes dos métodos de uma Lista
help(list)

#Dica de Ouro: Você pode usar o help() até nas funções que você mesmo criou, desde que tenha escrito uma docstring (aquelas três aspas logo abaixo do def).
def somar(a, b):
    """Esta função recebe dois números e retorna a soma deles."""
    return a + b

help(somar) # Vai imprimir a sua frase explicativa!



#breakpoint() — O Inspetor de Código

def calcular_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    
    # O CÓDIGO VAI PAUSAR EXATAMENTE AQUI!
    breakpoint() 
    
    preco_final = preco - valor_desconto
    return preco_final

calcular_desconto(200, 15)