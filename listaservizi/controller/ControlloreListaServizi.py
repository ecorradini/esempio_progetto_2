from listaservizi.model.ListaServizi import ListaServizi


class ControlloreListaServizi():

    def __init__(self):
        super(ControlloreListaServizi, self).__init__()
        self.model = ListaServizi()

    def get_lista_dei_servizi(self):
        return self.model.get_lista_servizi()

    def get_servizio_by_index(self, index):
        return self.model.get_servizio_by_index(index)

    def save_data(self):
        self.model.save_data()