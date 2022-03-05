from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel
)

from lib.CustomWidgets import CustomRationButton
from lib.style import Style


class CalculationChanger(QMainWindow):
    def __init__(self, change_calcu_func):
        super().__init__()
        self.change_calcu_func = change_calcu_func

        self.button_max = CustomRationButton(
            clicked=self.clicked,
            name="Maximum"
        )
        self.button_average = CustomRationButton(
            clicked=self.clicked,
            name="Average"
        )
        self.button_min = CustomRationButton(
            clicked=self.clicked,
            name="Minimum"
        )
        self.button_add_all = CustomRationButton(
            clicked=self.clicked,
            name="Add All"
        )

        self.button_average.click()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_max)
        self.layout.addWidget(self.button_average)
        self.layout.addWidget(self.button_min)
        self.layout.addWidget(self.button_add_all)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def clicked(self, super: CustomRationButton):
        self.change_calcu_func(super.objectName())


class CalculationChangerTwoAx(QMainWindow):
    def __init__(self, style: Style, change_calcu_x, change_calcu_y):
        super().__init__()
        self.setStyleSheet(style.style)

        self.calcu_x = CalculationChanger(change_calcu_x)
        self.calcu_y = CalculationChanger(change_calcu_y)

        self.layout = QGridLayout()
        self.layout.addWidget(QLabel("X-Axes"), 0, 0)
        self.layout.addWidget(self.calcu_x, 1, 0)
        self.layout.addWidget(QLabel("Y-Axes"), 0, 1)
        self.layout.addWidget(self.calcu_y, 1, 1)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
