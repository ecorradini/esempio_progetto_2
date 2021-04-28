class Servizio():

    def __init__(self, id, nome, tipo, posizione, prezzo):
        super(Servizio, self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.posizione = posizione
        self.prezzo = prezzo
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False