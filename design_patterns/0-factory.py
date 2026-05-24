#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def mode(self):
        pass


class Bus(Vehicle):
    def mode(self):
        return "road"


class Train(Vehicle):
    def mode(self):
        return "rails"


class Bike(Vehicle):
    def mode(self):
        return "lane"


class Scooter(Vehicle):
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {
            "bus": Bus,
            "train": Train,
            "bike": Bike
        }

    def register_kind(self, name, cls):
        self._registry[name] = cls

    def create(self, kind):
        return self._registry[kind]()


def main():
    factory = VehicleFactory()

    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()