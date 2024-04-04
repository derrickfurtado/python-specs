from pprint import pprint
import csv

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}>"

    def price_str(self):
        return f"${round(self.price, 2)}"

melon_dict = {}

with open("melons.csv", "r") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row["melon_id"]
        
        melon = Melon(melon_id, row["common_name"], float(row["price"]), row["image_url"], row["color"], eval(row["seedless"]))

        melon_dict[melon_id] = melon


# pprint(melon_dict)


def get_by_id(melon_id):
   return melon_dict[melon_id]

# print(get_by_id("fair"))

def get_all():
   return list(melon_dict.values())

# pprint(get_all())