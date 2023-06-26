contagem = ('zero','um', 'dois', 'tres' , 'quatro', 'cinco' , 'seis', 'sete',
             'oito', 'nove', 'dez', 'onze', 'dose', 'treze', 'catorze', 'quinze' ,
               'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')


while True:
  num = int(input('Digite um numero entre 0 e 20: '))
  if num >= 0 and num <=20:
    print(f'O numero {num} se escreve {contagem[num]}')
  elif num < 0 or num > 20:
    print('Tente novamente') 
  elif num == '':
    break



