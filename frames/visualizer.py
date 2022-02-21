from __future__ import annotations
import datetime

from matplotlib import pyplot as plt
import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget
)

from lib.Options import OPTIONS_GEN
from lib.database import (
    read_database,
    ProcessScreenshotBook,
    ProcessScreenshot,
    Process,
    Info
)


def average(array: np.ndarray | list):
    result = 0
    for element in array:
        result += element
    return result / len(array)


class Visualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        book = read_database(copy_data=False)
        dates = []
        averages = []
        for i, screenshot in enumerate(book.proc_screenshots):
            data = screenshot.filter_name("cpu_percent").astype(float)
            averages.append(average(data))
            dates.append(screenshot.date)
        plt.plot([0, 12, 421, 3], [34, 23, 52, 3])
        plt.show()
        self.setCentralWidget(QWidget())

    def change(self, new_data: str):
        new_data = OPTIONS_GEN[int(new_data)]
