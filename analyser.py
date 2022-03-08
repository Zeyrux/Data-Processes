import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget
)

from lib.style import Style
from frames.ChangeVisualisation import ChangeVisualisationTwoAx
from frames.VisualizerGraph import VisualizerGraph
from frames.ChangeCalculation import CalculationChangerTwoAx

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

        # change visualisation
        change_visu_style = Style([
            STYLE_Q_MAIN_WINDOW
        ])

        # change calculation
        change_calcu_style = Style([
            STYLE_Q_MAIN_WINDOW
        ])

        self.visualizer = VisualizerGraph()
        self.change_calcu = CalculationChangerTwoAx(
            change_calcu_style,
            self.change_calculation_x,
            self.change_calculation_y
        )
        self.change_visu = ChangeVisualisationTwoAx(
            change_visu_style,
            self.change_visualization_x,
            self.change_visualization_y
        )

        self.visualizer.set_ref_change_calcu(self.change_calcu)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.visualizer)
        self.layout.addWidget(self.change_calcu)
        self.layout.addWidget(self.change_visu)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def change_visualization_x(self, new_data: str):
        self.visualizer.change_graph_x(new_data=new_data)

    def change_visualization_y(self, new_data: str):
        self.visualizer.change_graph_y(new_data=new_data)

    def change_calculation_x(self, new_calcu: str, plot: bool):
        self.visualizer.change_graph_x(new_calcu=new_calcu, plot=plot)

    def change_calculation_y(self, new_calcu: str, plot: bool):
        self.visualizer.change_graph_y(new_calcu=new_calcu, plot=plot)


def main():
    global window
    app = QApplication(sys.argv)
    app.setStyle(STYLE)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
