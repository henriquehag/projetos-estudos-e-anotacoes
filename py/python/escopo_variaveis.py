#O Escopo define onde uma variável existe, onde ela pode ser acessada e até onde ela "vive" dentro do seu código.

#No Python, você sempre pode ler variáveis que estão fora de uma função. Porém, por segurança, o Python não deixa você modificar essas variáveis externas diretamente. É aí que entram as palavras-chave global e nonlocal.




#jeito com problema (não recomendado)
pontuacao = 100

def adicionar_pontos():
    # O Python cria uma nova 'pontuacao' local e ignora a de fora!
    pontuacao = 200  

adicionar_pontos()
print(pontuacao)  # Saída: 100 (A variável externa não foi tocada)


pontuacao = 100

def adicionar_pontos():
    global pontuacao  # Avisa que vamos mexer na variável externa
    pontuacao += 50   # Agora sim, estamos alterando o valor real

adicionar_pontos()
print(pontuacao)  # Saída: 150


#O nonlocal é usado exclusivamente quando você tem uma função dentro de outra função (funções aninhadas).

#Se a função de dentro quiser modificar uma variável da função de fora (mas que não é uma variável global do arquivo), você usa o nonlocal. Ele diz: "Suba um nível de escopo, mas não vá até o topo global".



def jogo():
    vidas = 3  # Variável local de jogo(), mas externa para perder_vida()
    
    def perder_vida():
        nonlocal vidas  # Avisa que vamos mexer na 'vidas' da função pai
        vidas -= 1
        print(f"Você perdeu uma vida! Restam {vidas}.")
        
    perder_vida()
    perder_vida()

jogo()
# Saída:
# Você perdeu uma vida! Restam 2.
# Você perdeu uma vida! Restam 1.