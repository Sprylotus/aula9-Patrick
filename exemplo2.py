import os

os.system('cls')


try:
    resp = input('Informe (s/n): ').lower()

    if resp =='':
        raise EOFError('Você não digitou nada')
    if resp.isdigit():
        raise ValueError('Não informe números')
except EOFError as e:
    print(f'{e}')
except ValueError as e:
    print(f'{e}')


while True:
    try:
        num = int(input('Informe um número: '))
    except (ValueError) as e:
        print(f'{e} Valor informado não é válido')
    except KeyboardInterrupt as e:
        print(f'{e} Entrada interrompida pelo usuário')
        break
    else:
        print(f'Número {num} informado com sucesso')
        break