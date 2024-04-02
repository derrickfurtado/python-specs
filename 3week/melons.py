import csv, pdb
import melons as csvfile

source = "melons.csv"



class Melon():

    def __init__(self, melon_id, common_name, price_per_unit, image_url, color, is_it_seedless):

        self.id = melon_id
        self.name = common_name
        self.price = price_per_unit
        self.image = image_url
        self.color = color
        self.seedless = is_it_seedless


melon_dict = {}

def import_melon_db(source):
    with open(source, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for each_melon in reader:
            melon_id = each_melon["melon_id"]       #declaring each component first
            new_melon = Melon(                      #instantiating the melon first
                melon_id,
                each_melon["common_name"],
                float(each_melon["price"]),
                each_melon["image_url"],
                each_melon["color"],
                eval(each_melon["seedless"]))
            melon_dict[melon_id] = new_melon        #taking both id definition and new_melon dictionary and adding to melon_dict



import_melon_db(source)

pdb.set_trace()