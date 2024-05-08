class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
    
# Uso da classe
pessoa = Pessoa("Ana", 30)
print(pessoa.get_nome())
print(pessoa.get_idade())
