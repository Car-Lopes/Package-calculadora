import operacao

repetir = 1

oper = str(input('Digite um operador: '))
op = str(operacao.operacao(oper))

total = 0 


def calcular(a,b,oper=op):  

    oper = op
    #op = str(operacao.operacao(oper))  

    if op == '*' :
        total = a * b;
        return print(f'{a} {op} {b} = {total}')  

    elif op == '/' :
        if a < b:
            return print('a é menor que b - não da para dividir');
        elif b == 0:
            return print('Não existe divisivel por zero');
        else:        
            total = a / b;
            return print(f'{a} {op} {b} = {total}')  

    elif op == '+' :
        total = a + b;
        return print(f'{a} {op} {b} = {total}')  

    elif op == '-' :
        total = a - b
        return print(f'{a} {op} {b} = {total}')  

    else :
        return 'Operador não encontrado 2'


    
while repetir != 0 : 

    a = int(input('Digite um numero: ')) 
    b = int(input('Digite outro numero: ')) 
    print(calcular(a,b))

    repetir = int(input('Digite entre (1 e 0) - 1 para continuar e 0 para encerrar: ')) 

    if repetir == 1:
        oper = str(input('Digite um operador: '))
        op = str(operacao.operacao(oper))
    