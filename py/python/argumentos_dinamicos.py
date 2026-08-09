#Os Argumentos Dinâmicos (*args e **kwargs) são recursos que permitem que uma função receba uma quantidade indefinida (variável) de parâmetros. Você não precisa saber de antemão quantos argumentos o usuário vai passar.

#O grande "segredo" aqui não são as palavras args ou kwargs (que são apenas convenções da comunidade), mas sim os asteriscos (* e **), que atuam como operadores de empacotamento (packing).

#O *args pega todos os argumentos posicionais extras que você passar para a função e os empacota em uma Tupla.



def somar_tudo(*args):
    # args se torna uma tupla: (10, 20, 30)
    total = sum(args)
    return total

print(somar_tudo(10, 20))          # Saída: 30
print(somar_tudo(1, 2, 3, 4, 5))   # Saída: 15
print(somar_tudo())                # Saída: 0

#mistura de argumentos fixos e dinâmicos (*args). Os argumentos fixos devem vir antes dos dinâmicos.
def exibir_time(capitao, *jogadores):
    print(f"Capitão: {capitao}")
    print(f"Restante do time: {jogadores}")
    
exibir_time("Lucas", "Ana", "Beto", "Carla")

#O **kwargs (Keyword Arguments) captura todos os argumentos nomeados (passados no formato nome=valor) que não foram definidos na função e os empacota em um Dicionário.


def criar_perfil(nome, **kwargs):
    # kwargs se torna um dicionário: {'idade': 28, 'cidade': 'Lajeado'}
    print(f"Nome do usuário: {nome}")
    
    for chave, valor in kwargs.items():
        print(f"- {chave.capitalize()}: {valor}")

criar_perfil("Ana", idade=28, cidade="Lajeado", profissao="Desenvolvedora")

#*args deve sempre vir antes de **kwargs na definição da função, caso contrário, o Python não saberá como separar os argumentos posicionais dos nomeados.

def super_funcao(a, b, *args, **kwargs):
    print(a, b)       # Pegou os dois primeiros (1, 2)
    print(args)       # Pegou o que sobrou sem nome: (3, 4)
    print(kwargs)     # Pegou tudo que tinha nome: {'x': 100, 'y': 200}

super_funcao(1, 2, 3, 4, x=100, y=200)


def saudar_tres_pessoas(p1, p2, p3):
    print(f"Olá {p1}, {p2} e {p3}!")

amigos = ["Lucas", "Marcos", "Julia"]

# O asterisco "explode" a lista, passando cada item como um argumento
saudar_tres_pessoas(*amigos)