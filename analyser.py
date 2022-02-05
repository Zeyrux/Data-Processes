import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QGridLayout,
    QVBoxLayout,
    QWidget
)

from lib.style import Style
from lib.CustomWidgets import CustomPushButton

OPTIONS_SELF = [
    "date",
    "finished in"
]
OPTIONS_GEN = [
    "connections",
    "cpu_affinity",
    "cpu_percent",
    "cpu_times",
    "create_time",
    "cwd",
    "exe",
    "io_counters",
    "ionice",
    "memory_full_info",
    "memory_percent",
    "name",
    "nice",
    "num_ctx_switches",
    "num_handles",
    "num_threads",
    "pid",
    "ppid",
    "status",
    "threads",
    "username"
]

STYLE = "Fusion"
STYLE_Q_PUSH_BUTTON = open("styles\\QPushButton.css", "r").read()
STYLE_Q_MAIN_WINDOW = open("styles\\QMainWindow.css", "r").read()


class MainWindow(QMainWindow):
    count_button_clicked = 0

    def __init__(self):
        super().__init__()

        self.stylesheet = Style([
            STYLE_Q_MAIN_WINDOW,
            STYLE_Q_PUSH_BUTTON
        ])
        self.setStyleSheet(self.stylesheet.style)

        self.layout_buttons = QGridLayout()
        for i in range(0, len(OPTIONS_GEN), 3):
            self.layout_buttons.addWidget(CustomPushButton(
                text=OPTIONS_GEN[i],
                checkable=True,
                button_click=self.button_click), i // 3, 0
            )
            self.layout_buttons.addWidget(CustomPushButton(
                text=OPTIONS_GEN[i+1],
                checkable=True,
                button_click=self.button_click), i // 3, 1
            )
            self.layout_buttons.addWidget(CustomPushButton(
                text=OPTIONS_GEN[i+2],
                checkable=True,
                button_click=self.button_click), i // 3, 2
            )
        self.widget_buttons = QWidget()
        self.widget_buttons.setLayout(self.layout_buttons)

        self.layout = QVBoxLayout()
        self.layout.addWidget(CustomPushButton(
            text=OPTIONS_SELF[0], checkable=True))
        self.layout.addWidget(CustomPushButton(
            text=OPTIONS_SELF[1], checkable=True))
        self.layout.addWidget(self.widget_buttons)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def button_click(self):
        self.count_button_clicked += 1
        print("hi")
        print("2")


app = QApplication(sys.argv)
app.setStyle(STYLE)

window = MainWindow()
window.show()

app.exec()
