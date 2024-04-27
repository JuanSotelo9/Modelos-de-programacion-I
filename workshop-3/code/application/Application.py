from abc import ABC, abstractmethod
from datetime import datetime
import psutil

class Application(ABC):

    def __init__(self) -> None:
        self.controller = None

    @abstractmethod
    def run(self):
        """This method is the main of the application"""

class MainApplication(Application):

    def run(self):
        pass

    def login(self):
        pass

class Monitoring(Application):
    
    def __init__(self, application) -> None:
        super().__init__()
        self.wrapped = application
        self.monitoring_file = "monitoring.txt"

    def run(self):
        self.__monitor_start()
        memory_before = self.__get_memory_usage()
        self.wrapped.run()
        memory_after = self.__get_memory_usage()
        self.__monitor_end(memory_before, memory_after)

    def __monitor_start(self):
        with open(self.monitoring_file, "a") as file:
            file.write(f"Monitoring started at: {datetime.now()}")

    def __monitor_end(self, memory_before, memory_after):
        with open(self.monitoring_file, "a") as file:
            file.write(f"Memory consumption during execution: {memory_after - memory_before} bytes")
            file.write(f"Monitoring ended at: {datetime.now()}")

    def __get_memory_usage(self):
        process = psutil
        memory_usage = process.memory_info().rss
        return memory_usage