class ControlloreServizio():
    def __init__(self, servizio):
        self.model = servizio

    def get_nome_servizio(self):
        return self.model.nome

    def get_tipo_servizio(self):
        return self.model.tipo

    def get_posizione_servizio(self):
        return self.model.posizione

    def get_prezzo_servizio(self):
        return "{}".format(self.model.prezzo)

    def get_servizio_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"