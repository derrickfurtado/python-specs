class Cupcake():

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



strawberry_shortcake = Cupcake(1.99, 0.75, "strawberry", "strawberry cream", "cherry")

print("Cake type: ", strawberry_shortcake.flavor)
print("Filling type: ", strawberry_shortcake.filling)
print("Frosting type: ", strawberry_shortcake.frosting)
print("Sprikles type: ", strawberry_shortcake.sprinkles)

strawberry_shortcake.add_sprinkles("rainbow", "cherry", "Oreo")
print("============================")


print("Cake type: ", strawberry_shortcake.flavor)
print("Filling type: ", strawberry_shortcake.filling)
print("Frosting type: ", strawberry_shortcake.frosting)
print("Sprikles type: ", strawberry_shortcake.sprinkles)
