import os
os.system('cls')

while True:
    print('CALCULADORA DE NUMEROS DECIMAIS PARA BINÁRIO, OCTADECIMAL E HEXADECIMAL\n')
    opcao = input('[1]BINARIO\n[2]OCTADECIMAL\n[3]HEXADECIMAL\n[4]SOBRE\n[5]SAIR\nESCOLHA UMA OPÇÃO: ')
    base = ''
    resp = 's'
    digitos = '0123456789ABCDEF'


    if opcao == '5':
        print('Obrigado por utilizar nossa calculadora!')
        break
    elif opcao == '4':
       print('VERSÃO DA CALCULADORA: 1.0\nCiências da Computação\nBreno Fiusa Lopes  RGM:538768071\nEdivan Mendonça de Jesus  RGM:38645955\nJúlia Monteiro  RGM:37383604\nRenato Passos da Cruz  RGM:537900854\nSabrina Ramos dos Reis  RGM:39205011\n')
       break
    if opcao not in ['1', '2', '3']:
        print('Não foi uma opção valida, por favor escolha novamente')
        input('Pressione qualquer tecla para continuar: ')
        continue
    
    while resp != 'n':
        os.system('cls')
        converte = ''
        if opcao == '1':
              base = '2'
              num = int(input(f'Digite um número decimal inteiro para conversão para base {base} (Binário): '))
              num_inteiro = num
              while num > 0:
                  c = num % 2
                  num = num // 2
                  converte = str(c) + converte
        elif opcao == '2':
             base = '8'
             num = int(input(f'Digite um número decimal inteiro para conversão para base {base} (OCTADECIMAL): '))
             num_inteiro = num

             while num > 0:
                  c = num % 8
                  num = num // 8
                  converte = str(c) + converte
        elif opcao == '3':
             base = '16'
             num = int(input(f'Digite um número decimal inteiro para conversão para base {base} (HEXADECIMAL): '))
             num_inteiro = num

             while num > 0: 
                  c = num % 16
                  num = num // 16
                  converte = digitos[c] + converte
        print(f'o número {num_inteiro} na base 10 é igual a {converte} na base {base}\n')
        resp = input(f'Deseja continuar convertendo para base {base}, S/N ?\n').lower()
        os.system('cls')