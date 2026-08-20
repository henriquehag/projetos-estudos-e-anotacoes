#ord("letra") — De Letra para Número

print(ord("A"))  # Saída: 65
print(ord("a"))  # Saída: 97 (Maiúsculas e minúsculas têm números diferentes!)
print(ord("@"))  # Saída: 64

#chr(numero) — De Número para Letra

print(chr(65))   # Saída: "A"
print(chr(97))   # Saída: "a"
print(chr(9829)) # Saída: "♥" (Coração na tabela Unicode)



#Juntando as duas (Aplicações Práticas)

letra_original = "A"

# 1. Traduz "A" para número (65)
codigo = ord(letra_original)

# 2. Desloca matematicamente (65 + 2 = 67)
novo_codigo = codigo + 2

# 3. Traduz o 67 de volta para letra
letra_criptografada = chr(novo_codigo)

print(letra_criptografada) # Saída: "C"