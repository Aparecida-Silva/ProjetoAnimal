class Animal():
    def __init__(self, nome, numMembros, habitat):
        self.nome = nome
        self.numMembros = numMembros
        self.habitat = habitat
    def mover(self):
        print(self.nome + " movendo de forma genérica")

    def comer(self):
        print(self.nome + "comendo de forma genérica")

    def __str__(self):
        return "Nome: " + self.nome + ", numMembros: " + str(self.numMembros) + ", Habitat: " + self.habitat
