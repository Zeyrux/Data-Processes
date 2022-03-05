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

from lib.database import read_database
from lib.Calculation import change_calcu


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=6, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)


class VisualizerGraph(QMainWindow):

    calculation_x = None
    calculation_y = None
    calculation_x_name = None
    calculation_y_name = None
    cur_data_x = None
    cur_data_y = None

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

    def plot(self, info_x: str, info_y: str):
        self.graph.ax.cla()
        self.graph.ax.set_xlabel(info_x)
        self.graph.ax.set_ylabel(info_y)
        plot_data_x = []
        plot_data_y = []
        last_date = pd.to_datetime("2000-01-01 00:00:00")
        for i, screenshot in enumerate(self.book.proc_screenshots):
            date = pd.to_datetime(screenshot.date)
            if (date - last_date).total_seconds() > 61:
                self.graph.ax.scatter(plot_data_x, plot_data_y)
                plot_data_x = []
                plot_data_y = []
            if i % 100 == 99:
                self.graph.figure.canvas.draw()

            data_x: np.ndarray = screenshot.filter_name(info_x)
            plot_data_x.append(self.calculation_x(data_x))
            data_y: np.ndarray = screenshot.filter_name(info_y)
            plot_data_y.append(self.calculation_y(data_y))

            last_date = date
        self.graph.ax.scatter(plot_data_x, plot_data_y)
        self.graph.figure.canvas.draw()

    def change_graph_x(self, new_data=None, new_calcu=None):
        if new_data is not None:
            self.cur_data_x = new_data
        if new_calcu is not None:
            self.calculation_x_name = new_calcu
        self.start_plot()

    def change_graph_y(self, new_data=None, new_calcu=None):
        if new_data is not None:
            self.cur_data_y = new_data
        if new_calcu is not None:
            self.calculation_y_name = new_calcu
        self.start_plot()

    def start_plot(self):
        if self.cur_data_x is not None \
                and self.cur_data_y is not None:
            self.calculation_x = change_calcu(
                self.cur_data_x,
                self.calculation_x_name
            )
            self.calculation_y = change_calcu(
                self.cur_data_y,
                self.calculation_y_name
            )
            Thread(
                target=self.plot,
                args=(self.cur_data_x, self.cur_data_y,),
                daemon=True
            ).start()
        pass


# https://www.w3schools.com/python/matplotlib_scatter.asp
