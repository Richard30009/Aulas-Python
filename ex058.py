from random import randint


comp = randint(0,10)
print('Eai panaca, estou pensando em um numero, sera que consegue advinhar ?')
print('Vou pensar entre 0 e 10!')
resposta = False
tentativa = 0
while not resposta:
    jogador = int(input('Qual o seu palpite? '))
    tentativa += 1
    if jogador == comp:
        resposta = True
    else: 
        if comp < jogador:
            print('Voce errou... pensei em um nomero menor')
        else:
            print('Voce errou... pensei em um nomero maior')

    
    

print('Parabens voce acertou em {} tentativas!'.format(tentativa))



 
