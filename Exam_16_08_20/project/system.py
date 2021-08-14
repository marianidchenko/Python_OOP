from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        current_hardware = None
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                current_hardware = hardware
        if current_hardware:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                current_hardware.install(software)
                System._software.append(software)
            except Exception as ex:
                return str(ex)
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        current_hardware = None
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                current_hardware = hardware
        if current_hardware:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                current_hardware.install(software)
                System._software.append(software)
            except Exception as ex:
                return str(ex)
        else:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = None
        software = None
        for h in System._hardware:
            if h.name == hardware_name:
                hardware = h
                break
        for s in System._software:
            if s.name == software_name:
                software = s
                break
        if software and hardware:
            hardware.uninstall(software)
            System._software.remove(s)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ["System Analysis"]
        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {sum([x.memory_consumption for x in System._software])} "
                      f"/ {sum([x.memory for x in System._hardware])}")
        result.append(f"Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} "
                      f"/ {sum([x.capacity for x in System._hardware])}")
        return "\n".join(result)

    @staticmethod
    def system_split():
        results = []
        for hardware in System._hardware:
            result = []
            result.append(f"Hardware Component - {hardware.name}")
            result.append(
                f"Express Software Components: {len([x for x in hardware.software_components if x.type == 'Express'])}")
            result.append(
                f"Light Software Components: {len([x for x in hardware.software_components if x.type == 'Light'])}")
            result.append(
                f"Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / "
                f"{hardware.memory}")
            result.append(
                f"Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / "
                f"{hardware.capacity}")
            result.append(f"Type: {hardware.type}")
            if System._software:
                result.append(f"Software Components: {', '.join(x.name for x in hardware.software_components)}")
            else:
                result.append(f"Software Components: None")
            results.append('\n'.join(result))
        return ''.join(results)