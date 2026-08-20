# Abrindo um arquivo para leitura
arquivo = open("py/python/texto_teste.txt", "r")

print(arquivo.read())  # Lê todo o conteúdo do arquivo e imprime na tela

# "r" significa "read" (leitura). Se o arquivo não existir, o Python lançará um erro.
# "w" significa "write" (escrita). Se o arquivo não existir, ele será criado.
# "a" significa "append" (acrescentar). Se o arquivo não existir, ele será criado. Se existir, o conteúdo será adicionado ao final.
# "x" significa "exclusive creation" (criação exclusiva). Se o arquivo já existir, o Python lançará um erro.
# "b" significa "binary" (binário). Usado para arquivos binários, como imagens ou vídeos.
# "rb" or "r+" significa "read and write" (leitura e escrita). Permite ler e escrever no mesmo arquivo. Se o arquivo não existir, o Python lançará um erro.


# 1. Abre o arquivo em modo de escrita
documento = open("py/python/convidados.txt", "w")

# 2. Faz as operações necessárias
documento.write("Ana\nBeto\nCarlos\n Diana\n Eduardo\n Fernanda\n Gustavo\n Helena\n Igor\n Juliana\n Kleber\n Lucas\n Mariana\n Nicolas\n Olivia\n Pedro\n Quésia\n Rafael\n Sabrina\n Tiago\n Ursula\n Vanessa\n William\n Xuxa\n Yara\n Zeca \n ")

# 3. Fecha o arquivo e libera o sistema
documento.close()


#le tudo de uma vez
arquivo = open("py/python/convidados.txt", "r")

# Lê o arquivo inteiro
textoCompleto = arquivo.read()
print(textoCompleto)

arquivo.close()

#Dica: Você pode passar um número dentro dos parênteses, como .read(10), e o Python vai ler apenas os primeiros 10 caracteres.


arquivo = open("py/python/convidados.txt", "r")

# Retorna algo como: ["Ana\n", "Beto\n", "Carlos\n"]
listaConvidados = arquivo.readlines()

for pessoa in listaConvidados:
    print(pessoa)

arquivo.close()


# Modo "a" (append) adiciona no fim sem apagar o que já existe
relatorio = open("py/python/vendas.txt", "a")

relatorio.write("Produto vendido: Notebook\n")
relatorio.write("Valor: 3500.00\n")

relatorio.close()



#Você lembra da regra de ouro do passo anterior? "Sempre feche a porta!" (.close()).

#O problema é que, no mundo real, programadores esquecem de fechar arquivos. Pior ainda: se o seu código der um erro e travar bem no meio da leitura/escrita, o programa morre antes de chegar na linha do .close(), deixando o arquivo travado na memória.

#Para resolver isso de forma elegante, o Python criou o Gestor de Contexto, usando a palavra-chave with.




with open("py/python/texto_teste.txt", "r") as documento:
    texto = documento.read()
    print(texto)
    
# Assim que a indentação acaba, o arquivo é FECHADO automaticamente!