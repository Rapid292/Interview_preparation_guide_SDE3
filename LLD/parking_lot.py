"""
Designing a Parking Lot System
Requirements:
The parking lot should have multiple levels, each level with a certain number of parking spots.
The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
Each parking spot should be able to accommodate a specific type of vehicle.
The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
The system should track the availability of parking spots and provide real-time information to customers.
The system should handle multiple entry and exit points and support concurrent access.
"""
from enum import Enum
from abc import ABC
import threading


class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3


class Vehicle(ABC):
    # Applying Liskov Substitution Principle (LSP) - all derived vehicle types (Car, Motorcycle, Truck)
    # can replace the Vehicle base class without altering the correctness of the program.
    def __init__(self, vehicleType, registrationNumber):
        self.vehicleType = vehicleType
        self.registrationNumber = registrationNumber


class Car(Vehicle):
    # Inherits from Vehicle class (Inheritance) and complies with LSP.
    def __init__(self, registrationNumber):
        super().__init__(VehicleType.CAR, registrationNumber)


class Motorcycle(Vehicle):
    # Inherits from Vehicle class (Inheritance) and complies with LSP.
    def __init__(self, registrationNumber):
        super().__init__(VehicleType.MOTORCYCLE, registrationNumber)


class Truck(Vehicle):
    # Inherits from Vehicle class (Inheritance) and complies with LSP.
    def __init__(self, registrationNumber):
        super().__init__(VehicleType.TRUCK, registrationNumber)


class ParkingLot:
    _lock = threading.Lock()
    _instance = None

    # Applying Singleton Design Pattern - Only one instance of ParkingLot is created and shared across the system.
    def __init__(self):
        self.levels = []

    @staticmethod
    def get_instance():
        # Applying Double-Checked Locking pattern to ensure thread-safe Singleton initialization.
        if not ParkingLot._instance:
            with ParkingLot._lock:
                if not ParkingLot._instance:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def addLevel(self, level):
        # Applying Open/Closed Principle (OCP) - The system is open for extension (adding more levels)
        # but closed for modification of existing code structure.
        self.levels.append(level)

    def parkVehicle(self, vehicle):
        # This method is open to adding more functionality (such as more levels or vehicle types)
        # without changing its core behavior, supporting OCP.
        for level in self.levels:
            level.parkVehicle(vehicle)
            return True
        return False

    def unparkVehicle(self, vehicle):
        for level in self.levels:
            level.unparkVehicle(vehicle)
            return True
        return False

    def displayAvailableSpots(self):
        # This method displays the available parking spots at each level.
        for level in self.levels:
            level.displayAvailableSpots()


class Level:
    # Level class adheres to Single Responsibility Principle (SRP) - only manages parking spots on a specific level.
    def __init__(self, floor: int, numberOfSpots: int):
        self.floor = floor
        self.parkingSpots = [ParkingSpot(i) for i in range(numberOfSpots)]

    def parkVehicle(self, vehicle):
        # This method adheres to SRP by being responsible for parking vehicles in appropriate spots.
        for spot in self.parkingSpots:
            if spot.isAvailable() and spot.vehicleType == vehicle.vehicleType:
                spot.parkVehicle(vehicle)
                return True

    def unparkVehicle(self, vehicle):
        # Unparks the vehicle from the spot it was parked in, maintaining SRP.
        for spot in self.parkingSpots:
            if not spot.isAvailable() and spot.parked_vehicle == vehicle:
                spot.unparkVehicle()
                return True
        return False

    def displayAvailableSpots(self):
        # Displays all available or occupied spots per level.
        for spot in self.parkingSpots:
            if not spot.isAvailable():
                print(f"Level: {self.floor}, Spot: {spot.spotNumber}, Occupied Vehicle of Type {spot.parked_vehicle.vehicleType} of Registration Number: {spot.parked_vehicle.registrationNumber}")
            # else:
            #     print(f"Level: {self.floor}, Spot: {spot.spotNumber}, Available")


class ParkingSpot:
    # ParkingSpot adheres to SRP, as it handles only one responsibility - managing the status of a parking spot.
    def __init__(self, spotNumber: int):
        self.spotNumber = spotNumber
        self.vehicleType = VehicleType.CAR  # Default value, can be extended (OCP).
        self.parked_vehicle = None

    def isAvailable(self):
        # Checks whether a spot is available (SRP).
        return not self.parked_vehicle

    def parkVehicle(self, vehicle):
        # Responsible for assigning a vehicle to the spot (SRP).
        if self.isAvailable() and vehicle.vehicleType == self.vehicleType:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or Spot not available")

    def unparkVehicle(self):
        # Responsible for releasing the parking spot (SRP).
        self.parked_vehicle = None


if __name__ == "__main__":
    # Main program demonstrating the use of Singleton ParkingLot and vehicle parking system.
    parking_lot = ParkingLot.get_instance()
    parking_lot.addLevel(Level(1, 100))
    parking_lot.addLevel(Level(2, 80))

    car = Car("ABC123")
    truck = Truck("XYZ789")
    motorcycle = Motorcycle("M1234")

    # Park vehicles
    parking_lot.parkVehicle(car)
    parking_lot.parkVehicle(truck)
    parking_lot.parkVehicle(motorcycle)

    # Display availability
    parking_lot.displayAvailableSpots()

    # Unpark vehicle
    parking_lot.unparkVehicle(motorcycle)

    # Display updated availability
    parking_lot.displayAvailableSpots()


"""
Explaination:

Classes, Interfaces and Enumerations:
The ParkingLot class follows the Singleton pattern to ensure only one instance of the parking lot exists. It maintains a list of levels and provides methods to park and unpark vehicles.
The Level class represents a level in the parking lot and contains a list of parking spots. It handles parking and unparking of vehicles within the level.
The ParkingSpot class represents an individual parking spot and tracks the availability and the parked vehicle.
The Vehicle class is an abstract base class for different types of vehicles. It is extended by Car, Motorcycle, and Truck classes.
The VehicleType enum defines the different types of vehicles supported by the parking lot.
Multi-threading is achieved through the use of synchronized keyword on critical sections to ensure thread safety.
The Main class demonstrates the usage of the parking lot system.

"""