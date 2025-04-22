import unittest
from progetto_IS.models.utente import Utente

class TestUtente(unittest.TestCase):

    def test_from_dict(self):
        data = {
            "id": 1,
            "nome": "Mario",
            "cognome": "Rossi",
            "username": "mr",
            "password": "123",
            "email": "mr@email.it",
            "tessera": {
                "telefono": "12345",
                "codice_fiscale": "MR1234",
                "data_tesseramento": "2025-03-22",
                "data_scadenza": "2026-03-22"
            },
            "isAdmin": False
        }

        utente = Utente.from_dict(data)

        self.assertIsInstance(utente, Utente)

