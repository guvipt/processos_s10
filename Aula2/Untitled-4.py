class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo protegido

    def depositar(self,valor):
       
           self._saldo += valor
           print("valor depositado")


    def get_saldo(self):
        return self._saldo 

# Uso da classe
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.get_saldo())
