from PyQt6.QtWidgets import (
    QGridLayout,
    QMainWindow,
    QWidget
)

from lib.style import Style
from lib.CustomWidgets import CustomPushButton
from lib.Options import OPTIONS_GEN


class ChangeVisualisation(QMainWindow):
    def __init__(self, style: Style, change_visu_func):
        super().__init__()

        self.setStyleSheet(style.style)

        self.layout = QGridLayout()
        for i in range(0, len(OPTIONS_GEN), 3):
            self.layout.addWidget(CustomPushButton(
                    text=OPTIONS_GEN[i],
                    button_click=change_visu_func,
                    on_click_name_para=True,
                    name=str(i))
                , i // 3, 0
            )
            self.layout.addWidget(CustomPushButton(
                    text=OPTIONS_GEN[i + 1],
                    button_click=change_visu_func,
                    on_click_name_para=True,
                    name=str(i + 1))
                , i // 3, 1
            )
            self.layout.addWidget(CustomPushButton(
                    text=OPTIONS_GEN[i + 2],
                    button_click=change_visu_func,
                    on_click_name_para=True,
                    name=str(i + 2))
                , i // 3, 2
            )

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
