from PyQt6.QtWidgets import (
    QPushButton,
    QRadioButton
)


def empty():
    pass


# class CustomPushButton(QPushButton):
#     is_checked = False
#
#     def __init__(
#             self,
#             text="",
#             checkable=False,
#             button_click=empty,
#             on_click_name_para=False,
#             name=""
#     ):
#         super().__init__(text)
#         self.setObjectName(name)
#         self.setCheckable(checkable)
#         if on_click_name_para:
#             self.clicked.connect(lambda: button_click(name))
#         else:
#             self.clicked.connect(button_click)


class CustomRationButton(QRadioButton):
    def __init__(
            self,
            clicked=empty,
            name=""
    ):
        super().__init__(name)
        self.setObjectName(name)
        self.clicked.connect(lambda: clicked(self))
