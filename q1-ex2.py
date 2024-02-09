
#questão 1 Escreva um programa que receba como entrada um número e exiba uma mensagem informando se ele é positivo, negativo ou neutro.
#

for i in range(5):

    num = float(input('Escreva um número'))

    if num > 0:
        print('o numero,', num, 'é positivo!')

    elif num < 0:
        print('o numero,', num, 'é negativo!')

    else:
        print('o numero,', num, 'é neutro')
    
#questão 2 Escreva um programa que receba como entrada um número e exiba uma mensagem informando se ele é par ou ímpar.#

for i in range (5):
    num = float(input('escreva um numero'))

    if num % 2 == 0:
        print('o número,', num, 'é par!') 

    else: 
        print('o número,', num, 'é ímpar!')
        

#questão 3 Escreva um programa que receba como entrada três números e exiba uma mensagem informando qual é o maior deles. #


num1 = int(input('escreva um número'))
num2 = int(input('escreva um número'))
num3 = int(input('escreva um número'))

if num1 >= num2 and num1 >= num3:
    maior_numero = num1

elif num2 >= num1 and num2 >= num3:
    maior_numero = num2

else:
    maior_numero = num3


print('o maior número é:', maior_numero)

#questão 4 Escreva um programa que receba como entrada um número e exiba mensagens informando:
#Se ele é ímpar
#Se ele é múltiplo de 3
#Se ele é divisor de 102

num = int(input("Digite um número: "))


if num % 2 != 0:
    print("Número é ímpar")
else:
    print("Número não é ímpar")

if num % 3 == 0:
    print("Número é múltiplo de 3")
else:
    print("Número não é múltiplo de 3")

if 102 % num == 0:
    print("Número é divisor de 102")
else:
    print("Número não é divisor de 102")

#questão 5 Natália abriu uma loja de bijuterias recentemente e as vendas vão muito bem. Pensando em atrair uma clientela ainda maior, ela deseja oferecer um desconto de 10% para os clientes que gastarem R$ 100,00 ou mais e pagarem em dinheiro. Escreva um programa que receba como entrada o valor do produto comprado e a forma de pagamento escolhida (dinheiro ou cheque), calcule o desconto devido (caso necessário), e exiba o valor final a ser pago.
    
valor_produto = float(input('Qual o valor do produto? '))
forma_pagamento = input('Dinheiro ou cheque? ')

if valor_produto >= 100 and forma_pagamento == 'dinheiro':
    valor_total = valor_produto * 0.9
    print('O valor total é:', valor_total, "Você teve 10% de desconto")

elif forma_pagamento != 'dinheiro' and forma_pagamento != 'cheque':
    print('Forma de pagamento inválida')

else:
    print('O valor total é:', valor_produto)

    #questão 6 em desenvolvimento Passados seis meses, a loja de Natália teve um crescimento surpreendente e agora ela vai aceitar pagamentos também com cartão. O cliente poderá escolher entre as funções débito e crédito do cartão, e ainda parcelar sua compra em até 3 vezes na opção crédito. Modifique o programa anterior para que as novas formas de pagamento sejam consideradas e, além do valor final a ser pago, seja exibido o valor de cada parcela nas compras com cartão de crédito.