# 1 - Herança:
#   É a criação de uma classe a partir de outra classe existente, permitindo que a nova classe herde os atributos e métodos da classe existente.

class One:
    def __init__(self, nome) -> None:
        self.nome = nome

class Two(One):
    def __init__(self, nome) -> None:
        super().__init__(nome)

a = Two("Nicolas")
print(a.nome)