import os
import time

timer = time.time_ns()
os.system("g++ test.cpp")
print(f"BUILD SUCCESSFULLY: {(time.time_ns()- timer) / 1_000_000_000}\n\n")
timer = time.time_ns()
os.system("a.exe")
print(f"\n\nTIME: {(time.time_ns()- timer) / 1_000_000_000}")



important = [
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

eventuell = [
    "environ",
    "memory_maps", # gibt sehr viel inforamtionene, aber auch sehr sehr lang
    "open_files" # gibt alle geöffnete dateien an, aber viel speicher
]


unimportant = [
    "cmdline",
    "memory_info"
]