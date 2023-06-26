mais18 = 0
homem = 0
mulher20 = 0
cadastro = 0
cont = 's'

while True:
    if cont == 'N':
        break
    nome = str(input('Qual seu nome: '))
    sexo = str(input('Qual seu sexo [M/F]: ').strip().upper()[0])
    while sexo not in 'MF':
        sexo = str(input('Digite uma opção valida! [M/F]: ').strip().upper()[0])
        print(sexo)
    idade = int(input('Qual sua idade: '))
    cadastro += 1
    if sexo == 'M' and idade > 18:
        mais18 += 1
        homem += 1
    elif sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher20 += 1
    cont = str(input('Continuar cadastrando? [S/N]: ').strip().upper()[0])
    
    
    

print(f'{cadastro} foram cadastradas, sendo {homem} homens, dentre eles {mais18} com mais de 18 anos.')
print(f'E {mulher20} mulher com menos de 20 anos! ')