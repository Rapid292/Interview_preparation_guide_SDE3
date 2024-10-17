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

from enum import Enum

# Elevator state
class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3

class Status(Enum):
    MOVING = 1
    STOPPED = 2
    MAINTENANCE = 3

class Elevator:
    def __init__(self, id, total_floors):
        self.id = id                    # Unique ID for the elevator
        self.current_floor = 0           # Starting floor of the elevator
        self.direction = Direction.IDLE  # Initial direction
        self.status = Status.STOPPED     # Initial status (not moving)
        self.requests = []               # List of floors the elevator has to visit
        self.total_floors = total_floors # Total number of floors the elevator can serve

    def request_floor(self, floor):
        # Add a requested floor to the list if it's not already there.
        if floor not in self.requests:
            self.requests.append(floor)
        # Sort floors based on the current direction
        if self.direction == Direction.UP:
            self.requests.sort()  # Floors are sorted in ascending order when moving up.
        elif self.direction == Direction.DOWN:
            self.requests.sort(reverse=True)  # Floors are sorted in descending order when moving down.

    def move(self):
        # Elevator moves to the next requested floor.
        if not self.requests:
            self.direction = Direction.IDLE
            self.status = Status.STOPPED
            return

        # Get the next floor from the list of requests.
        next_floor = self.requests[0]

        # Moving logic: up or down
        if self.current_floor < next_floor:
            self.direction = Direction.UP
            self.current_floor += 1
        elif self.current_floor > next_floor:
            self.direction = Direction.DOWN
            self.current_floor -= 1
        else:
            # When reached the desired floor, remove it from requests.
            self.requests.pop(0)
            self.status = Status.STOPPED

        # Update status to MOVING when the elevator is in transit.
        if self.requests:
            self.status = Status.MOVING

    def __str__(self):
        # Returns the current status of the elevator.
        return f"Elevator {self.id} at floor {self.current_floor}, direction: {self.direction}, status: {self.status}, requests: {self.requests}"

class ElevatorController:
    def __init__(self, num_elevators, total_floors):
        # Initialize multiple elevators.
        self.elevators = [Elevator(i, total_floors) for i in range(num_elevators)]
        self.total_floors = total_floors

    def request_elevator(self, floor, direction):
        # Find the closest elevator that is idle or moving in the desired direction.
        best_elevator = None
        best_distance = self.total_floors + 1  # Start with the worst possible distance.

        for elevator in self.elevators:
            if elevator.direction == Direction.IDLE:
                distance = abs(elevator.current_floor + floor)
                if distance < best_distance:
                    best_elevator = elevator
                    best_distance = distance
            elif elevator.direction == direction:
                if direction == Direction.UP and elevator.current_floor <= floor:
                    distance = floor - elevator.current_floor
                elif direction == Direction.DOWN and elevator.current_floor >= floor:
                    distance = elevator.current_floor - floor

                if distance < best_distance:
                    best_elevator = elevator
                    best_distance = distance

        # Assign the request to the best elevator found.
        if best_elevator:
            best_elevator.request_floor(floor)
            print(f"Assigned elevator {best_elevator.id} to floor {floor}")

    def step(self):
        # Simulate each elevator taking a step (moving one floor).
        for elevator in self.elevators:
            elevator.move()
            print(elevator)

if __name__ == "__main__":
    controller = ElevatorController(3, 10)

    # Requests coming in
    controller.request_elevator(3, Direction.UP)
    controller.request_elevator(5, Direction.UP)
    controller.request_elevator(7, Direction.DOWN)

    # Simulate the elevator system by repeatedly calling step.
    for _ in range(10):
        controller.step()

"""
Explanation:

Classes, Interfaces, and Enumerations:
The Elevator class represents an individual elevator and contains attributes such as current floor, direction, and status. It also manages the requests to visit floors and handles the logic for moving the elevator between floors.
The ElevatorController class manages multiple elevators. It is responsible for receiving floor requests and assigning them to the most suitable elevator based on direction, distance, and current requests. It also simulates elevator movement.
The Direction enum defines the possible directions an elevator can move (UP, DOWN, IDLE).
The Status enum defines the operational states of the elevator (MOVING, STOPPED, MAINTENANCE).
The system simulates elevator movement through repeated calls to the `step()` method, which moves each elevator one step at a time towards its destination.

"""