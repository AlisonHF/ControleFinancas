from PySide6.QtWidgets import (QMainWindow, QPushButton,
                               QGridLayout, QWidget
)
from windowAdd import AddWindow
from windowRet import JanelaRetirar
from windowTot import TotalWindow
from windowPl import SpreadsheetWindow
from utils import connectClicked



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurações
        self.cw: QWidget = QWidget()
        self.gLayout: QGridLayout = QGridLayout()
        self.cw.setLayout(self.gLayout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle("Finanças")
        self.setFixedSize(1000, 300)
        
        # Widgets da janela
        self.buttonAdd = QPushButton('Adicionar gastos')
        self.buttonRet = QPushButton('Retirar gastos')
        self.buttonTot = QPushButton('Total dos gastos')
        self.buttonPl = QPushButton('Planilha completa')

        # Configurações dos widgets
        self.buttonAdd.setMinimumSize(900, 70)
        self.buttonRet.setMinimumSize(900, 70)
        self.buttonTot.setMinimumSize(900, 70)
        self.buttonPl.setMinimumSize(900, 70)

        # Conexões
        connectClicked(self.buttonAdd, self.openWindow1)
        connectClicked(self.buttonRet, self.openWindow2)
        connectClicked(self.buttonTot, self.openWindow3)
        connectClicked(self.buttonPl, self.openWindow4)

        # Adicionar ao layout
        self.gLayout.addWidget(self.buttonAdd)
        self.gLayout.addWidget(self.buttonRet)
        self.gLayout.addWidget(self.buttonTot)
        self.gLayout.addWidget(self.buttonPl)
        

    # Funções para abrir janelas
    def openWindow1(self) -> None:
        self.thisWindow = AddWindow()
        self.thisWindow.show()


    def openWindow2(self) -> None:
        self.thisWindow = JanelaRetirar()
        self.thisWindow.show()
    

    def openWindow3(self) -> None:
        self.thisWindow = TotalWindow()
        self.thisWindow.show()


    def openWindow4(self) -> None:
        self.thisWindow = SpreadsheetWindow()
        self.thisWindow.show()
