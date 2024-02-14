from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from utils import connectClicked



class WindowError(QWidget):
    def __init__(self, msg, parent=None) -> None:
        super().__init__(parent)
        
        # Configurações
        self.setWindowTitle('ERRO')
        layout = QGridLayout()
        self.setLayout(layout)

        # Widgets da janela
        self.msg = QLabel(msg)
        self.ok = QPushButton('Ok')

        # Configurações dos widgets
        
        # Conexões
        connectClicked(self.ok, self.close)

        # Adicionar ao layout
        layout.addWidget(self.msg, 0, 0)
        layout.addWidget(self.ok, 1, 1)
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())


class WindowDialog(QWidget):
    def __init__(self, msg, parent=None) -> None:
        super().__init__(parent)
        
        # Configurações
        self.setWindowTitle('AVISO')
        layout = QGridLayout()
        self.setLayout(layout)

        # Widgets da janela
        self.msg = QLabel(msg)
        self.ok = QPushButton('Ok')

        # Configurações dos widgets
        
        # Conexões
        connectClicked(self.ok, self.close)

        # Adicionar ao layout
        layout.addWidget(self.msg, 0, 0)
        layout.addWidget(self.ok, 1, 1)
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
