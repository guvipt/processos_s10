class Contador:
    def __init__(self):
        self.__valor = 0

    def incrementar(self):
        self.__valor +=1

    def decrementar(self):
        if self.__valor>0:

           self.__valor -=1
   
        else:
            print("valor do contador ja e 0")

    def get_valor(self):
        return self.__valor

# Uso da classe
contador = Contador()
contador.incrementar()
contador.incrementar()
print(contador.get_valor())  # Deve mostrar 2
contador.decrementar()
print(contador.get_valor())  # Deve mostrar 1
