from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = "Heavy"
    capacity_factor = 2
    memory_factor = 0.75

    def __init__(self, name, capacity, memory):
        new_capacity = int(capacity * HeavyHardware.capacity_factor)
        new_memory = int(memory * HeavyHardware.memory_factor)
        super().__init__(name, HeavyHardware.TYPE, new_capacity, new_memory)