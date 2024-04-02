import csv, pdb
import melons as csvfile

source = "melons.csv"
melon_dict = {}



class Melon():

    def __init__(self, melon_id, common_name, price_per_unit, image_url, color, is_it_seedless):

        self.id = melon_id
        self.name = common_name
        self.price = price_per_unit
        self.image = image_url
        self.color = color
        self.seedless = is_it_seedless

    def __repr__(self):
        return (f"{self.name}\n")

    def price_str(self):
        return f"${self.price:.2f}"
    

def import_melon_db(source):
    with open(source, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for each_melon in reader:
            melon_id = each_melon["melon_id"]       #declaring each component first
            new_melon = Melon(                      #instantiating the listed data into a Melon class first
                melon_id,
                each_melon["common_name"],
                float(each_melon["price"]),
                each_melon["image_url"],
                each_melon["color"],
                eval(each_melon["seedless"]))       #need to use eval() because bool() will take a "False" string to be True, eval() evaluates it in python code
            melon_dict[melon_id] = new_melon        #taking both id definition and new_melon dictionary and adding to melon_dict


def melon_lookup(melon_id):
    return melon_dict[melon_id]

def get_melon_list(dic):
    return list(dic.values())
    








if __name__ == "__main__":
    
    import_melon_db(source)




