# uma lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

while True:

    resposta = str(input('Você que continuar? ')).upper()[0]

    if resposta == 'S':

        print('Você que Criptografar ou descriptografar uma mensagem?')
        variavel = int(input('Opção 1 ou 2? '))

        if variavel == 1:
            #capture a mensagem do usuário
            mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

        elif variavel == 2:
            #capture a mensagem do usuário
            mensagem = input("Por favor, entre com a mensagem a ser descriptografada: ").lower()



        #estar variável armazenará a mensagem criptografada
        mensagemCriptografada = ""


        #capture a chave secreta
        chave = input("Por favor, entre a chave: ")
        #Esta ação é necessária porque o programa não lê o valor da chave como número
        chave = int (chave)



        #percorra cada caracter na mensagem
        for char in mensagem:

            if char in alfabeto:


                #encontre a posição de caracter em alfabeto
                #por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
                posição = alfabeto.find(char)


                #some a chave secreta para encontrar a posição do caracter criptografado
                #% 26 significa 'volte para 0 quando você atingir 26'
                novaPosicao = (posição + chave) % 26


                #acrescente a letra descriptografada à mensagem
                #a letra criptografada está em alfabeto na novaPosicao
                mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]


            else:
                    
                #alguns caracteres (por exemplo '£', '?') não estão no alfabeto,
                # então simplismente adicione a letra criptografada à mensagem
                mensagemCriptografada = mensagemCriptografada + char
            
        print("Sua mensagem criptografada é:" , mensagemCriptografada)
    else:
        break