import numpy as np
import pandas as pd

from lib.Options import OPTIONS_WITH_TYPE


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


# date
def date(data: np.ndarray) -> pd.Timestamp:
    return pd.to_datetime(data[0])


# string
def count_string(data: np.ndarray, cnt_string: str):
    cnt = 0
    for element in data:
        if element == cnt_string:
            cnt += 1
    return cnt


# calculation
def change_calcu(data: str, new_calcu: str):
    new_calcu = new_calcu.lower()
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
    if OPTIONS_WITH_TYPE.get(data) == "date":
        return date
    if OPTIONS_WITH_TYPE.get(data) == "string":
        return count_string
