
def operacao(operador):
    
    #operador = input('Digite um Operador: ')
    #operador = ' '

    while operador != '*' and operador != '/'  and operador != '-' and operador != '+':
    
        print('Operador não encontrado 1')
        operador = str(input('Digite um operador valido: '))
    
    return operador