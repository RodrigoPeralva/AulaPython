from datetime import datetime, timedelta

class Cliente:
    def __init__(self, cpf, nome):
        self._cpf = cpf
        self._nome = nome

    def get_cpf(self):
        return self._cpf

    def get_nome(self):
        return self._nome

class Corrida:
    def __init__(self, id, horario_final = 0):
        self._id = id
        self._horario_final = horario_final

    def get_id(self):
        return self._id

    def set_horario_final(self, horario_final):
        self._horario_final = horario_final

    def get_horario_final(self):
        return self._horario_final

    # Não é necessário um set horario inicial, pois o inicio_corrida, já realiza a ação de SET.
    def get_horario_inicial(self):
        return datetime.now()

    def fim_corrida(self):
        # mock
        delta_tempo_mock = timedelta(hours=0, minutes=15, seconds=0)
        self.set_horario_final(self.get_horario_inicial() + delta_tempo_mock)

    def get_duracao_da_corrida(self):
        self.fim_corrida()
        self._duracao_da_corrida = ((self.get_horario_final() - self.get_horario_inicial()).seconds) / 60

        return self._duracao_da_corrida
    
    def bandeira(self):
        if ((self.get_horario_inicial().hour > 22) or (self.get_horario_inicial().hour < 6 )):
            return 2
        else:
            return 1

class Conta:
    def __init__(self, id, objeto_cliente, objeto_corrida):
        self._id = id
        self._cliente = objeto_cliente
        self._corrida = objeto_corrida

    def valor_inicial(self):
        return 5.50

    def encerrar_conta(self):
        if (self._corrida.bandeira() == 1):
            self._corrida_valor = self.valor_inicial() + (0.50*self._corrida.get_duracao_da_corrida())
        else:
            self._corrida_valor = self.valor_inicial() + (0.50*1.10*self._corrida.get_duracao_da_corrida())

    def extrato(self):
        print('***********************')
        print('Extrato da Corrida')
        print('***********************')
        print('CPF do cliente: {}'.format(self._cliente.get_cpf()))
        print('Nome cliente: {}'.format(self._cliente.get_nome()))
        print('***********************')
        print('Início da corrida: {}'.format(self._corrida.get_horario_inicial()))
        print('Término da corrida: {}'.format(self._corrida.get_horario_final()))
        print('Duração da corrida: {}'.format(self._corrida.get_duracao_da_corrida()))
        print('Valor da corrida: {}'.format(self._corrida_valor))
        print('***********************')
        print("{}".format(datetime.now()))
        print('***********************')

    def imprimir_extrato(self):
        self.extrato()
