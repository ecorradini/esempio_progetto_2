from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from servizio.views.VistaServizio import VistaServizio


class VistaListaServizi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaServizi, self).__init__(parent)

        self.controller = ControlloreListaServizi()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_dei_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle('Lista Servizi')

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        servizio_selezionato = self.controller.get_servizio_by_index(selected)
        self.vista_servizio = VistaServizio(servizio_selezionato)
        self.vista_servizio.show()