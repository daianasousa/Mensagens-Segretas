#lista de letras para criptografiar
alfabeto = "abcdefghijklmnopqrstuvwxyz"


#a chave secreta é 3
chave = 3

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.

posicao = alfabeto.find(letra)

#some a chaves secreta para encotrar a posição da letra criptografada
#% 26 significa 'volte para 0 quando você chegar no 26'

#subtraia a chave para voltar para trás
novaPosicao = (posicao - chave) % 26


#a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é" , letraCriptografada )