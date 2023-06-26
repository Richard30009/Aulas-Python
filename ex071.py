#simulador caixa eletronico
import time
saldo = 999999.00
print('Bem vindo ao BancoSimulator!! Maior banco da America latina')
op = 
0

while True:
    #print('{:-^40}'.format('Menu Principal'))
    #op = int(input(' [1] Consultar saldo \n [2] Sacar \n [3] Depositar \n [4] Sair \n ')) # opçoes do menu
    while op == 1:
        print('{:-^40}'.format('SALDO'))
        print(f'----------R$ {saldo:.2f}----------')
        op = int(input(' [1] Menu Principal \n [2] Sacar \n [3] Depositar \n [4] Sair \n '))    
        if op == 1:
            break
    while op == 2:
        print('{:-^40}'.format('SAQUE'))
        print('Cedulas Disponiveis: R$200 - R$50 - R$20 - R$10 - R$2')
        sacar = int(input('Digite o valor a ser Saquado: '))
        verif = sacar % 2 #verificar se as cedulas sao capazes de pagar
        if verif == 0:
            print(f'Voce tem certeza que deseja sacar R${sacar}.')
            op = int(input(' [1] Sim - [2] Digitar outro valor - [3] Menu Principal [4] Sair'))
        else:
            print('Não é possivel sacar esse valor')
            op = int(input(' [1] Digitar outro valor - [2] Menu Principal - [3] Sair '))
            if op == 1: #sacando
                saldo = saldo - sacar
                print(f'Saldo Atual R${saldo}')
                op = int(input('[1] Menu Principal - [2] Novo Saque - [3] Sair'))
                if op == 1:
                    break
    while op == 3:
        print('{:-^40}'.format('DEPOSITO'))
        deposit = int(input('Qual o valor que deseja depositar: '))
        saldo = saldo + deposit
        print(f'Novo Saldo R${saldo:.2f}')
        op = int(input(' [1] Menu Principal - [2] Sacar - [3] Depositar outro valor [4] Sair \n'))
    
    print('{:-^40}'.format('Menu Principal'))
    op = int(input(' [1] Consultar saldo \n [2] Sacar \n [3] Depositar \n [4] Sair \n ')) # opçoes do menu    
                

                        

