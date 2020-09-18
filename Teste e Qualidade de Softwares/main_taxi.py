from taxi_v2 import Conta,Cliente,Corrida

cliente_1 = Cliente(15,"Rodrigo")
corrida_1 = Corrida(15)
conta_1 = Conta(15, cliente_1, corrida_1)

conta_1.encerrar_conta()
conta_1.imprimir_extrato()