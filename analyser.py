import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget
)

from lib.style import Style
from frames.changer import ChangeVisualisation
from frames.visualizer import Visualizer

STYLE = "Fusion"
STYLE_Q_PUSH_BUTTON = open("styles\\QPushButton.css", "r").read()
STYLE_Q_MAIN_WINDOW = open("styles\\QMainWindow.css", "r").read()


window: "MainWindow" = None


class MainWindow(QMainWindow):
    count_button_clicked = 0

    def __init__(self):
        super().__init__()

        self.style = Style([
            STYLE_Q_MAIN_WINDOW
        ])
        self.setStyleSheet(self.style.style)

        self.layout = QVBoxLayout()
        self.change = ChangeVisualisation(Style([
            STYLE_Q_MAIN_WINDOW,
            STYLE_Q_PUSH_BUTTON
        ]), self.change_visualization)
        self.visualizer = Visualizer()
        self.layout.addWidget(self.visualizer)
        self.layout.addWidget(self.change)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def change_visualization(self, new_data: str):
        self.visualizer.change(new_data)


def main():
    global window
    app = QApplication(sys.argv)
    app.setStyle(STYLE)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    # main()
    from lib.database import read_database, copy_database
    # copy_database()
    book = read_database(copy_data=False)
    print(book.proc_screenshots[0].filter_name("name"))

