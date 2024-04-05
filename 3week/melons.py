import csv


melon_dict = {}

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self. price = float(price)
        self.image_url = image_url
        self.color = color
        self.seedless = eval(seedless)

    def __repr__(self):
        return (
            f"This is the class object for: {self.common_name}\n"
            )
    
    def price_str(self):
        return f"${self.price:.2f}"



def import_melon_data(source):
    with open(source, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            melon_id = row["melon_id"]

            melon = Melon(
                melon_id, 
                row["common_name"], 
                row["price"], 
                row["image_url"],  
                row["color"], 
                row["seedless"])
            
            melon_dict[melon_id] = melon


def get_by_id(melon_id):
    return melon_dict[melon_id]

def get_all():
    return list(melon_dict.values())




import_melon_data("melons.csv")














    

