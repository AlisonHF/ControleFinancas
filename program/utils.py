from PySide6.QtWidgets import QPushButton
from datetime import datetime
from pathlib import Path

ROOT_DIR: Path = Path(__file__).parent
FILES_DIR: Path = ROOT_DIR / 'files'
WINDOW_ICON_PATH: Path = FILES_DIR / 'icone.png'

date: datetime = datetime.now()
currentDate: str = datetime.strftime(date , '%d/%m/%Y')


def connectClicked(button: QPushButton, func) -> None:
    button.clicked.connect(func)

def valueName(name: str, value: str):
    valid = True
    name = name
    value = value
    
    if name == '' or value == '':
        valid = False
        return valid
    return valid

def checkNum(num: str | float) -> bool:
    valid: bool = True
    num = num

    try:
        num = float(num)
    except ValueError:
        valid: bool = False
        return valid
    
    return valid

def checkIndex(index: str | float) -> bool:
    valid: bool = True
    try:
        index = int(index)
    except ValueError:
        valid = False
        return valid
    return valid
