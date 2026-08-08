#Ao contrário das listas, as Tuplas são coleções ordenadas e imutáveis (inalteráveis). Uma vez criada uma tupla, você não pode adicionar, remover, reordenar ou alterar nenhum dos seus elementos.

#Elas são utilizadas principalmente para garantir a segurança de dados que não devem mudar ao longo da execução do programa (como coordenadas GPS, dias da semana ou configurações fixas) e por serem mais leves e rápidas em memória do que as listas.

# Usando parênteses (Sintaxe direta)
ponto_cardeal = ("Norte", "Sul", "Leste", "Oeste")

# Usando o construtor tuple() (Converte outros iteráveis em tupla)
numeros_imutaveis = tuple([1, 2, 3, 4])  # Converte lista para tupla: (1, 2, 3, 4)
letras = tuple("Python")                  # ('P', 'y', 't', 'h', 'o', 'n')


# Criando uma tupla com um único elemento

nao_e_tupla = ("Ana")   # Tipo: str
e_uma_tupla = ("Ana",)  # Tipo: tuple

# Acessando elementos de uma tupla

respostas = ("sim", "não", "sim", "talvez", "sim")

qtd_sim = respostas.count("sim")
print(qtd_sim)  # Saída: 3

# Acessando o índice de um elemento específico
dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

posicao = dias.index("Quarta")
print(posicao)  # Saída: 2


# Desempacotando tuplas
coordenadas = (-29.4678, -51.9614)

# Desempacotando latitude e longitude
lat, lon = coordenadas

print(f"Lat: {lat}, Lon: {lon}")  # Lat: -29.4678, Lon: -51.9614


# Função que retorna múltiplos valores (como uma tupla)
def obter_dimensoes():
    largura = 1920
    altura = 1080
    return largura, altura  # Retorna implicitamente a tupla (1920, 1080)

dim = obter_dimensoes()
print(type(dim))  # Saída: <class 'tuple'>