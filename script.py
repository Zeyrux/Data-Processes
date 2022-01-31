import os







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