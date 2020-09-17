class Conta:
    def __init__(self, numero, saldo=0):
        self._saldo = saldo
        self._numero = numero

    def get_saldo(self):
        return self._saldo
    def get_numero(self):
        return self._numero
    def set_saldo(self, saldo):
        if(saldo < 0):
            print("Saldo não pode ser negativo.")
        else:
            self._saldo = saldo
    
    def extrato(self):
        print("O seu saldo é = {}".format(self.get_saldo()))
    def saque(self, valor):
        self.set_saldo( 
            self.get_saldo() - valor
        )
    def deposito(self, valor):
        self.set_saldo(
            self.get_saldo() + valor
        )
    