class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 12)
woo = Parrot("Woo", 15)

# access the class attributes
print(f"Blu is a {blu.species}")
print(f"Woo is also a {woo.species}")

# access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")