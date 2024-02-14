from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
from csv_ import File



class TotalWindow(QWidget):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.file = File()

        # Configurações
        self.setWindowTitle(f"Total")
        layout = QGridLayout()
        self.setLayout(layout)

        # Widgets da janela
        self.value = QLabel(self.file.total())

        # Configurações dos widgets

        # Conexões

        # Adicionar ao layout
        layout.addWidget(self.value)

        self.resize(450, 100)
