from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"
    memory_factor = 2

    def __init__(self, name, capacity_consumption, memory_consumption):
        new_memory = int(memory_consumption * ExpressSoftware.memory_factor)
        super().__init__(name, ExpressSoftware.TYPE, capacity_consumption, new_memory)