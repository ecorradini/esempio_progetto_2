class ControllorePrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        print(self.model.id)
        return self.model.id

    def get_cliente_prenotazione(self):
        return self.model.cliente

    def get_servizio_prenotazione(self):
        return self.model.servizio

    def get_data_prenotazione(self):
        return self.model.data