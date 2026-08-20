#O comando assert no Python é usado para testar diretamente se uma condição no seu código é verdadeira durante a execução. Quando o programa chega nessa linha, ele avalia a expressão lógica que você definiu. Se o resultado for verdadeiro, o programa simplesmente ignora o comando e avança para a próxima linha normalmente. No entanto, se o resultado for falso, o Python interrompe o funcionamento do script de forma imediata e exibe um erro do tipo AssertionError, sinalizando que o código encontrou um estado ou valor inesperado.



def aplicar_desconto(preco, desconto):
    preco_final = preco - desconto
    
    # Eu, como programador, AFIRMO que o preço final nunca será negativo.
    # Se for, significa que a minha lógica matemática falhou em algum lugar.
    assert preco_final >= 0, "Erro interno: O desconto deixou o preço negativo!"
    
    return preco_final

# Isso funciona perfeitamente (silencioso)
aplicar_desconto(100, 20) 

# Isso quebra o código e dispara o AssertionError
aplicar_desconto(100, 150)






# ERRADO E PERIGOSO!
def logar(usuario, senha):
    assert senha == "1234", "Senha incorreta!"
    print("Acesso liberado!")