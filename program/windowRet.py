from PySide6.QtWidgets import (QWidget, QGridLayout, QLabel,
                               QLineEdit, QPushButton
)
from utils import checkIndex, connectClicked
from csv_ import File
from windowsW import WindowError, WindowDialog


        
class JanelaRetirar(QWidget):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Configurações
        self.setWindowTitle(f"Retirar")
        layout = QGridLayout()
        self.setLayout(layout)
        self.file = File()

        # Widgets da janela
        self.textToAdd = QLabel('Índice do gasto:')
        self.displayIndex = QLineEdit()
        self.confirmed = QPushButton('Confirmar')

        # Configurações dos widgets

        # Conexões
        connectClicked(self.confirmed, lambda: self.withDrawExpense())

        # Adicionar ao layout
        layout.addWidget(self.textToAdd, 0, 0)
        layout.addWidget(self.displayIndex, 0, 1)
        layout.addWidget(self.confirmed, 1, 1)

        self.resize(450, 100)

    def withDrawExpense(self) -> None:
        i: str = self.displayIndex.text()
        self.displayIndex.clear()
        checagem: bool = checkIndex(i)
        
        if not checagem:
            self.showError('Índice inválido!')
        else:
            self.file.remove(int(i))
            self.showDialog('Índice removido com sucesso!')

    def showError(self, msg: str) -> None:
        self.windowError = WindowError(msg)
        self.windowError.show()

    def showDialog(self, msg: str) -> None:
        self.windowError = WindowDialog(msg)
        self.windowError.show()
