from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = "Power"
    capacity_factor = 0.25
    memory_factor = 1.75

    def __init__(self, name, capacity, memory):
        new_capacity = int(capacity * PowerHardware.capacity_factor)
        new_memory = int(memory * PowerHardware.memory_factor)
        super().__init__(name, PowerHardware.TYPE, new_capacity, new_memory)