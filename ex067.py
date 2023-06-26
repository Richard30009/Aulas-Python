tabuada = int(input('Digite o numero que voce deseja saber a taboada: '))
mult = 0
resul = 0
while True:
    resul = tabuada * mult
    
    print(f'{tabuada} x {mult} = {resul}' )
    mult +=1
    if mult > 10: 
        tabuada = int(input('Quer ver a tabuada de qual valor: '))
        mult = 0
    if tabuada < 0:
        break
    
       
    

print('FIM')
