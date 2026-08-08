#este método é mais eficiente do que o if-elif-else, pois o match-case é otimizado para lidar com múltiplos casos de forma mais clara e legível.

# Exemplo de uso do match-case em Python

comando = "reiniciar"

match comando:
    case "iniciar":
        print("Iniciando o sistema...")
    case "pausar":
        print("Sistema pausado.")
    case "parar":
        print("Sistema encerrado.")
        
        
#exemplo de uso do match-case com validação de comando

comandos_validos = ["iniciar", "pausar", "parar"]
comando = "desconhecido"

if comando not in comandos_validos:
    print("Comando inválido.")
else:
    match comando:
        case "iniciar":
            print("Iniciando o sistema...")
        case "pausar":
            print("Sistema pausado.")
        case "parar":
            print("Sistema encerrado.")
            
            
            
