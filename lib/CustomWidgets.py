from PyQt6.QtWidgets import (
    QPushButton
)
from PyQt6.QtGui import QMouseEvent


def empty():
    pass


class CustomPushButton(QPushButton):
    is_checked = False

    def __init__(
            self,
            text="",
            checkable=False,
            button_click=empty
    ):
        super().__init__(text)
        self.setCheckable(checkable)
        self.clicked.connect(button_click)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.is_checked = False if self.is_checked else True
