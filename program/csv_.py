from pathlib import Path
import csv
import shutil
from windowsW import WindowError



class File():

    def __init__(self) -> None:
        self.path = Path.cwd() / f'Extrato.csv'
        self.fieldNames = ['Arquivo', 'Data', 'Nome', 'Valor']

    def create(self, path: Path) -> None:
        if not path.exists():
            with open(path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldNames)
                writer.writeheader()

    def add(self, data: dict| list[dict]) -> None:
        if not self.path.exists():
            self.create(self.path)
        
        with open(self.path, 'a', newline='') as file:
            escritor = csv.DictWriter(file, fieldnames=self.fieldNames)
            for valor in data:
                escritor.writerow(valor)

    def view(self) -> str | None:
        planilha: str = ''

        if not self.path.exists():
            self.showError('Arquivo não existente para ler!')

        else:
            with open(self.path, 'r') as file:
                reader = csv.DictReader(file)

                for index, line in enumerate(reader):
                    planilha += f'{index + 1} - {line["Data"]} {line["Nome"]} { line["Valor"]}\n'

                return planilha
            
    def remove(self, indexToRemove: int) -> None:
        indexToRemove -= 1
        if not self.path.exists():
            self.showError('Arquivo não existente para ler!')
        else:
            with open(self.path, 'r') as arquivo:
                new_lines: list = []
                reader = csv.DictReader(arquivo)

                for currIndex, line in enumerate(reader):
                    if currIndex != indexToRemove:
                        new_lines.append(line)

            self.path.unlink()

            with open(self.path, 'w', newline='') as novo_arquivo:
                writer = csv.DictWriter(novo_arquivo, fieldnames=self.fieldNames)
                writer.writeheader()
                writer.writerows(new_lines)


    def total(self) -> str | None:
        if not self.path.exists():
            self.showError('Arquivo não existente para ler!')

        else:
            total = 0
            with open(self.path, 'r') as arquivo:
                reader = csv.DictReader(arquivo)

                for linha in reader:
                    if linha['Valor']:
                        valueString= linha['Valor'].replace('R$', '')
                        amount = valueString.replace(' ', '')
                        amount = float(amount)
                        total += amount
                        
            return f'Total: R$ {total:.2f}'
        
    def saveCopy(self) -> None:
        if not self.path.exists():
            print('Arquivo não existente para copiar!')

        else:
            destiny: Path = Path.home() / 'Desktop' / 'Extrato.csv' 
            shutil.copy(self.path, destiny)
            print('Arquivo salvado com sucesso!')

    def showError(self, msg: str) -> None:
        self.windowError = WindowError(msg)
        self.windowError.show()
