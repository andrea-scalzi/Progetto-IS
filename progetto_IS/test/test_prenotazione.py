import unittest

from progetto_IS.controllers.prenotazione_controller import PrenotazioneController


class TestPrenotazione(unittest.TestCase):

    def test_aggiunta_prenotazione(self):
        prenotazione_controller = PrenotazioneController()

        prenotazioni_iniziali = prenotazione_controller.load_prenotazioni()
        num_prenotazioni_iniziale = len(prenotazioni_iniziali)

        prenotazione_controller.create_prenotazione(
            "2025-05-05", "15:00", "17:00", "Campo Blu",
            ["a", "b"], ["c", "d"], "z"
        )

        prenotazioni_finali = prenotazione_controller.load_prenotazioni()
        num_prenotazioni_finale = len(prenotazioni_finali)

        self.assertEqual(num_prenotazioni_finale, num_prenotazioni_iniziale + 1)




