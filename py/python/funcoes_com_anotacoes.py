#O Type Hinting (Anotação de Tipos), introduzido a partir do Python 3.5, permite indicar explicitamente os tipos esperados para os parâmetros de uma função e o tipo do valor que ela deve retornar.

#No Python, o Type Hinting é puramente informativo: ele não altera o comportamento dinâmico da linguagem e não impede a execução do programa caso você passe um tipo diferente do anotado.

#estrutura básica de uma função com Type Hinting:
#    param entrada || param saída
def func(a: int) -> str:
    return str(a)

print(func(10))  # Saída: '10' (string)


#Exemplo de função com Type Hinting para parâmetros e retorno:
def processar_usuario(nome: str, idade: int, ativo: bool = True) -> str:
    if ativo:
        return f"Usuário {nome} ({idade} anos) está ativo."
    return f"Usuário {nome} está inativo."

print(processar_usuario("Ana", 28))  # Saída: "Usuário Ana (28 anos) está ativo."

# Lista contendo apenas inteiros
def somar_elementos(numeros: list[int]) -> int:
    return sum(numeros)

# Dicionário com chaves do tipo string e valores do tipo float
def calcular_totais(precos: dict[str, float]) -> float:
    return sum(precos.values())

# Tupla com número exato e ordem de tipos
def obter_coordenada() -> tuple[float, float]:
    return (-29.4678, -51.9614)

print(somar_elementos([1, 2, 3, 4]))  # Saída: 10

print(calcular_totais({"item1": 10.5, "item2": 20.0}))  # Saída: 30.5

print(obter_coordenada())  # Saída: (-29.4678, -51.9614)


#multiplos tipos de entrada (Union) e saída (Optional):

# No Python 3.10+ (Uso do |):
def converter_id(identificador: int | str) -> str:
    return str(identificador)

# Equivalente com typing (Python 3.9-):
from typing import Union

def converter_id_legado(identificador: Union[int, str]) -> str:
    return str(identificador)

print(converter_id(123))  # Saída: '123'
print(converter_id("abc"))  # Saída: 'abc'

print(converter_id_legado(456))  # Saída: '456'
print(converter_id_legado("def"))  # Saída: 'def'



#quando as funções podem retornar um valor ou None, você pode usar o Optional para indicar que o retorno pode ser de um tipo específico ou None.
from typing import Any

def logar_dados(dado: Any) -> None:
    print(f"Log: {dado}")
    
print(logar_dados("Teste de log"))  # Saída: Log: Teste de log