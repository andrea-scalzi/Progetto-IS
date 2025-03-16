from progetto_IS.models.tessera import Tessera

class Utente:
    def __init__(self, id, nome, cognome, username, password, email):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.email = email
        self.tesserato = False
        self.isAdmin = False

    def setTessera(self, telefono, codiceFiscale):
        self.tessera = Tessera(telefono, codiceFiscale)
        self.tesserato = True

    def getTesseramento(self):
        if self.tesserato:
            return True
        else:
            return False
