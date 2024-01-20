from pathlib import Path
import csv
import shutil

class Arquivo():

    def __init__(self) -> None:
        self.caminho = Path.cwd() / f'Extrato.csv'

    def criar(self, caminho: Path):
        if not caminho.exists():
            with open(caminho, 'w', newline='') as arquivo:
                nome_colunas = ['Data', 'Nome', 'Valor']
                escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
                escritor.writeheader()

    def adicionar(self, dados : list) -> None:
        if not self.caminho.exists():
            self.criar(self.caminho)
        
        with open(self.caminho, 'a') as arquivo:
            nome_colunas = ['Data', 'Nome', 'Valor']
            escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
            for valor in dados:
                escritor.writerow(valor)

    def visualizar(self) -> None:
        if not self.caminho.exists():
            print('Arquivo não existente para ler!')

        else:
            with open(self.caminho, 'r') as arquivo:
                leitor = csv.DictReader(arquivo)

                for linha in leitor:
                    print(linha['Data'], linha['Nome'], linha['Valor'])
                    print()

    def total(self) -> str:
        if not self.caminho.exists():
            print('Arquivo não existente para ler!')

        else:
            total = 0
            with open(self.caminho, 'r') as arquivo:
                leitor = csv.DictReader(arquivo)

                for linha in leitor:
                    if linha['Valor']:
                        valor_string= linha['Valor'].replace('R$', '')
                        valor_bruto = valor_string.replace(' ', '')
                        valor_bruto = float(valor_bruto)
                        total += valor_bruto
                        
            return f'Total: R$ {total:.2f}'
        
    def salvar_copia(self) -> None:
        if not self.caminho.exists():
            print('Arquivo não existente para copiar!')

        else:
            destino = Path.home() / 'Desktop' / 'Extrato.csv' 
            shutil.copy(self.caminho, destino)
            print('Arquivo salvado com sucesso!')



if __name__ == '__main__':
    print('Arquivo CSV')
    arquivo1 = Arquivo()
    gasto1 = [{'Data' : '22/09/2001', 'Nome' : 'Gasto1', 'Valor' : 'R$ 5000.00'},
          {'Data' : '23/09/2001', 'Nome' : 'Gasto2', 'Valor' : 'R$ 4000.00'}]
    arquivo1.adicionar(gasto1)

