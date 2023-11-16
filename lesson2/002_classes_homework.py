class Zoo
    def add_animals(self, animals):



    def count_animals(self):
        return len(self.__animals)

    def get_animals_by_species(self, species):
        species_list = []
        for animal in self.__animals:
            if animal.species == species:
                species_list.append(animal)
        return species_list

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.name == name:
                self.__animals.remove(animal)
                return
        print(f'Animal with name {name} is not in Zoo')

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(f'Feeding {animal.name} ({animal.species}). Ih has {animal.fur_color()} fur.')
            if isinstance(animal, Bird):
                print(f'Feeding {animal.name} ({animal.species}). Ih has {animal.fur_color()} mm wide wings.')
            if isinstance(animal, Reptile):
                print(f'Feeding {animal.name} ({animal.species}). Ih has {animal.fur_color()} scales.')

# You can use code below for testing purpouses if you want
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
    for reptile in reptiles:
        print(f'{reptile.name()} ({reptile.species()})')