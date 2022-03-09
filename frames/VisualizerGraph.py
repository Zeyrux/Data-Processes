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
from frames.ChangeCalculation import CalculationChangerTwoAx
from lib.Options import OPTIONS_WITH_TYPE


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=9, height=7, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)


class VisualizerGraph(QMainWindow):
    cur_data_x = None
    cur_data_y = None
    change_state_calcu = None

    def __init__(self, calculation_ref: CalculationChangerTwoAx = None):
        super().__init__()
        self.graph = Canvas(self)

        self.calcu_ref = calculation_ref

        self.book = read_database(copy_data=False)
        self.graph.fig.set_facecolor("#444")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graph)
        self.layout.addWidget(NavigationToolbar(self.graph, self))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def set_ref_calcu(self, calcu_ref: CalculationChangerTwoAx):
        self.calcu_ref = calcu_ref

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
            plot_data_x.append(self.calcu_ref.calcu_x.calcu.calculation(
                data_x)
            )
            data_y: np.ndarray = screenshot.filter_name(info_y)
            plot_data_y.append(self.calcu_ref.calcu_x.calcu.calculation(
                data_y)
            )

            last_date = date
        self.graph.ax.scatter(plot_data_x, plot_data_y)
        self.graph.figure.canvas.draw()

    def change_graph_x(self, new_data=None, new_calcu=None, plot=True):
        if new_data is not None:
            self.cur_data_x = new_data
        if new_calcu is not None:
            self.calcu_ref.calcu_x.calcu.new_calculation_name = new_calcu
        if plot:
            self.start_plot()

    def change_graph_y(self, new_data=None, new_calcu=None, plot=True):
        if new_data is not None:
            self.cur_data_y = new_data
        if new_calcu is not None:
            self.calcu_ref.calcu_y.calcu.new_calculation_name = new_calcu
        if plot:
            self.start_plot()

    def start_plot(self):
        if self.cur_data_x is not None \
                and self.cur_data_y is not None:
            self.calcu_ref.calcu_x.change_state(
                OPTIONS_WITH_TYPE.get(self.cur_data_x)
            )
            self.calcu_ref.calcu_y.change_state(
                OPTIONS_WITH_TYPE.get(self.cur_data_y)
            )

            self.calcu_ref.calcu_x.calcu.calculation = \
                self.calcu_x.get_change_calcu(self.cur_data_x)
            self.calcu_ref.calcu_y.calcu.calculation = \
                self.calcu_y.get_change_calcu(self.cur_data_y)

            Thread(
                target=self.plot,
                args=(self.cur_data_x, self.cur_data_y,),
                daemon=True
            ).start()

# https://www.w3schools.com/python/matplotlib_scatter.asp
