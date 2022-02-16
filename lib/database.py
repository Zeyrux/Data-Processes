import os
import shutil
import pathlib
import numpy as np

DATABASE_PATH_ORI = os.path.join("C:\\Zeyrux\\Database", "database.data")
DATABASE_DIR_COPY = "C:\\Zeyrux\\Database\\Analyse"
DATABASE_PATH_COPY = os.path.join(DATABASE_DIR_COPY, "database_copy.data")


class Info:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __str__(self):
        return f"name: {self.name}; " \
               f"value: {self.value}"


class Process:
    def __init__(self, info: list = None):
        if info is None:
            info = []
        self.info = info

    def add_info(self, info: Info):
        self.info.append(info)

    def remove_info(self, index):
        del self.info[index]

    def save(self, process_screenshot: "ProcessScreenshot"):
        self.info = np.array(self.info)
        process_screenshot.add_proc(self)

    def filter_name(self, name: str) -> str:
        for info in self.info:
            if info.name == name:
                return info.value
        return ""

    def filter_value(self, value: str) -> np.ndarray:
        names = []
        for info in self.info:
            if info.value == value:
                names.append(info.name)
        return np.array(names, dtype=str)

    def __len__(self):
        return len(self.info)

    def __str__(self):
        return f"len: {self.__len__()}"


class ProcessScreenshot:
    def __init__(
            self,
            date="undef",
            finished_in: float = None,
            processes: list = None
    ):
        if processes is None:
            processes = []
        if finished_in is None:
            finished_in = -1
        self.date = date
        self.finished_in = finished_in
        self.processes = processes

    def add_proc(self, proc: Process):
        self.processes.append(proc)

    def remove_proc(self, index):
        del self.processes[index]

    def save(self, process_screenshot_book: "ProcessScreenshotBook"):
        self.processes = np.array(self.processes)
        process_screenshot_book.add_proc_screenshot(self)

    def filter_name(self, name: str) -> np.ndarray:
        values = []
        for proc in self.processes:
            proc_ret = proc.filter_name(name)
            if not proc_ret == "":
                values.append(proc_ret)
        return np.array(values, dtype=str)

    def filter_value(self, value: str) -> np.ndarray:
        names = []
        for proc in self.processes:
            proc_ret = proc.filter_value(value)
            if len(proc_ret) != 0:
                names.append(proc_ret)
        return np.array(names, dtype=object)

    def __len__(self):
        return len(self.processes)

    def __str__(self):
        return f"date: {self.name}; " \
               f"len: {self.__len__()}"


class ProcessScreenshotBook:
    def __init__(self, proc_screenshots: list=None):
        if proc_screenshots is None:
            proc_screenshots = []
        self.proc_screenshots = proc_screenshots

    def add_proc_screenshot(self, proc_screenshot: ProcessScreenshot):
        self.proc_screenshots.append(proc_screenshot)

    def remove_proc_screenshot(self, index):
        del self.proc_screenshots[index]

    def __len__(self):
        return len(self.proc_screenshots)

    def __str__(self):
        return f"len: {self.__len__()}"


def empty():
    pass


def copy_database():
    if not os.path.isdir(DATABASE_DIR_COPY):
        pathlib.Path(DATABASE_DIR_COPY).mkdir(
            parents=True,
            exist_ok=True
        )
    shutil.copy(DATABASE_PATH_ORI, DATABASE_PATH_COPY)


def read_database(
        copy_data=True,
        progress_func=empty
) -> ProcessScreenshotBook:
    # copy database
    if copy_data:
        copy_database()
    # read database
    proc_screenshot_book = ProcessScreenshotBook()
    with open(DATABASE_PATH_COPY, "rb") as f:
        cnt_inputs = 0
        proc_screenshot: ProcessScreenshot = None
        date: str
        finished_in: float
        for line in f:
            line = line.decode()
            line = line.replace("\n", "")
            # jump to next line
            if line == "":
                continue
            # save date and create new ProcessScreenshot
            elif line[0:4] == "date":
                if proc_screenshot is not None:
                    proc_screenshot.save(proc_screenshot_book)
                proc_screenshot = ProcessScreenshot()
                proc_screenshot.date = line[6:len(line)]
                cnt_inputs += 1
                progress_func()
                continue
            # save finished in
            elif line[0:11] == "finished in":
                proc_screenshot.finished_in = float(line[13:len(line)])
                continue
            # save processes
            else:
                proc = Process()
                line = line.split(";")
                for info in line:
                    info = info.split("#")
                    proc.add_info(Info(
                        info[0],
                        info[1]
                    ))
                proc.save(proc_screenshot)
    return proc_screenshot_book
