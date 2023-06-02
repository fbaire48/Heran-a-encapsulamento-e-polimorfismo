#3 - Encapsulamento:
#    É o princípio que permite ocultar os detalhes internos de uma classe e expor apenas uma interface pública.

class Banco:
    def __init__(self):
        self.__saldo = 10
    
    def mostrar_saldo(self):
        return self.__saldo

a = Banco()
# print(a.__saldo)
#Traceback (most recent call last):
#  File "c:\Users\ALUNO\Downloads\encapsulamento.py", line 6, in <module>
#    print(a.__saldo)
#AttributeError: 'Banco' object has no attribute '__saldo'
print(a.mostrar_saldo()) # 10
a.__saldo = 20
print(a.mostrar_saldo()) # 10