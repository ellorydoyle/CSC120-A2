"""
    Filename: oo_resale_shop.py
    Description: the class definitions for Resale Shop
    Author: Ellory Doyle (@ellorydoyle)
    Date: 8 February 2023
"""
from computer import Computer
from typing import Dict, Union, Optional
#This class is the resale shop that the computers are fed through
class ResaleShop:

    # What attributes will it need?
    name = "Ellory's Store"
    inventory :list
    item_id = 0 
    
    #This is my constructor
    def __init__(self) -> None:
        self.inventory = []

    #This creates a new computer
    def create(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        return computer

    #This allows you to buy a computer and place it in inventory
    def buy(self, computer):
        self.item_id += 1
        self.inventory.append(computer)
        return self.item_id

    #This allows you to sell the computer from the inventory
    def sell(self):
        if self.item_id in range(self.inventory):
            del self.inventory[self.item_id]
            print("Item", self.item_id, "sold!")
        else: 
            print("Item", self.item_id, "not found. Please select another item to sell.")

    #This allows you to update the price of the computer in the inventory
    def update_price(self, new_price: int):
        if self.item_id in range(self.inventory):
            self.inventory[self.item_id]["price"] = new_price
        else:
            print("Item", self.item_id, "not found. Cannot update price.")

    #This allows you to refurbish the computers
    def refurbish(self, new_os: Optional[str] = None):
        if self.item_id in range(self.inventory):
            computer = self.inventory[self.item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", self.item_id, "not found. Please select another item to refurbish.")
