from abc import ABC, abstractmethod
import csv, random
from pprint import pprint




####################################################################


def read_csv (file):
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def write_csv (file, cupcakes):
    with open (file, "w", newline="\n") as csvfile:
        csv_field_names = ["name", "size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
        writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
        writer.writeheader()
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"name": cupcake.name, "size": cupcake.size, "price": cupcake.price, "cost": cupcake.cost, "flavor": cupcake.flavor, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles, "gluten_free": cupcake.gluten_free})
            else:
                writer.writerow({"name": cupcake.name, "size": cupcake.size, "price": cupcake.price, "cost": cupcake.cost, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles, "gluten_free": cupcake.gluten_free})
            

def append_csv (file, cupcake):
    with open (file, "a", newline="\n") as csvfile:
        csv_field_names = ["name", "size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
        writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
        if hasattr(cupcake, "filling"):
            writer.writerow({"name": cupcake.name, "size": cupcake.size, "price": cupcake.price, "cost": cupcake.cost, "flavor": cupcake.flavor, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles, "gluten_free": cupcake.gluten_free})
        else:
            writer.writerow({"name": cupcake.name, "size": cupcake.size, "price": cupcake.price, "cost": cupcake.cost, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles, "gluten_free": cupcake.gluten_free})

####################################################################




def display_menu(source):
    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
    return reader

def show_cart(source):
    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
    return reader

def display_random_cupcakes(source):
    batch = []                  #should be copy of all cupcakes from the source csv
    sorted_batch = []

    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            batch.append(row)                       # append all cupcakes to batch list
        index = random.randint(0, len(batch)-1)     
        sorted_batch.append(batch[index])              
        index = random.randint(0, len(batch)-1)                 
        sorted_batch.append(batch[index])           #append 3 random cupcakes from batch list to sorted batch list
        index = random.randint(0, len(batch)-1)                 
        sorted_batch.append(batch[index])
    
    return sorted_batch

    ######## No longer needing the following as I'm sending batch direct to HTML with Jinja2 ##########

    # with open(target, "w", newline="\n") as csvfile:
    #     csv_field_names = ["name", "size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
    #     writer.writeheader()
    #     for x in sorted_batch:
    #         if hasattr(x, "filling"):
    #             writer.writerow({"name": x["name"], "size": x["size"], "price": x["price"], "cost": x["cost"], "flavor": x["flavor"], "filling": x["filling"], "sprinkles": x["sprinkles"], "gluten_free": x["gluten_free"]})
    #         else:
    #             writer.writerow({"name": x["name"], "size": x["size"], "price": x["price"], "cost": x["cost"], "flavor": x["flavor"], "sprinkles": x["sprinkles"], "gluten_free": x["gluten_free"]})



def find_cupcake_name(source, name_query):
    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        reader_list = list(reader)
        for cupcake in reader_list:
            if cupcake["name"] == name_query:
                return cupcake
        # return None
    
def add_cupcake_to_order(target, cupcake):
    with open(target, "a", newline="\n") as csvfile:
        csv_field_names = ["name", "size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
        writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
        if hasattr(cupcake, "filling"):
            writer.writerow({"name": cupcake["name"], "size": cupcake["size"], "price": cupcake["price"], "cost": cupcake["cost"], "flavor": cupcake["flavor"], "filling": cupcake["filling"], "sprinkles": cupcake["sprinkles"], "gluten_free": cupcake["gluten_free"]})
        else:
            writer.writerow({"name": cupcake["name"], "size": cupcake["size"], "price": cupcake["price"], "cost": cupcake["cost"], "flavor": cupcake["flavor"], "sprinkles": cupcake["sprinkles"], "gluten_free": cupcake["gluten_free"]})

def empty_cart(target):
    with open(target, "w", newline="\n") as csvfile:
        csv_field_names = ["name", "size", "price", "cost", "flavor", "frosting", "filling", "sprinkles", "gluten_free"]
        writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
        writer.writeheader()

####################################################################

class Cupcake(ABC):                                                 ##### parent ABC class #####

    size = "regular"
    gluten_free = False


    def __init__(self, name, price, cost, cake_flavor, frosting_type, filling_type):

        self.name = name
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
    gluten_free = False

    def __init__(self, name, price, cost, cake_flavor, frosting_type):

        self.name = name
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
    gluten_free = False

    def __init__(self, name, price, cost, cake_flavor, frosting_type, filling_type):
        self.name = name
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
    gluten_free = False

    def __init__(self, name, price, cost, cake_flavor, frosting_type, filling_type):
        self.name = name
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


###############################################################


cupcake_1 = Mini("Strawberry Shortcake", .99, .35, "strawberry", "strawberry")
cupcake_2 = Regular("Strawberry Shortcake", 1.99, 0.75, "strawberry", "strawberry cream", "cherry")
cupcake_3 = Large("Strawberry Shortcake", 3.99, 2.17, "Strawberry", "Strawberry Cream", "Cherry")
cupcake_4 = Regular("Stars and Stripes", 2.99, 1.20, "Blueberry", "White Cream", None)
cupcake_5 = Mini("Oreo", .99, .25, "Chocolate", "Amaretto")
cupcake_6 = Large("Red Velvet", 3.99, 1.75, "Cherry", "Cherry", None)

cupcake_3.make_gluten_free(True)
cupcake_5.add_sprinkles("Oreo pieces")
cupcake_3.add_sprinkles("pink", "white", "red")
cupcake_4.add_sprinkles("Red", "White", "Blue")

cupcake_list = [ 
    cupcake_1,
    cupcake_2,
    cupcake_3,
    cupcake_4,
    cupcake_5,
    cupcake_6
]

### additional Cupcakes:

cupcake_7 = Mini("Vanilla Dream", 1.50, 0.75, "Vanilla", ["Rainbow Sprinkles"])
cupcake_8 = Large("Chocolate Haven", 2.00, 1.00, "Chocolate", ["Chocolate Chips"], "Chocolage")
cupcake_9 = Large("Strawberry Swirl", 1.80, 0.90, "Strawberry", ["Pink Sprinkles", "Hearts"], "Chocolage")
cupcake_10 = Regular("Lemon Zest", 1.70, 0.85, "Lemon", ["Yellow Sprinkles"], "Amaretto")
cupcake_11 = Mini("Orange Burst", 2.10, 1.05, "Orange", ["Orange Sugar"])
cupcake_12 = Regular("Minty Fresh", 2.20, 1.10, "Mint", ["Green Sprinkles"], "Lemon")
cupcake_13 = Regular("Blueberry Blast", 2.30, 1.15, "Blueberry", ["Blue Sprinkles"], "Berry")
cupcake_14 = Mini("Raspberry Rage", 2.40, 1.20, "Raspberry", ["Red Sprinkles"])
cupcake_15 = Large("Caramel Crunch", 2.50, 1.250, "Caramel", ["Gold Sprinkles"], "Caramel")
cupcake_16 = Large("Coffee Kick", 2.60, 1.30, "Coffee", ["Chocolate Beans"], "Chocolate")


if __name__ == "__main__":
    
    empty_cart("order.csv")
    