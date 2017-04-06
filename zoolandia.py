class Habitat:

    def __init__(self, marketing_name, industry_name):
        self.marketing_name = marketing_name
        self.industry_name = industry_name

island = Habitat("Galapagos", "Island")
jungle = Habitat("Dark Continent", "Jungle")
savannah = Habitat("Safari", "Savannah")





class Animal:

    def __init__(self, name, animal_type):
        self.name = name
        self.type = animal_type
        self.habitat = None

tommy = Animal("Tommy", "Tortoise")
tommy.habitat = island

danny = Animal("Danny", "Dodo")
danny.habitat = island

chester = Animal("Chester", "Cheetah")
chester.habitat = savannah

horton = Animal("Horton", "Elephant")
horton.habitat = jungle








class Zoo:
    """Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    """
    def __init__(self, name):
        self.zoo_name = name
        self.animals = set()
        self.habitats = set()
        self.visitors = list()


    def build_habitat(self, habitat):
        """Adds a habitats to the zoo

        Method arguments:
        -----------------
        habitat(object) -- A habitat instance
        """

        self.habitats.add(habitat)


    def sell_family_ticket(self, family):
        """Adds an entire family to the list of visitors

        Method argument:
        -----------------
        family(list) -- A list of people in a family of visitors
        """

        self.visitors.extend(family)


    def purchase_animal(self, animal):
        """Add an animal to the zoo

        Method arguments:
        -----------------
        animal(object) -- An animal instance
        """

        self.animals.add(animal)

    def animal_report(self):

        for habitat in self.habitats:
            print("\n\nHabitat:"+habitat.marketing_name)
            print("-------------------------")
            for animal in self.animals:
                if animal.habitat is habitat:
                    print(animal.name)


    def list_animals(self):
        """Lists all animals in the zoo

        Method arguments:
        n/a
        """

        [print("{} the {}".format(animal.name, animal.type)) for animal in self.animals]


a_zoo = Zoo("Zoolandia")
a_zoo.purchase_animal(tommy)
a_zoo.purchase_animal(chester)
a_zoo.purchase_animal(horton)
a_zoo.purchase_animal(danny)

a_zoo.build_habitat(savannah)
a_zoo.build_habitat(jungle)
a_zoo.build_habitat(island)

a_zoo.list_animals()

a_zoo.animal_report()

print("")
print(a_zoo.list_animals.__doc__) # To view the docstring for the method












