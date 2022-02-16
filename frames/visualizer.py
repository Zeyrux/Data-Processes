import pyqtgraph as pg
import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow
)

from lib.Options import OPTIONS_GEN
from lib.database import (
    read_database,
    ProcessScreenshotBook,
    ProcessScreenshot,
    Process,
    Info
)
# https://pyqtgraph.readthedocs.io/en/latest/how_to_use.html
# https://www.pythonguis.com/tutorials/plotting-pyqtgraph/

# dateteim:
# https://stackoverflow.com/questions/29385868/plotting-datetime-objects-with-pyqtgraph

def average(array: np.ndarray | list):
    result = 0
    for element in array:
        result += element
    return result / len(array)


class Visualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        book = read_database()
        self.graph = pg.PlotWidget()

        dates = []
        averages = []
        for i, screenshot in enumerate(book.proc_screenshots):
            data = screenshot.filter_value("None")
            averages.append(len(data))
            dates.append(60*i)
        self.graph.plot(dates, averages)

        axis = pg.DateAxisItem()
        self.graph.setAxisItems({"bottom": axis})
        self.graph.setLabel("left", "cnt None", "")

        self.setCentralWidget(self.graph)

    def change(self, new_data: str):
        new_data = OPTIONS_GEN[int(new_data)]
