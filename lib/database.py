import os
import shutil
import pathlib

from lib.Options import OPTIONS_GEN, OPTIONS_GEN_WITH_TYPE, Class

DATABASE_PATH_TO_COPY = os.path.join("C:\\Zeyrux\\Database", "database.txt")
DATABASE_DIR = "C:\\Zeyrux\\Database\\Analyse"
DATABASE_PATH = os.path.join(DATABASE_DIR, "database_copy.txt")


class Info:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __str__(self):
        return f"name: {self.name}; " \
               f"value: {self.value}"


class Process:
    def __init__(self, info=[]):
        self.info = info

    def add_info(self, info: Info):
        self.info.append(info)

    def remove_info(self, index):
        del self.info[index]

    def __len__(self):
        return len(self.info)

    def __str__(self):
        return f"len: {self.__len__()}"


class ProcessScreenshot:
    def __init__(self, date="undef", finished_in=-1., processes=[]):
        self.date = date
        self.finished_in = finished_in
        self.processes = processes

    def add_proc(self, proc: Process):
        self.processes.append(proc)

    def remove_proc(self, index):
        del self.processes[index]

    def save(self):
        print(self.date)

    def __len__(self):
        return len(self.processes)

    def __str__(self):
        return f"date: {self.name}; " \
               f"len: {self.__len__()}"


def copy_database():
    if not os.path.isdir(DATABASE_DIR):
        pathlib.Path(DATABASE_DIR).mkdir(
            parents=True,
            exist_ok=True
        )
    shutil.copy(DATABASE_PATH_TO_COPY, DATABASE_PATH)


def filter_line(line: str) -> Process:
    proc = Process()
    while True:
        cur_in = []

def write_all_info(copy_data=True):
    # copy database
    if copy_data:
        copy_database()
    # read database
    with open(DATABASE_PATH, "r") as f:
        cnt_inputs = 0
        proc_screenshot: ProcessScreenshot = None
        date: str
        finished_in: float
        writer = get_writer()
        for line in f:
            line = line.replace("\n", "")
            if line == "":
                continue
            elif line == "#NEW_INPUT#":
                cnt_inputs += 1
                if proc_screenshot is not None:
                    proc_screenshot.save()
                proc_screenshot = ProcessScreenshot()
                continue
            elif line[0:4] == "date":
                proc_screenshot.date = line[6:len(line)]
                continue
            elif line[0:11] == "finished in":
                proc_screenshot.finished_in = float(line[13:len(line)])
                continue
            else:
                proc_screenshot.add_proc(filter_line(line))


def get_writer() -> dict:
    writer = {}
    for inp in OPTIONS_GEN:
        writer[inp] = open(inp + ".txt", "w")
    return writer
