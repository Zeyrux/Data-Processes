import numpy as np


def maximum(data: np.ndarray) -> float:
    return data.max()


def average(data: np.ndarray) -> float:
    result = 0
    for element in data:
        result += element
    return result / len(data)


def minimum(data: np.ndarray) -> float:
    return data.min()


def change_calcu(new_calcu: str):
    new_calcu = new_calcu.lower()
    if new_calcu == "maximum":
        return maximum
    elif new_calcu == "average":
        return average
    else:
        return minimum
