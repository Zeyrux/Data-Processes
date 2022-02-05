import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget
)

from lib.style import Style
from lib.CustomWidgets import CustomPushButton

OPTIONS_SELF = [
    "date:",
    "finished in:"
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
    def __init__(self):
        super().__init__()

        self.stylesheet = Style([
            STYLE_Q_MAIN_WINDOW,
            STYLE_Q_PUSH_BUTTON
        ])
        self.setStyleSheet(self.stylesheet.style)

        self.layout_buttons = QGridLayout()
        for i in range(0, len(OPTIONS_GEN), 3):
            self.layout_buttons.addWidget(
                CustomPushButton(OPTIONS_GEN[i], checkable=True), i // 3, 0
            )
            self.layout_buttons.addWidget(
                CustomPushButton(OPTIONS_GEN[i+1], checkable=True), i // 3, 1
            )
            self.layout_buttons.addWidget(
                CustomPushButton(OPTIONS_GEN[i+2], checkable=True), i // 3, 2
            )
        self.widget = QWidget()
        self.widget.setLayout(self.layout_buttons)
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
app.setStyle(STYLE)

window = MainWindow()
window.show()

app.exec()
