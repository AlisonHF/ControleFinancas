from csv_ import Arquivo
from dados import Criacao_Dados
import os
from time import sleep

gastos = Criacao_Dados()
arquivos = Arquivo()

while True:
    print( '1- Adicionar gasto\n\
2- Total\n\
3- Visualizar planilha\n\
4- Salvar planilha na area de trabalho\n\
5- Sair\
        ')
    
    usuario = input('Digite a opção:')
    if usuario == '1':
        arquivos.adicionar(gastos.criar_dados())
        print('Dados salvos com sucesso!')
        sleep(2)
        os.system('cls')

    elif usuario == '2':
        while True:
            print(arquivos.total())
            usuario = input('Para sair do modo visualização digite "0"\n')
            if usuario == '0':
                os.system('cls')
                break

    elif usuario == '3':
        while True:
            arquivos.visualizar()
            usuario = input('Para sair do modo visualização digite "0"\n')
            while not usuario == '0':
                usuario = input('Para sair do modo visualização digite "0"\n')
                break
            os.system('cls')
            break
    elif usuario == '4':
        arquivos.salvar_copia()
        sleep(3)
        os.system('cls')

    elif usuario == '5':
        print('Fechando o programa...')
        sleep(2)
        break
