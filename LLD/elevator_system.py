"""
Designing an Elevator System
Requirements:
The elevator system should consist of multiple elevators serving multiple floors.
Each elevator should have a capacity limit and should not exceed it.
Users should be able to request an elevator from any floor and select a destination floor.
The elevator system should efficiently handle user requests and optimize the movement of elevators to minimize waiting time.
The system should prioritize requests based on the direction of travel and the proximity of the elevators to the requested floor.
The elevators should be able to handle multiple requests concurrently and process them in an optimal order.
The system should ensure thread safety and prevent race conditions when multiple threads interact with the elevators.
"""
import time
from enum import Enum
from threading import Thread, Lock, Condition


class Direction(Enum):
    UP = 1
    DOWN = 2

class Request:
    def __init__(self, source_floor, destination_floor):
        # This class follows the **Single Responsibility Principle (SRP)**
        # by only encapsulating the request details (source and destination).
        self.source_floor = source_floor
        self.destination_floor = destination_floor

class Elevator:
    def __init__(self, id: int, capacity: int):
        # The **Single Responsibility Principle (SRP)** is applied here as this class is responsible
        # for handling elevator-specific operations (moving and processing requests).
        # **Factory Method Pattern** could be considered, as Elevator objects are created dynamically in ElevatorController.
        self.id = id
        self.capacity = capacity
        self.current_floor = 1
        self.current_direction = Direction.UP
        self.requests = []
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def add_request(self, request: Request):
        with self.lock:
            # Ensures thread-safe request addition using **threading locks**, adhering to the **Liskov Substitution Principle (LSP)**.
            if len(self.requests) < self.capacity:
                self.requests.append(request)
                print(
                    f"Elevator {self.id} added request: {request.source_floor} to {request.destination_floor}"
                )
                self.condition.notify_all()

    def get_next_request(self) -> Request:
        # **Command Pattern**: The request to move the elevator can be viewed as a command, where
        # an elevator is instructed to fulfill the next pending request.
        with self.lock:
            while not self.requests:
                self.condition.wait()
            return self.requests.pop(0)

    def process_requests(self):
        # This method runs an infinite loop to process incoming requests, adhering to the **Single Responsibility Principle (SRP)**.
        while True:
            request = self.get_next_request()  # This will wait until there's a request
            self.process_request(request)

    def process_request(self, request: Request):
        # This method defines the core responsibility of the elevator (moving between floors), adhering to the **Open/Closed Principle (OCP)**,
        # as it can be extended to include other functionalities without modifying the base logic.
        start_floor = self.current_floor
        end_floor = request.destination_floor

        if start_floor < end_floor:
            self.current_direction = Direction.UP
            for i in range(start_floor, end_floor + 1):
                self.current_floor = i
                print(f"Elevator {self.id} reached floor {self.current_floor}")
                time.sleep(1)  # Simulating elevator movement
        elif start_floor > end_floor:
            self.current_direction = Direction.DOWN
            for i in range(start_floor, end_floor - 1, -1):
                self.current_floor = i
                print(f"Elevator {self.id} reached floor {self.current_floor}")
                time.sleep(1)  # Simulating elevator movement

    def run(self):
        # **Template Method Pattern**: The `run` method invokes `process_requests`
        # to handle the movement and request processing.
        self.process_requests()

class ElevatorController:
    def __init__(self, num_elevators: int, capacity: int):
        # **Single Responsibility Principle (SRP)**: ElevatorController manages the elevators and requests optimally.
        # The **Factory Method Pattern** can be applied here for dynamically creating Elevator instances.
        self.elevators = []
        for i in range(num_elevators):
            elevator = Elevator(i + 1, capacity)
            self.elevators.append(elevator)
            Thread(target=elevator.run).start()

    def request_elevator(self, source_floor: int, destination_floor: int):
        # **Facade Pattern**: This method provides a simplified interface for clients to request an elevator.
        optimal_elevator = self.find_optimal_elevator(source_floor, destination_floor)
        optimal_elevator.add_request(Request(source_floor, destination_floor))

    def find_optimal_elevator(self, source_floor: int, destination_floor: int) -> Elevator:
        # **Strategy Pattern**: Different strategies could be applied here for selecting the optimal elevator
        # (e.g., based on load, direction, or proximity).
        optimal_elevator = None
        min_distance = float('inf')

        for elevator in self.elevators:
            distance = abs(source_floor - elevator.current_floor)
            if distance < min_distance:
                min_distance = distance
                optimal_elevator = elevator

        return optimal_elevator


if __name__ == "__main__":
    controller = ElevatorController(3, 5)
    time.sleep(3)
    controller.request_elevator(10, 12)
    time.sleep(3)
    controller.request_elevator(1, 7)
    time.sleep(3)
    controller.request_elevator(2, 5)
    time.sleep(3)
    controller.request_elevator(1, 9)

    # Keep the main thread running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Elevator system stopped.")
