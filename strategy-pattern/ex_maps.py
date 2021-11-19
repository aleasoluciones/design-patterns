from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Map():
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    @property
    def transport(self) -> Transport:
        return self._transport

    @transport.setter
    def transport(self, transport: Transport) -> None:
        self._transport = transport

    def give_me_the_route(self) -> None:
        result = self._transport.calculate_route(["Avenida de la Albufera, Metro Sierra de Guadalupe"])
        print(result)

class Transport(ABC):
    @abstractmethod
    def calculate_route(self, points: List) -> int:
        pass

class CarTransport(Transport):
    def calculate_route(self, points: List) -> int:
        print("Route by car in minutes")
        return sum([len(x) for x in points]) / 2

class FootTransport(Transport):
    def calculate_route(self, points: List) -> int:
        print("Route by foot in minutes")
        return sum([len(x) for x in points]) * 2


if __name__ == "__main__":
    print("Route from point A to point B")
    alea_map = Map(CarTransport())
    alea_map.give_me_the_route()
    print()

    alea_map.transport = FootTransport()
    alea_map.give_me_the_route()
    print()
