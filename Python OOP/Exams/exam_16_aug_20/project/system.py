from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
            software = [x for x in System._software if x.name == software_name][0]
            if hardware and software:
                hardware.uninstall(software)
                System._software.remove(software)
        except IndexError:
            "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f'System Analysis\n' \
               f'Hardware Components: {len(System._hardware)}\n' \
               f'Software Components: {len(System._software)}\n' \
               f'Total Operational Memory: {sum(x.memory_consumption for x in System._software)} / ' \
               f'{sum(x.memory_consumption for x in System._hardware)}\n' \
               f'Total Capacity Taken: {sum(x.capacity_consumption for x in System._software)} / ' \
               f'{sum(x.capacity_consumption for x in System._hardware)}'

    @staticmethod
    def system_split():
        return '\n'.join(str(x) for x in System._hardware)
