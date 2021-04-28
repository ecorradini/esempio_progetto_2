from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaservizi.views.VistaListaServizi import VistaListaServizi


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Servizi", self.go_lista_servizi), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Stabilimento PRO")

    '''
    Questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_clienti(self):
        pass

    def go_lista_dipendenti(self):
        pass

    def go_lista_prenotazioni(self):
        pass