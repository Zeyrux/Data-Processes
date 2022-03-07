from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit
)
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

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
        self.inp_cnt_string = QLineEdit()
        self.inp_cnt_string.keyReleaseEvent = self.cnt_string_key_release
        self.inp_cnt_string.setPlaceholderText("string to count")

        self.button_average.click()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_max)
        self.layout.addWidget(self.button_average)
        self.layout.addWidget(self.button_min)
        self.layout.addWidget(self.button_add_all)
        self.layout.addWidget(self.inp_cnt_string)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def cnt_string_key_release(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.change_calcu_func(self.get_cur_aktiv_button().objectName())

    def get_cur_aktiv_button(self):
        if self.button_min.isChecked():
            return self.button_min
        if self.button_average.isChecked():
            return self.button_average
        if self.button_max.isChecked():
            return self.button_max
        if self.button_add_all.isChecked():
            return self.button_add_all

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
