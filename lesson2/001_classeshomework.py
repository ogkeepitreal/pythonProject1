class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species  

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        self.__species = species

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.__fur_color = fur_color

    def get_fur_color(self):
        return self.__fur_color

    def set_fur_color(self, fur_color):
        self.__fur_color = fur_color

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.__wing_span = wing_span

    def get_wing_span(self):
        return self.__wing_span

    def set_wing_span(self, wing_span):
        self.__wing_span = wing_span

class Reptile(Animal):
    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.__scale_type = scale_type

    def get_scale_type(self):
        return self.__scale_type

    def set_scale_type(self, scale_type):
        self.__scale_type = scale_type

class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def list_animals(self):
        for animal in self.__animals:
            print(f"Name: {animal.get_name()}, Species: {animal.get_species()}")

    def remove_animal(self, name):
        self.__animals = [animal for animal in self.__animals if animal.get_name() != name]

    def count_animals(self):
        return len(self.__animals)

    def get_animals_by_species(self, species):
        species_list = [animal for animal in self.__animals if animal.get_species() == species]
        for animal in species_list:
            print(f"Name: {animal.get_name()}, Species: {animal.get_species()}")

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(f'Feeding {animal.get_name()} the {animal.get_species()} with fur color {animal.get_fur_color()}')
            elif isinstance(animal, Bird):
                print(f'Feeding {animal.get_name()} the {animal.get_species()} with wing span {animal.get_wing_span()}')
            elif isinstance(animal, Reptile):
                print(f'Feeding {animal.get_name()} the {animal.get_species()} with scale type {animal.get_scale_type()}')


if __name__ == "__main__":
    zoo = Zoo()

    lion = Mammal('Simba', 'Lion', 'Golden')
    eagle = Bird('Baldy', 'Eagle', 100)
    python = Reptile('Monty', 'Python', 'Diamond')
    royal_python = Reptile('Muscle', 'Python', 'Triangle')

    zoo.add_animal(lion)
    zoo.add_animal(eagle)
    zoo.add_animal(python)
    zoo.add_animal(royal_python)

    print('Zoo animals:')
    zoo.list_animals()

    print('Feeding animals:')
    zoo.feed_animals()

    print('Removing animal:')
    zoo.remove_animal("Baldy")

    print('Zoon animals after removing:')
    zoo.list_animals()

    print('Total number of animals', zoo.count_animals())

    print('List all reptiles:')
    reptiles = zoo.get_animals_by_species('Python')
    if reptiles:
        for reptile in reptiles:
            print(f'{reptile.get_name()} ({reptile.get_species()})')
        else:
            print('No reptiles found in the zoo.')

