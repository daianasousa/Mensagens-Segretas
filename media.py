lista = list()
soma = 0
for n in range(6):
    nota = float(input(f'Digite a nota {n+1}: '))
    soma += nota
    lista.append(nota)
menor = min(lista)
b1 = (soma - menor) / 5
print(f'A menor nota foi {menor}')

soma1 = 0
for n in range(6):
    nota = float(input(f'Digite a nota {n+7}: '))
    soma1 += nota
    lista.append(nota)
menor = min(lista)
b2 = (soma1 - menor) / 5
print(f'A menor nota foi {menor}')


print(f'Média do Primeiro Bimestre: {b1:.2f}')
print(f'Média do Segundo Bimestre: {b2:.2f}')

media_final = (b1 + b2) / 2
print(f'A sua média final foi  {media_final:.2f}')

if media_final < 4:
    print('Reprovado')
elif media_final >= 4 and media_final < 7:
    print('Recuperação')
elif media_final > 7:
    print('Aprovado')