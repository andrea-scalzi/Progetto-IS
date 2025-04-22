import datetime

class Tessera:
    def __init__(self, telefono, codice_fiscale):
        self.telefono = telefono
        self.codice_fiscale = codice_fiscale
        self.data_tesseramento = datetime.date.today()
        self.data_scadenza = self.data_tesseramento + datetime.timedelta(days=365)

    @classmethod
    def from_dict(cls, data):
        tessera = cls(data["telefono"], data["codice_fiscale"])
        tessera.data_tesseramento = datetime.date.fromisoformat(data["data_tesseramento"])
        tessera.data_scadenza = datetime.date.fromisoformat(data["data_scadenza"])
        return tessera

    def to_dict(self):
        return {
            "telefono": self.telefono,
            "codice_fiscale": self.codice_fiscale,
            "data_tesseramento": self.data_tesseramento.isoformat(),
            "data_scadenza": self.data_scadenza.isoformat()
        }
