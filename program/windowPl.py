from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
from csv_ import File



class SpreadsheetWindow(QWidget):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurações
        self.setWindowTitle(f"Planilha")
        layout = QGridLayout()
        self.setLayout(layout)
        self.file = File()

        # Widgets da janela
        self.value = QLabel(self.file.view())

        # Configurações dos widgets

        # Conexões

        # Adicionar ao layout
        layout.addWidget(self.value)

        self.resize(450, 100)
