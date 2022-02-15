from datetime import datetime
import os
import time
import psutil
import threading

from lib.Options import OPTIONS_GEN

DATABASE_PATH = os.path.join("C:\\Zeyrux\\Database", "database.data")


def save():
    timer = time.time_ns()
    cur_time = "date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    with open(DATABASE_PATH, "ab") as f:
        f.write(cur_time.encode())
        for proc in psutil.process_iter():
            str_with_proc = ""
            proc = proc.as_dict(attrs=OPTIONS_GEN)
            for name, value in proc.items():
                str_with_proc += name + "#" + str(value) + ";"
            f.write((str_with_proc[0:len(str_with_proc)-1] + "\n").encode())
        f.write(("finished in: " + str((time.time_ns() - timer) / 1_000_000_000) + "\n").encode())


def main():
    while True:
        try:
            threading.Thread(target=save, daemon=True).start()
        except Exception as e:
            print(e)
        time.sleep(60)


if __name__ == "__main__":
    main()
