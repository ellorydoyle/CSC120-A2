"""
    Filename: oo_resale_shop.py
    Description: the class definitions for Resale Shop
    Author: Ellory Doyle (@ellorydoyle)
    Date: 6 February 2023
"""
from computer import *
from typing import Dict, Union, Optional
class ResaleShop:

    # What attributes will it need?
    name = "Ellory's Store"
    inventory = list
    item_id = 0 # We'll increment this every time we add a new item 
                # so that we always have a new value for the itemID
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory) -> None:
        self.inventory = []

    # What methods will you need?
    def buy(self, inventory, item_id):
        item_id += 1
        item_id = Computer()
        inventory.append(item_id.computer)
        print(self.inventory)
        #1. call Computer(...)constructor
        #   to create a new Computer instance

        #2. call inventory.append(...) to add the
        #   new Computer instance to the inventory

    def sell(self, inventory, item_id):
        pass

    def update_price(self, inventory, price):
        pass

    def update_os(self, inventory):
        pass

    def print_inventory(self):
        for c in self.inventory:
            c.print_details()
