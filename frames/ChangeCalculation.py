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

from lib.Calculation import Calclation
from lib.CustomWidgets import CustomRationButton
from lib.style import Style


class CalculationChangerNumbers(QMainWindow):

    enabled = False

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

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_max)
        self.layout.addWidget(self.button_average)
        self.layout.addWidget(self.button_min)
        self.layout.addWidget(self.button_add_all)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def clicked(self, super: CustomRationButton, plot=True):
        self.change_calcu_func(super.objectName(), plot)

    def get_cur_aktiv_button(self):
        if self.button_min.isChecked():
            return self.button_min
        if self.button_average.isChecked():
            return self.button_average
        if self.button_max.isChecked():
            return self.button_max
        if self.button_add_all.isChecked():
            return self.button_add_all

    def enable(self):
        if not self.enabled:
            self.button_average.setChecked(True)
            self.change_calcu_func(self.button_average.objectName(), False)
            self.enabled = True


class CalculationChangerStrings(QMainWindow):

    enabled = False

    def __init__(self, change_calcu_func):
        super().__init__()
        self.change_calcu_func = change_calcu_func

        self.button_cnt_string = CustomRationButton(
            clicked=self.clicked,
            name="Count Strings"
        )

        self.inp_string = QLineEdit()
        self.inp_string.keyReleaseEvent = self.cnt_string_key_release
        self.inp_string.setPlaceholderText("string to count")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_cnt_string)
        self.layout.addWidget(self.inp_string)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def cnt_string_key_release(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.change_calcu_func(self.get_cur_aktiv_button().objectName())

    def clicked(self, super: CustomRationButton):
        self.change_calcu_func(super.objectName())

    def get_cur_aktiv_button(self) -> CustomRationButton:
        if self.button_cnt_string.isChecked():
            return self.button_cnt_string

    def enable(self):
        if not self.enabled:
            self.button_cnt_string.setChecked(True)
            self.change_calcu_func(self.button_cnt_string.objectName(), False)
            self.enabled = True


class CalculationChangerDates(QMainWindow):

    enabled = False

    def __init__(self, change_calcu_func):
        super().__init__()
        self.change_calcu_func = change_calcu_func

    def enable(self):
        if not self.enabled:
            self.enabled = True


class CalculationChanger(QMainWindow):
    def __init__(self, change_calcu_func, init_state="float"):
        super().__init__()

        self.state = init_state
        self.calcu = Calclation(self)

        self.widget_numbers = CalculationChangerNumbers(change_calcu_func)
        self.widget_strings = CalculationChangerStrings(change_calcu_func)
        self.widget_dates = CalculationChangerDates(change_calcu_func)

        self.widget = QWidget()
        self.change_state(self.state)
        self.setCentralWidget(self.widget)

    def change_state(self, state: str):
        self.state = state.lower()
        if state == "float" or state == "int":
            self.widget = self.widget_numbers
        elif state == "string":
            self.widget = self.widget_strings
        elif state == "date":
            self.widget = self.widget_dates
        self.widget.enable()
        self.setCentralWidget(self.widget)
        self.centralWidget().update()


class CalculationChangerTwoAx(QMainWindow):
    def __init__(self, style: Style, change_calcu_x, change_calcu_y, visualizer):
        super().__init__()
        visualizer.set_ref_calcu(self)

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
