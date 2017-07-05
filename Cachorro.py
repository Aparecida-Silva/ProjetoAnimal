from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, numMembros, habitat, corPelo):
        super(Cachorro, self).__init__(nome, numMembros, habitat)
        self.corPelo = corPelo

    def mover(self):
        print("Cachorro está se movendo")

    def farejar(self):
        print("O cachorro está farejando")
