from PyQt6.QtWidgets import (
    QMainWindow,
    QComboBox,
    QGridLayout,
    QLabel,
    QWidget
)

from lib.style import Style
from lib.Options import OPTIONS


class ChangeVisualisation(QMainWindow):
    def __init__(self, change_visu_func):
        super().__init__()
        self.change_visu_func = change_visu_func

        self.box = QComboBox()
        for option in OPTIONS:
            self.box.addItem(option)
        self.box.currentTextChanged.connect(self.changed)

        self.setCentralWidget(self.box)

    def changed(self):
        self.change_visu_func(self.box.currentText())


class ChangeVisualisationTwoAx(QMainWindow):
    def __init__(self, style: Style, change_visu_x, change_visu_y):
        super().__init__()
        self.setStyleSheet(style.style)

        self.visu_x = ChangeVisualisation(change_visu_x)
        self.visu_y = ChangeVisualisation(change_visu_y)

        self.layout = QGridLayout()
        self.layout.addWidget(QLabel("X-Axes"), 0, 0)
        self.layout.addWidget(self.visu_x, 0, 1)
        self.layout.addWidget(QLabel("Y-Axes"), 1, 0)
        self.layout.addWidget(self.visu_y, 1, 1)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
