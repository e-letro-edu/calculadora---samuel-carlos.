def soma(a, b):
        return a + b

def subtração(a, b):
     return a - b

def multiplicação(a, b):
        return a * b


def potenciação(a, b):
     return a ** b               

def divisão(a, b):     
    try:
     return a / b        
    except ZeroDivisionError:
            print('Erro! Divisão por zero!')
    

def divisão_exata(a, b):     
        try:
            return a // b        
        except ZeroDivisionError:
            print('Erro! Divisão por zero!')
 

def main():
    print('Calculadora básica Python')
    print('Selecione uma operação:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('6 - Divisão exata')
    escolha = input('Digite sua escolha (1/2/3/4/5/6): ')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    if escolha == '1':
        print('Resultado:', soma(num1, num2))
    elif escolha == '2':
        print('Resultado:', subtração(num1, num2))
    elif escolha == '3':
        print('Resultado:', multiplicação(num1, num2))
    
    elif escolha == '5':
        print('Resultado:', potenciação(num1,num2))
    elif escolha == '6':
        resultado = divisão_exata(num1, num2)
        if resultado is not None:
            print('Resultado:', resultado)
        else:
            print('Opção inválida!') 
    
    elif escolha == '4':
        resultado = divisão(num1, num2)
        if resultado is not None:  
            print('Resultado:', resultado)
    else:
        print('Opção inválida!')
        
if __name__ == "__main__":
    main()
