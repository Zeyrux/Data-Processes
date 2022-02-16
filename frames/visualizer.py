import pyqtgraph as pg
from PyQt6.QtWidgets import (
    QMainWindow
)

from lib.Options import OPTIONS_GEN
from lib.database import read_database
# https://pyqtgraph.readthedocs.io/en/latest/how_to_use.html
# https://www.pythonguis.com/tutorials/plotting-pyqtgraph/


class Visualizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graph = pg.PlotWidget()

        self.setCentralWidget(self.graph)

    def change(self, new_data: str):
        new_data = OPTIONS_GEN[int(new_data)]
