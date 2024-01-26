import data_

class Criacao_Dados():

    def convert_dinheiro(self, valor):
        valor_ = f'R${float(valor):.2f}'
        return valor_

    def criar_dados(self):
        dicionario = dict()
        dicionario['Data'] = data_.retornar_data()

        while True:
            nome = str(input('Digite o nome do gasto: '))
            if nome == '':
                print('Erro! Nome vazio')
            else:
                dicionario['Nome'] = nome
                break

        while True:
            try:
                valor = float(input('Digite o valor (Sem cifrão): '))
                dicionario['Valor'] = self.convert_dinheiro(valor)
                break

            except ValueError:
                print('Digite o valor sem cifrão ou caracteres!')
        dicionario['Valor'] = self.convert_dinheiro(valor)
        return [dicionario] # type: ignore


if __name__ == '__main__':
    dados1 = Criacao_Dados()
    print(dados1.criar_dados())
