import json
import os

from progetto_IS.models.prenotazione import Prenotazione

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "prenotazioni.json")

class PrenotazioneController:

    def load_prenotazioni(self):
        with open(FILE_PATH, "r") as f:
            prenotazioni_data = json.load(f)
            return [Prenotazione.from_dict(p) for p in prenotazioni_data]

    def save_prenotazioni(self, prenotazioni):
        with open(FILE_PATH, "w") as f:
            json.dump([p.to_dict() for p in prenotazioni], f, indent=4)

    def create_prenotazione(self, data, orario_inizio, orario_fine, campo, squadra1, squadra2, username):
        prenotazioni = self.load_prenotazioni()

        for prenotazione in prenotazioni:
            if prenotazione.data == data and prenotazione.campo == campo:
                if not (orario_fine <= prenotazione.orario_inizio or orario_inizio >= prenotazione.orario_fine):
                    return False

        nuova_prenotazione = Prenotazione(data, orario_inizio, orario_fine, campo, squadra1, squadra2, username)
        prenotazioni.append(nuova_prenotazione)
        self.save_prenotazioni(prenotazioni)
        return True

    def get_prenotazioni_per_data(self, data):
        prenotazioni = self.load_prenotazioni()
        return [p for p in prenotazioni if p.data == data]

    def update_prenotazione(self, prenotazione, nuovo_campo, nuovo_orario_inizio, nuovo_orario_fine, nuova_squadra1, nuova_squadra2):
        prenotazioni = self.load_prenotazioni()

        for p in prenotazioni:
            if (p.data == prenotazione.data and
                    p.orario_inizio == prenotazione.orario_inizio and
                    p.orario_fine == prenotazione.orario_fine and
                    p.campo == prenotazione.campo and
                    p.username == prenotazione.username):
                p.campo = nuovo_campo
                p.orario_inizio = nuovo_orario_inizio
                p.orario_fine = nuovo_orario_fine
                p.squadra1 = nuova_squadra1
                p.squadra2 = nuova_squadra2
                self.save_prenotazioni(prenotazioni)
                return True

        return False

    def delete_prenotazione(self, prenotazione_da_eliminare):
        prenotazioni = self.load_prenotazioni()

        nuove_prenotazioni = [
            p for p in prenotazioni if not (
                    p.data == prenotazione_da_eliminare.data and
                    p.orario_inizio == prenotazione_da_eliminare.orario_inizio and
                    p.orario_fine == prenotazione_da_eliminare.orario_fine and
                    p.campo == prenotazione_da_eliminare.campo and
                    p.username == prenotazione_da_eliminare.username
            )
        ]

        if len(nuove_prenotazioni) < len(prenotazioni):
            self.save_prenotazioni(nuove_prenotazioni)
            return True

        return False