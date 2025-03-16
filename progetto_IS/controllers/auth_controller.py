import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "utenti.json")

class AuthController:
    def __init__(self):
        if not os.path.exists(FILE_PATH):
            raise FileNotFoundError(f"Errore: il file {FILE_PATH} non esiste.")

    def load_users(self):
        with open(FILE_PATH, "r") as f:
            return json.load(f)

    def save_users(self, users):
        with open(FILE_PATH, "w") as f:
            json.dump(users, f, indent=4)

    def authenticate(self, username, password):
        users = self.load_users()

        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
        return False

    def register_user(self, nome, cognome, username, password, email):
        users = self.load_users()

        # Controllo se esiste un altro utente con lo stesso username
        for user in users:
            if user["username"] == username:
                return False

        # Creo un ID univoco
        new_id = max([user["id"] for user in users], default=0) + 1

        new_user = {
            "id": new_id,
            "nome": nome,
            "cognome": cognome,
            "username": username,
            "password": password,
            "email": email,
            "telefono": "",
            "codice_fiscale": "",
            "tessera": "",
            "isAdmin": False
        }

        users.append(new_user)
        self.save_users(users)
        return True
