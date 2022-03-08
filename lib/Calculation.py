import time

import numpy as np
import pandas as pd

from lib.Options import OPTIONS_WITH_TYPE
from frames.ChangeCalculation import CalculationChanger


def check_dtpye(target: np.ndarray, dtype) -> bool:
    try:
        dtype(target[0])
        return True
    except ValueError:
        return False


# float
def maximum(data: np.ndarray) -> float:
    data = data.astype(float)
    return data.max()


def average(data: np.ndarray) -> float:
    data = data.astype(float)
    result = 0
    for element in data:
        result += element
    return result / len(data)


def minimum(data: np.ndarray) -> float:
    data = data.astype(float)
    return data.min()


def add_all(data: np.ndarray) -> float:
    data = data.astype(float)
    result = 0
    for element in data:
        result += element
    return result


# calculation
class Calclation:
    def __init__(self, ref_change_calcu: CalculationChanger = None):
        self.calculation = None
        self.new_calculation_name = None
        self.ref_change = ref_change_calcu

    def get_change_calcu(self, data: str):
        data = data.lower()
        new_calcu = self.new_calculation_name.lower()
        if OPTIONS_WITH_TYPE.get(data) == "int" \
                or OPTIONS_WITH_TYPE.get(data) == "float":
            if new_calcu == "maximum":
                return maximum
            elif new_calcu == "average":
                return average
            elif new_calcu == "minimum":
                return minimum
            elif new_calcu == "add_all":
                return add_all
        elif OPTIONS_WITH_TYPE.get(data) == "date":
            return self.date
        elif OPTIONS_WITH_TYPE.get(data) == "string":
            return self.count_string

    def set_ref_change(self, ref_change: CalculationChanger):
        self.ref_change = ref_change

    def count_string(self, data: np.ndarray):
        cnt_string = self.ref_change.widget_strings.inp_string.text()
        cnt = 0
        for element in data:
            if element == cnt_string:
                cnt += 1
        return cnt

    def date(self, data: np.ndarray) -> pd.Timestamp:
        if check_dtpye(data, float):
            data = data[2:]
            calcu = self.get_change_calcu("cpu_percent")
            return pd.to_datetime(calcu(data), unit="s")
        else:
            return pd.to_datetime(data[0])
