from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_servizio_prenotazione().nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding))

        label_cliente = QLabel("Cliente: {} {}".format(self.controller.get_cliente_prenotazione().nome, self.controller.get_cliente_prenotazione().cognome))
        font_cliente = label_cliente.font()
        font_cliente.setPointSize(30)
        label_cliente.setFont(font_cliente)
        v_layout.addWidget(label_cliente)

        label_data = QLabel("Data: {}".format(self.controller.get_data_prenotazione()))
        font_data = label_data.font()
        font_data.setPointSize(30)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_servizio_prenotazione().nome)

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()