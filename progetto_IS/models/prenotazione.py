class Prenotazione:
    def __init__(self, data, orario_inizio, orario_fine, campo, squadra1, squadra2, username):
        self.data = data
        self.orario_inizio = orario_inizio
        self.orario_fine = orario_fine
        self.campo = campo
        self.squadra1 = squadra1
        self.squadra2 = squadra2
        self.username = username

    @classmethod
    def from_dict(cls, data):
        return cls(
            data=data["data"],
            orario_inizio=data["orario_inizio"],
            orario_fine=data["orario_fine"],
            campo=data["campo"],
            squadra1=data.get("squadra1", []),
            squadra2=data.get("squadra2", []),
            username=data["username"]
        )

    def to_dict(self):
        return {
            "data": self.data,
            "orario_inizio": self.orario_inizio,
            "orario_fine": self.orario_fine,
            "campo": self.campo,
            "squadra1": self.squadra1,
            "squadra2": self.squadra2,
            "username": self.username
        }