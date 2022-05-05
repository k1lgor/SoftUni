from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def free_capacity(self):
        return sum(x.capacity_consumption for x in self.software_components)

    @property
    def free_memory(self):
        return sum(x.memory_consumption for x in self.software_components)

    def install(self, software: Software):
        if software.memory_consumption > self.free_memory and software.capacity_consumption > self.free_capacity:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __str__(self):
        software_comp = f'{", ".join(x.name for x in self.software_components)}'
        if not software_comp:
            software_comp = 'None'
        return f'Hardware Component - {self.name}\n' \
               f'Express Software Components: {len([x for x in self.software_components if x.software_type == "Express"])}\n' \
               f'Light Software Components: {len([x for x in self.software_components if x.software_type == "Light"])}\n' \
               f'Memory Usage: {sum([x for x in self.software_components if x.memory_consumption])} / {self.memory}\n' \
               f'Capacity Usage: {sum([x for x in self.software_components if x.capacity_consumption])} / {self.capacity}\n' \
               f'Software Components: {software_comp}'
