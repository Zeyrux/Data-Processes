from PyQt6.QtWidgets import (
    QPushButton
)


class CustomPushButton(QPushButton):
    def __init__(self, text, checkable=False):
        super().__init__(text)
        self.setCheckable(checkable)
