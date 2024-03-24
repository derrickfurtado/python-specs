class Dog():
    
    species = 'mammal'

    def __init__(self, dog_breed, dog_size, coat_color):

        self.breed = dog_breed
        self.size = dog_size
        self.color = coat_color
    
    def bark(self):
        if self.size == 'Small' or self.size == 'Medium':
            return "woof"
        elif self.size == "Large":
            return "WOOF!!!"







my_dog = Dog("Mutt", "Small", "Brown")
family_dog = Dog("Coton","Small","White")
my_favorite_dog = Dog("Doberman",'Large','Black')




print("ATTRIBUTE breed: ", my_dog.breed)
print("ATTRIBUTE size: ", my_dog.size)
print("ATTRBUTE color: ", my_dog.color)

print(f"Our dog is a {my_dog.size.lower()} {my_dog.breed} and he is {my_dog.color.lower()}. My Brother-in-Law's dog is a {family_dog.size.lower()} {family_dog.breed} and he is {family_dog.color.lower()}. They are both {my_dog.species}s. The dog I really want is a {my_favorite_dog.color} {my_favorite_dog.breed} because they are a {my_favorite_dog.size} breed")

print("Our dog sounds like: ", my_dog.bark())
print("My favorite dog sounds like: ", my_favorite_dog.bark())

print(type(my_dog))