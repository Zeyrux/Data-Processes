from datetime import datetime
import os
import time
import psutil
import threading

DATABASE_PATH = os.path.join("C:\\Zeyrux\\Database", "database.txt")

IMPORTANT = [
    "connections",
    "cpu_affinity",
    "cpu_percent",
    "cpu_times",
    "create_time",
    "cwd",
    "exe",
    "io_counters",
    "ionice",
    "memory_full_info",
    "memory_percent",
    "name",
    "nice",
    "num_ctx_switches",
    "num_handles",
    "num_threads",
    "pid",
    "ppid",
    "status",
    "threads",
    "username"
]

SOMETHING_BETWEEN = [
    "environ",
    "memory_maps", # gibt sehr viel inforamtionene, aber auch sehr sehr lang
    "open_files" # gibt alle geöffnete dateien an, aber viel speicher
]


UNIMPORTANT = [
    "cmdline",
    "memory_info"
]


def save():
    timer = time.time_ns()
    with open(DATABASE_PATH, "ab") as f:
        f.write("\n#NEW_INPUT#\n".encode())
        f.write(f"date: {str(datetime.now())}\n".encode())
        for proc in psutil.process_iter():
            f.write((str(proc.as_dict(attrs=IMPORTANT)) + "\n").encode())
        end_time = (time.time_ns()-timer) / 1_000_000_000
        f.write(
            f"finished in: {end_time}\n".encode()
        )
        print(f"finished in: {end_time}")


def main():
    while True:
        threading.Thread(target=save, daemon=True).start()
        time.sleep(60)


if __name__ == "__main__":
    main()
