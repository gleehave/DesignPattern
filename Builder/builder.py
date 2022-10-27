# two builders: Margarita Builder, CreamyBaconBuilder

from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')

STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        time.sleep(STEP_DELAY)

        print(f"preparing the {self.dough.name} dough of you {self}...")
        print(f'done with the {self.dough.name} dough')

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.backing_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)

    def bake(self):
        self.progress = PizzaProgress.baking
        time.sleep(self.backing_time)
        self.progress = PizzaProgress.ready


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)

    def add_topping(self):
        topping_desc = 'mozzarella, bacon, ham, mushrooms, red onion, oregano'
        topping_items = (PizzaTopping.mozzarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)

    def bake(self):
        self.progress = PizzaProgress.baking
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready