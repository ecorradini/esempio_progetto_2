from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from abbonamento.views.VistaAbbonamento import VistaAbbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_cliente()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_cliente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_cliente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_cliente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_cliente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_abbonamento = QPushButton("Abbonamento")
        btn_abbonamento.clicked.connect(self.check_abbonamento)
        v_layout.addWidget(btn_abbonamento)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(), self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()