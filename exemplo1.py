import os

os.system('cls')


try:
    n = int(input('Informe um número: '))
except:
    print('Erro')


try:
    n = int(input('Informe um número: '))
except ValueError as e:
    print(f'{e}')
except KeyboardInterrupt as e:
    print(f'\nO usuário cancelou a operação')

