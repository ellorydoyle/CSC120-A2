"""
    Filename: computer.py
    Description: the class definitions for Computer
    Author: Ellory Doyle (@ellorydoyle)
    Date: 8 February 2023
"""
# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
#This class represents my computers
class Computer:

    # Here are my attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    #Here are my methods
    #This is my constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    #This can be called on to print or return the computer details
    def __repr__(self) -> str:
        return (
        f"Description: {self.description}\n"
        f"Processor Type: {self.processor_type}\n"
        f"Hard Drive Capacity: {self.hard_drive_capacity}\n"
        f"Memory: {self.memory}\n"
        f"Operating System: {self.operating_system}\n"
        f"Year Made: {self.year_made}\n"
        f"Price: {self.price}"
        )