from abc import ABC, abstractmethod


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



# strawberry_shortcake = Cupcake(1.99, 0.75, "strawberry", "strawberry cream", "cherry")                #can no longer use the parent class due to it's abstract base class nature (ABC)

# print("\nStrawberry Shortcake - Regular:")
# print(strawberry_shortcake.price)
# print(strawberry_shortcake.cost)
# print(strawberry_shortcake.flavor)
# print(strawberry_shortcake.frosting)
# print(strawberry_shortcake.filling)
# print(strawberry_shortcake.size)

print("======================================")

class Mini(Cupcake):
    size = "mini"

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


print("======================================")


strawberry_shortcake_mini = Mini(0.55, 0.35, "strawberry", "strawberry cream")

print("\nStrawberry Shortcake - Mini:")

print("Price: ", strawberry_shortcake_mini.price)
print("Cost: ", strawberry_shortcake_mini.cost)
print("Cake Flavor: ", strawberry_shortcake_mini.flavor)
print("Frosting:", strawberry_shortcake_mini.frosting)
print("Size: ", strawberry_shortcake_mini.size)
print("Gluten Free? ", strawberry_shortcake_mini.gluten_free)

strawberry_shortcake_regular = Regular(1.99, 0.75, "strawberry", "strawberry cream", "cherry")

print("\nStrawberry Shortcake - Regular:")
print("Price: ", strawberry_shortcake_regular.price)
print("Cost: ", strawberry_shortcake_regular.cost)
print("Cake Flavor: ", strawberry_shortcake_regular.flavor)
print("Frosting:", strawberry_shortcake_regular.frosting)
print("Filling: ", strawberry_shortcake_regular.filling)
print("Size: ", strawberry_shortcake_regular.size)
print("Gluten Free? ", strawberry_shortcake_regular.gluten_free)



strawberry_shortcake_large = Large(3.99, 2.17, "Strawberry", "Strawberry Cream", "Cherry")

strawberry_shortcake_large.make_gluten_free(True)

print("\nStrawberry Shortcake - Large:")
print("Price: ", strawberry_shortcake_large.price)
print("Cost: ", strawberry_shortcake_large.cost)
print("Cake Flavor: ", strawberry_shortcake_large.flavor)
print("Frosting:", strawberry_shortcake_large.frosting)
print("Filling: ", strawberry_shortcake_large.filling)
print("Size: ", strawberry_shortcake_large.size)
print("Gluten Free? ", strawberry_shortcake_large.gluten_free)

