# raise, é a ferramenta utilizada para disparar erros em Python. Abaixo, temos um exemplo de como utilizá-la:
# o raise é um break só que exclusivo para erros, mas ele para ao invez de quebrar o loop que nem o break


# O jeito fraco (apenas avisa, mas não impede problemas futuros)
def transferir(valor):
    if valor <= 0:
        print("Erro: O valor deve ser positivo!")
        return None
    
    
    
# O jeito forte (avisa e impede problemas futuros)
def transferir(valor):
    if valor <= 0:
        # Dispara o erro e INTERROMPE a função na mesma hora
        raise ValueError("Operação negada: O valor da transferência deve ser maior que zero.")
    
    print(f"Transferindo R$ {valor}...")

transferir(-50)


#escolhendo o erro certo

def cadastrar_idade(idade):
    if type(idade) is not int:
        raise TypeError("A idade deve ser um número inteiro!")
    
    if idade < 18:
        raise ValueError("Acesso negado: Usuário menor de idade.")
        
    print("Cadastro aprovado!")
    
    

try:
    10 / 0
except ZeroDivisionError as e:
    print("Anotando no arquivo de log que alguém tentou dividir por zero...")
    # Repassa o erro original para quem chamou a função lidar com ele
    raise