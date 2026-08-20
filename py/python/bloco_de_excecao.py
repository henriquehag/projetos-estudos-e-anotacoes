#Quando um erro acontece no Python (como tentar dividir um número por zero, ou buscar um arquivo que não existe), o interpretador entra em pânico: ele gera uma Exceção, trava o programa na mesma hora e cospe aquela famosa mensagem de erro em vermelho na tela.

#O bloco de tratamento de exceções serve para você dizer ao Python: "Tente fazer isso, mas se der errado, não entre em pânico. Siga este plano B".


#A estrutura possui quatro partes. Apenas o try e o except são obrigatórios, mas o else e o finally dão um controle perfeito sobre o fluxo.
try:
    # 1. Tente executar este código que é "arriscado"
    numero = int(input("Digite um número divisor: "))
    resultado = 100 / numero

except ValueError:
    # 2A. O plano B se o usuário digitou letras em vez de números
    print("Erro: Você precisa digitar um número inteiro!")

except ZeroDivisionError:
    # 2B. O plano B se o usuário digitou o número 0
    print("Erro: A matemática não permite divisão por zero!")

except Exception as e:
    # 2C. O plano C caso aconteça um erro que eu não previ
    print(f"Ocorreu um erro inesperado: {e}")

else:
    # 3. Sucesso! Só roda se o bloco 'try' não teve NENHUM erro
    print(f"Deu tudo certo! O resultado é {resultado}")

finally:
    # 4. Encerramento! Roda SEMPRE, dando erro ou não
    print("Operação finalizada.")