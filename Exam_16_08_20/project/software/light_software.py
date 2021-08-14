from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"
    capacity_factor = 1.5
    memory_factor = 0.5

    def __init__(self, name, capacity_consumption, memory_consumption):
        new_capacity = int(capacity_consumption * LightSoftware.capacity_factor)
        new_memory = int(memory_consumption * LightSoftware.memory_factor)
        super().__init__(name, LightSoftware.TYPE, new_capacity, new_memory)
