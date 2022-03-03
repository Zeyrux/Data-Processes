from __future__ import annotations
from threading import Thread

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout
)

from lib.Options import OPTIONS_GEN
from lib.database import read_database


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=6, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)


class Visualizer(QMainWindow):

    calculation = None
    cur_data = ""

    def __init__(self):
        super().__init__()
        self.graph = Canvas(self)

        self.book = read_database(copy_data=False)
        self.graph.fig.set_facecolor("#444")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graph)
        self.layout.addWidget(NavigationToolbar(self.graph, self))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def plot(self, info:  str):
        self.graph.ax.cla()
        dates = []
        plot_data = []
        last_date = pd.to_datetime("2000-01-01 00:00:00")
        for i, screenshot in enumerate(self.book.proc_screenshots):
            data: np.ndarray = screenshot.filter_name(info)
            data = data.astype(float)
            date = pd.to_datetime(screenshot.date)
            if (date - last_date).total_seconds() > 61:
                self.graph.ax.plot(dates, plot_data)
                dates = []
                plot_data = []
            plot_data.append(self.calculation(data))
            if i % 100 == 99:
                self.graph.figure.canvas.draw()
            dates.append(date)
            last_date = date
        self.graph.ax.plot(dates, plot_data)
        self.graph.figure.canvas.draw()

    def change_data(self, new_data: str):
        self.cur_data = new_data
        Thread(
            target=self.plot,
            args=(OPTIONS_GEN[int(new_data)],),
            daemon=True
        ).start()

    def change_calculation(self, new_calcu):
        self.calculation = new_calcu
        if self.cur_data != "":
            self.change_data(self.cur_data)


# https://www.w3schools.com/python/matplotlib_scatter.asp
