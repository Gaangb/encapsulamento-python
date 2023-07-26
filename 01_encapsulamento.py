# O encapsulamento em python é feito por convenção. Dessa forma se usa o _saldo para torna-la private. 
# Neste codigo simples de conta bancaria demonstro o seu uso em um sistema de conta bancaria
# De forma alguma deve-se acessar o valor do saldo direto pelo _saldo. 
# Toda modificação precisa ser realizada através dos metodos públicos

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    

conta = Conta("00001", 100)
conta.depositar(100)
print(conta.mostrar_saldo())