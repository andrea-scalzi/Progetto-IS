from progetto_IS.models.tessera import Tessera

class Utente:
    def __init__(self, id, nome, cognome, username, password, email, tessera=None, isAdmin=False):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.email = email
        self.tessera = tessera
        self.isAdmin = isAdmin

    @classmethod
    def from_dict(cls, data):
        tessera = Tessera.from_dict(data["tessera"]) if data.get("tessera") else None
        return cls(
            id=data["id"],
            nome=data["nome"],
            cognome=data["cognome"],
            username=data["username"],
            password=data["password"],
            email=data["email"],
            tessera=tessera,
            isAdmin=data.get("isAdmin", False)
        )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "tessera": self.tessera.to_dict() if self.tessera else None,
            "isAdmin": self.isAdmin
        }
