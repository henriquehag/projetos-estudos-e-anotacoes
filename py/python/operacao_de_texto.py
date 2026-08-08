# Operação de Texto em Python
# A função strip() é usada para remover espaços em branco no início e no final de uma string.
texto = "   Olá, mundo!   "
print(texto.strip())


# A função zfill() é usada para preencher uma string com zeros à esquerda até atingir um comprimento específico.
numero = "42"
print(numero.zfill(5))


# A função upper() é usada para converter uma string para letras maiúsculas.
texto = "Python é legal"
print(texto.upper())


# A função lower() é usada para converter uma string para letras minúsculas.
texto = "PyThOn"
print(texto.lower())

# A função replace() é usada para substituir partes de uma string por outra string.
frase = "Eu gosto de maçã"
print(frase.replace("maçã", "morango"))


# A função split() é usada para dividir uma string em uma lista de substrings com base em um delimitador.
datas = "20/05/2026"
print(datas.split("/"))


# A função join() é usada para unir uma lista de strings em uma única string, usando um delimitador específico.
palavras = ["Python", "é", "fácil"]
cola = " " 
print(cola.join(palavras)) 
print("-".join(palavras))



# A função find() é usada para encontrar a posição de uma substring dentro de uma string. Retorna -1 se não encontrar.
frase = "Aprender programação"
print(frase.find("pro")) 
# Saída: 9 (A palavra "pro" começa no 9º caractere)

print(frase.find("java"))
# Saída: -1 (Não encontrou)



# A função count() é usada para contar o número de ocorrências de uma substring dentro de uma string.
palavra = "banana"
print(palavra.count("a")) 
# Saída: 3 (a letra 'a' aparece três vezes)

print(palavra.count("na"))
# Saída: 2 (o bloco 'na' aparece duas vezes)