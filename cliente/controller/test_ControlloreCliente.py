from unittest import TestCase

from abbonamento.model.Abbonamento import Abbonamento
from cliente.model.Cliente import Cliente


class TestControlloreCliente(TestCase):

    def test_aggiungi_nuovo_abbonamento_cliente(self):
        self.cliente = Cliente(id="test", nome="test", cognome="test", cf="ABC", email="test@test.com", eta=23,
                               indirizzo="Via test", telefono="1234")
        self.assertIsNone(self.cliente.abbonamento)
        self.cliente.add_abbonamento(Abbonamento(scadenza="30/12/2022"))
        self.assertIsNotNone(self.cliente.abbonamento)