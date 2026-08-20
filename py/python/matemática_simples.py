#abs(x) — Valor Absoluto
#Retorna a distância de um número até o zero (ou seja, elimina o sinal negativo, se houver).

print(abs(-15))  # Saída: 15
print(abs(8.5))  # Saída: 8.5

#round(numero, casas_decimais) — Arredondamento

print(round(3.14159, 2))  # Saída: 3.14
print(round(7.8))         # Saída: 8


#divmod(dividendo, divisor) — Divisão + Resto em um só comando

# Queremos dividir 10 por 3
quociente, resto = divmod(10, 3)

print(f"Resultado: {quociente}, Resto: {resto}")
# Saída: Resultado: 3, Resto: 1

horas, minutos = divmod(135, 60)  # 135 minutos -> 2h e 15min

#pow(base, expoente, modulo) — Potenciação

print(pow(2, 3))  # Saída: 8 (2³)
# (2³ % 5) -> (8 % 5) = 3
print(pow(2, 3, 5))  # Saída: 3



#min() e max() — Menor e Maior Valor

# Passando uma lista
notas = [6.5, 9.8, 4.2, 8.0]
print(min(notas))  # Saída: 4.2
print(max(notas))  # Saída: 9.8

# Passando valores soltos
print(max(10, 50, 20))  # Saída: 50

#Com strings: Ambas funcionam com texto, baseando-se na ordem alfabética (tabela Unicode):
print(min("ana", "beatriz", "carlos"))  # Saída: "ana"



#sum(iteravel, inicio) — Soma de Elementos

precos = [10.50, 25.00, 5.00]
print(sum(precos))  # Saída: 40.5

# Começa somando em 100 e adiciona a lista
print(sum([10, 20], start=100))  # Saída: 130