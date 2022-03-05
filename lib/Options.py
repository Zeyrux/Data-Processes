
class Class:
    def __init__(self, name: str, value_type: str):
        self.name = name
        self.value_type = value_type

    @classmethod
    def create_list(cls, value_type: str):
        return Class("list", value_type)


OPTIONS_SELF = [
    "date",
    "finished in"
]


OPTIONS = [
    "connections",
    "cpu_affinity",
    "cpu_percent",
    "cpu_times",
    "create_time",
    "cwd",
    "date",
    "exe",
    "finished_in",
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

OPTIONS_WITH_TYPE = {
    "connections": Class.create_list(Class("pconn", "string")),
    "cpu_affinity": Class.create_list("int"),
    "cpu_percent": "float",
    "cpu_times": Class("pcputimes", "float"),
    "create_time": "float",
    "cwd": "string",
    "date": "date",
    "exe": "string",
    "finished_in": "float",
    "io_counters": Class("pio", "int"),
    "ionice": "string",
    "memory_full_info": Class("pfullmem", "int"),
    "memory_percent": "float",
    "name": "string",
    "nice": "string",
    "num_ctx_switches": Class("pctxsw", "int"),
    "num_handles": "int",
    "num_threads": "int",
    "pid": "int",
    "ppid": "int",
    "status": "string",
    "threads": Class.create_list(Class("pthread", "float")),
    "username": "string"
}
