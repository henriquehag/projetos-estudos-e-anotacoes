#Os Conjuntos (set) no Python são coleções não ordenadas de elementos únicos. Eles são baseados na Teoria dos Conjuntos da matemática e trazem duas características fundamentais:

#1--Não admitem elementos duplicados: Se você tentar inserir o mesmo valor duas vezes, o conjunto simplesmente ignorará a segunda inserção.

#2--Não possuem ordem (não indexados): Os elementos não têm uma posição fixa (0, 1, 2...). Por isso, não é possível acessar itens usando colchetes como conjunto[0].


# Usando chaves (Sintaxe direta)
frutas = {"maçã", "banana", "laranja"}

# Convertendo uma lista com duplicatas em um set (Remove duplicatas automaticamente)
numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_unicos = set(numeros_repetidos)

print(numeros_unicos)  # Saída: {1, 2, 3, 4, 5}


# Adicionando elementos a um conjunto
linguagens = {"Python", "Java"}
linguagens.add("C++")
linguagens.add("Python")  # Já existe, será ignorado

print(linguagens)  # {'Python', 'Java', 'C++'}

# Removendo elementos de um conjunto
tags = {"python", "codigo", "backend"}

tags.discard("codigo")   # Remove 'codigo'
tags.discard("frontend") # Não existe no set, mas roda sem quebrar o programa!

print(tags)  # {'python', 'backend'}



# Operações com Conjuntos

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. União (.union() ou |) -> Junta todos os elementos sem repetir
print(a.union(b))  # {1, 2, 3, 4, 5, 6}

# 2. Interseção (.intersection() ou &) -> Apenas os elementos presentes em AMBOS
print(a.intersection(b))  # {3, 4}

# 3. Diferença (.difference() ou -) -> Elementos que estão em 'a', mas NÃO em 'b'
print(a.difference(b))  # {1, 2}

# 4. Diferença Simétrica (.symmetric_difference() ou ^) -> Elementos que NÃO são compartilhados
print(a.symmetric_difference(b))  # {1, 2, 5, 6}




# Conjuntos Imutáveis (frozenset)



# Criando a partir de uma lista
permissoes = frozenset(["ler", "escrever", "executar"])

print(permissoes)  # frozenset({'ler', 'escrever', 'executar'})
print(type(permissoes))  # <class 'frozenset'>


# Tentando adicionar um elemento a um frozenset (vai gerar erro)
permissoes = frozenset(["ler", "escrever"])

# Isso vai lançar um AttributeError:
permissoes.add("deletar")  # ❌ Erro! 'frozenset' object has no attribute 'add'


# Frozensets podem ser usados como chaves em dicionários ou elementos de outros conjuntos, ao contrário dos sets normais, que são mutáveis e, portanto, não podem ser usados como chaves.

grupo_a = frozenset([1, 2, 3])
grupo_b = frozenset([3, 4, 5])

# União, interseção, diferença etc. continuam funcionando:
uniao = grupo_a | grupo_b  # frozenset({1, 2, 3, 4, 5})
intersecao = grupo_a & grupo_b  # frozenset({3})

# Criando um dicionário com frozensets como chaves

perfis = {
    frozenset(["ler"]): "Leitor",
    frozenset(["ler", "escrever"]): "Editor",
    frozenset(["ler", "escrever", "executar"]): "Admin"
}

# Buscando pelo conjunto de permissões:
minhas_permissoes = frozenset(["ler", "escrever"])
print(perfis[minhas_permissoes])  # Saída: Editor