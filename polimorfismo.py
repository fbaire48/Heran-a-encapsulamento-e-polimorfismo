# 2 - Polimorfismo:
#   É o princípio que permite que objetos de diferentes classes sejam tratados de maneira uniforme, permitindo que um objeto seja referenciado através de uma referência de tipo mais geral e comportando-se de maneiras diferentes com base no tipo real do objeto. Isso promove a flexibilidade e a extensibilidade do código.

class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "Au au"

class Gato(Animal):
    def som(self):
        return "Miau"


def ouvir_som(animal):
    print(animal.som())


onix = Cachorro()
lex = Gato()

ouvir_som(onix)
ouvir_som(lex)

