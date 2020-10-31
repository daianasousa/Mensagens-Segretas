print('Calculadora do Amor')
print('<3 '*7)

placar = 0

#capture a mensagem do usuário
mensagem = input("Digite o nome de 2 pessoas: ").lower().strip()


#estar variável armazenará a mensagem criptografada
mensagemCriptografada = ""




#percorra cada caracter na mensagem
for char in mensagem:

    if char in 'aãeiou':
        placar += 5

    if char in "amor":
        placar += 10
    
print(f"Seu placar de compatibilidade : {placar} ")

if placar < 10:
    print('Esqueça esta pessoa! Nunca vai dar certo!')

elif placar >= 10 and placar < 30:
    print('Dificil mais não impossivel de dar certo!')

elif placar >= 30 and placar <= 50:
    print('Com dedicação e perseverança pode da certo!')
elif placar > 50 and placar <= 70:
    print('A uma boa chancer desse relacionamento ter um futuro brilhante!')
elif placar > 70 and placar <= 80:
    print('Vocês terão um relacionamento muito intenso! <3')
else:
    print('Vocês nasceram um para o outro <3 <3 <3')
