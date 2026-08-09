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
documento = open("py/python/relatorio.txt", "w")

# 2. Faz as operações necessárias
documento.write("Novo relatorio gerado com sucesso.")

# 3. Fecha o arquivo e libera o sistema
documento.close()