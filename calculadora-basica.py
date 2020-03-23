#Essa calculadora faz operações básicas de soma, subtração, multiplicação e divisão.
#Só funciona com input de 2 números
#Ao final da execução dos cálculos, é perguntado se o usuário quer fazer outro cálculo.

#Operação de soma
def soma (num_1, num_2):
    return num_1 + num_2

#Operação de subtração
def sub (num_1, num_2):
    return num_1 - num_2

#Operação de multiplicação
def mult (num_1, num_2):
    return num_1*num_2

#Operação de divisão, com mensagem para exceção
def div (num_1, num_2):
    try:
        return num_1/num_2
    except ZeroDivisionError:
        return "Essa conta não é possível, pois está dividindo por 0"


#Função para printar as operações, e pede os 2 números que serão utilizados
#Os prints são, usando a "soma" como exemplo, no formato:
#num_1 + num_2 = resultado
def conta(operacao):
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o outro número: "))
    
    if operacao.upper() == "SOMA":
        print("{} + {} = ".format(num_1, num_2), soma(num_1, num_2))
    elif operacao.upper() == "SUB":
        print("{} - {} = ".format(num_1, num_2), sub(num_1, num_2))
    elif operacao.upper() == "MULT":
        print("{} * {} =".format(num_1, num_2), mult(num_1, num_2))
    elif operacao.upper() == "DIV":
        if num_2 == 0:
            print (div(num_1,num_2))
        else:
            print("{} / {} = ".format(num_1, num_2), div(num_1, num_2))

#Separa se o input de operação está na lista ou não
#Se não estiver, printa mensagem de erro e pergunta se a pessoa quer fazer outra conta
def redirec(operacao, list_operacoes):
    if operacao.upper() in list_operacoes:
        conta(operacao)
    else:
        print("Essa palavra não é entrada para contas")
        repetir()

#Função que pergunta se o usuário quer fazer uma nova operação.
def repetir():
    calc_nov = input("""Você gostaria de fazer um novo cálculo?
    Por favor, digite ou "S" para SIM, ou "N" para NÃO: """)

    if calc_nov.upper() == "S":
        __main__()
    elif calc_nov.upper() == "N":
        print("Agradeço a preferência!")           
    else:
        repetir()

#Função principal que pergunta quais operações a pessoa quer fazer, tem os comandos de entrada e a lista de entradas que aceita
def __main__(): 
    operacao = input("""Agora digite o comando da operação: 
    SOMA para somar, 
    SUB para subtrair, 
    MULT para multiplicar, 
    DIV para dividir: """)

    list_operacoes = ["SOMA", "SUB", "MULT", "DIV"]
    
    #chama a função para executar cálculo
    redirec(operacao, list_operacoes)
    #chama a função para fazer um novo cálculo
    repetir()

print("Olá! Esta é uma calculadora que executa contas com somente 2 números")
__main__()