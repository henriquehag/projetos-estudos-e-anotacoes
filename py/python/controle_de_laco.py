numeros = [10, 20, 30, 99, 40, 50]

for n in numeros:
    if n == 99:
        print("Achei o 99! Parando a busca...")
        break # Sai do loop na hora!
    print(f"Testando o número: {n}")

print("Código fora do loop segue normalmente.")



# Queremos imprimir apenas os números ímpares
for i in range(1, 6):
    if i % 2 == 0: # Se for par...
        continue   # Pula direto para o próximo número, ignorando o print abaixo
    print(f"Número ímpar encontrado: {i}")
    
    
    
    
senha_correta = True

if senha_correta:
    pass  # Não faça nada, apenas continue o programa
else:
    print("ALERTA: Conta Bloqueada por segurança!")
    

if senha_correta:
    ...  # Faz a mesma coisa que o 'pass'
else:
    print("ALERTA: Conta Bloqueada!")