
from ..vehicles_subsystem import Vehicle

class VehicleMemento:
    def __init__(self, vehicle: Vehicle) -> None:
        self._vehicle = vehicle

    def get_saved_vehicle(self) -> Vehicle:
        return self._vehicle
    
class VehicleHistory:

    def __init__(self) -> None:
        self._history = []

    def save_state(self, memento: VehicleMemento) -> None:
        self._history.append(memento)

    def get_last_saved(self) -> VehicleMemento:
        return self._history.pop() if self._history else None