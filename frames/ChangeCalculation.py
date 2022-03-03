from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from lib.CustomWidgets import CustomRationButton
from lib.Calculation import change_calcu


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

        self.button_average.click()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_max)
        self.layout.addWidget(self.button_average)
        self.layout.addWidget(self.button_min)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def clicked(self, super: CustomRationButton):
        self.change_calcu_func(change_calcu(super.objectName()))
