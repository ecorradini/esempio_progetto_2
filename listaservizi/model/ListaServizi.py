import json
import pickle
import os.path

from servizio.model.Servizio import Servizio


class ListaServizi():

    def __init__(self):
        super(ListaServizi, self).__init__()
        self.lista_servizi = []
        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as f:
                self.lista_servizi = pickle.load(f)
        else:
            with open('listaservizi/data/lista_servizi_iniziali.json') as f:
                lista_servizi_iniziali = json.load(f)
            for servizio_iniziale in lista_servizi_iniziali:
                self.aggiungi_servizio(Servizio(servizio_iniziale["id"], servizio_iniziale["nome"],
                                                servizio_iniziale["tipo"], servizio_iniziale["posizione"],
                                                servizio_iniziale["prezzo"]))

    def aggiungi_servizio(self, servizio):
        self.lista_servizi.append(servizio)

    def get_servizio_by_index(self, index):
        return self.lista_servizi[index]

    def get_lista_servizi(self):
        return self.lista_servizi

    def save_data(self):
        with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_servizi, handle, pickle.HIGHEST_PROTOCOL)