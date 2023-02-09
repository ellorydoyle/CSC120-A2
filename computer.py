"""
    Filename: computer.py
    Description: the class definitions for Computer
    Author: Ellory Doyle (@ellorydoyle)
    Date: 6 February 2023
"""
# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    def print_details(self):
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)

    # What methods will you need?
    
def main():
    description = input("What is the description of the computer?  > ")
    processor_type = input("What is the processor type of the computer?  > ")
    hard_drive_capacity = input("What is the hard drive capacity of the computer?  > ")
    memory = input("How big is the computer's memory?  > ")
    operating_system = input("What is the operating system of the computer?  > ")
    year_made = input("What is the year that the computer was made?  > ")
    price = input("What is the price of the computer?  > ")
    computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    computer.print_details()

main()