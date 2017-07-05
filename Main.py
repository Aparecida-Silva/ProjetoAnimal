from Animal import Animal
from Cachorro import Cachorro
from Galinha import Galinha

def main():
    a1 = Animal("Max", 10, "Floresta")
    a2 = Cachorro("Junior", 4, "Casinha", "Branco")
    a3 = Galinha("Gluglu", 2, "Puleiro")
    a2.mover()
    a2.farejar()
    a3.mover()
    a3.ciscar()

    print(a1)
    print(a2)
    print(a3)

if (__name__ ==  "__main__"):
    main()
