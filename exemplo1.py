import os

os.system('cls')


try:
    n = int(input('Informe um número: '))
except:
    print('Erro')


try:
    n = int(input('Informe um número: '))
except (ValueError, KeyboardInterrupt, IndexError) as e:
    print(f'Erro: {e}')
else:
    print(f'Você informou: {n}')

try:    
    txt= input('Informe o nome: ')[0]
except IndexError:
    print(f'Precisa digitar algo')
else:
    print('Acertou')
finally:
    print('Sempre executado')