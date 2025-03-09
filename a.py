class parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def ___init___(self, name, age):
        self.name = name
        self.age = age
        
#instantiate the parrot class
blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("Blu is a{}".format(blu.species))
print("Woo is also a {}" .format(blu.species))
