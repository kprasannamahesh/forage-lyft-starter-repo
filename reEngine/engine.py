from abc import ABC

class Engine(ABC):
    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.last_service_milage = last_service_milage
        self.current_milage = current_milage

    def need_services(self):
        return self.current_milage - self.last_service_milage > 30000

class SternmanEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def need_services(self):
        return self.current_milage - self.last_service_milage > 30000

class WiloughByEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def need_services(self):
        return self.current_milage - self.last_service_milage > 30000
