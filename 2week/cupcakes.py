from abc import ABC, abstractmethod
import csv
from pprint import pprint


def read_csv ():
    with open ("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def write_csv (file, cupcakes):
    with open (file, "w", newline="/n") as csvfile:
        fieldnames = ["size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)




####################################################################

class Cupcake(ABC):

    size = "regular"
    gluten_free = False


    def __init__(self, price, cost, cake_flavor, frosting_type, filling_type):

        self.price = price
        self.cost = cost
        self.flavor = cake_flavor
        self.frosting = frosting_type
        self.filling = filling_type
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkles in args:
            self.sprinkles.append(sprinkles)

    @abstractmethod
    def make_gluten_free(self, bool):
        self.gluten_free = bool

    @abstractmethod
    def calculate_price(self, order_quantity):
        return order_quantity * self.price



# strawberry_shortcake = Cupcake(1.99, 0.75, "strawberry", "strawberry cream", "cherry")                #can no longer use the parent class (Cupcake) due to it's abstract base class nature (ABC)

# print("\nStrawberry Shortcake - Regular:")
# print(strawberry_shortcake.price)
# print(strawberry_shortcake.cost)
# print(strawberry_shortcake.flavor)
# print(strawberry_shortcake.frosting)
# print(strawberry_shortcake.filling)
# print(strawberry_shortcake.size)

print("======================================")

class Mini(Cupcake):
    size = "Mini"

    def __init__(self, price, cost, cake_flavor, frosting_type):

        self.price = price
        self.cost = cost
        self.flavor = cake_flavor
        self.frosting = frosting_type
        self.sprinkles = []

    def calculate_price(self, order_quantity):
        return order_quantity * self.cost
    
    def make_gluten_free(self, bool):
        self.gluten_free = bool

class Regular(Cupcake):
    size = "Regular"

    def __init__(self, price, cost, cake_flavor, frosting_type, filling_type):
        self.price = price
        self.cost = cost
        self.flavor = cake_flavor
        self.frosting = frosting_type
        self.filling = filling_type
        self.sprinkles = []
    
    def calculate_price(self, order_quantity):
        return order_quantity * self.cost

    def make_gluten_free(self, bool):
        self.gluten_free = bool
    
class Large(Cupcake):

    size = "Large"

    def __init__(self, price, cost, cake_flavor, frosting_type, filling_type):
        self.price = price
        self.cost = cost
        self.flavor = cake_flavor
        self.frosting = frosting_type
        self.filling = filling_type

    def calculate_price(self, order_quantity):
        return order_quantity * self.cost

    def make_gluten_free(self, bool):
        self.gluten_free = bool


###############################################################


strawberry_shortcake_mini = Mini(0.55, 0.35, "strawberry", "strawberry cream")

strawberry_shortcake_regular = Regular(1.99, 0.75, "strawberry", "strawberry cream", "cherry")

strawberry_shortcake_large = Large(3.99, 2.17, "Strawberry", "Strawberry Cream", "Cherry")

strawberry_shortcake_large.make_gluten_free(True)





if __name__ == "__main__":
    read_csv()