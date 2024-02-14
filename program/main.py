import sys
from pathlib import Path
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication)
from mainWindow import MainWindow
from utils import WINDOW_ICON_PATH



def set_icon(caminho: Path) -> None:
     icon = QIcon(str(caminho))
 
     icon.addFile('files/10298172.png', size=QSize(64, 64))
    
     window.setWindowIcon(icon)
    
     app.setWindowIcon(icon)
    
     if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                u'CompanyName.ProductName.SubProduct.VersionInformation')


app: QApplication = QApplication(sys.argv)
window: MainWindow = MainWindow()   
icon = set_icon(WINDOW_ICON_PATH)
print(WINDOW_ICON_PATH)
window.show()
sys.exit(app.exec_())
