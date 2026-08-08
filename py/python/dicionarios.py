#Os Dicionários (dict) são estruturas de dados mutáveis que armazenam elementos no formato de pares chave: valor (Key: Value).

#Diferente das listas e tuplas, que utilizam índices numéricos (0, 1, 2...), os dicionários utilizam as próprias chaves como forma de acesso rápido aos dados.

# As Duas Regras de Ouro dos Dicionários
# 1-Chaves devem ser únicas: Se você tentar adicionar uma chave que já existe, o Python irá sobrescrever o valor antigo pelo novo.

# 2-Chaves devem ser imutáveis: As chaves precisam ser de tipos imutáveis (como str, int, float ou tuple). Valores podem ser de qualquer tipo, inclusive listas e outros dicionários.

#resumindo, dicionarios são uma lista de variaveis e valores, onde cada variavel é uma chave e cada valor é o valor associado a essa chave.


# Usando chaves (Forma mais comum)
pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Lajeado"
}

# Usando a função dict()
produto = dict(nome="Notebook", preco=3500.00, estoque=10) #print (produto) 
# { 'nome': 'Notebook',
#   'preco': 3500.0,
#   'estoque': 10}


dados = {"nome": "Carlos",
         "cargo": "Dev"}

# Sem erro, retorna o valor padrão
salario = dados.get("salario", 0.0)
print(salario)  # Saída: 0.0

print(dados.keys())  # dict_keys(['nome', 'cargo'])
print(dados.values())  # dict_values(['Carlos', 'Dev'])
print(dados.items())  # dict_items([('nome', 'Carlos'), ('cargo', 'Dev')])


#alterando valores de um dicionario
config = {"tema": "escuro", "fonte": 12}

# Atualiza 'fonte' e adiciona 'notificacoes'
config.update({"fonte": 14, "notificacoes": True})

print(config)
# Saída: {'tema': 'escuro', 'fonte': 14, 'notificacoes': True}



#removendo itens de um dicionario
inventario = {"espada": 1, "escudo": 1, "pocao": 5}

# Remove o último item adicionado
item_removido = inventario.popitem()

print(item_removido)  # ('pocao', 5)
print(inventario)     # {'espada': 1, 'escudo': 1}

#Nota: Além do .popitem(), existe o .pop("chave"), que remove uma chave específica informada por você.