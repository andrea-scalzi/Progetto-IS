import datetime
import json
import os

from progetto_IS.models.tessera import Tessera
from progetto_IS.models.utente import Utente

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "utenti.json")

class UserController:

    def load_users(self):
        with open(FILE_PATH, "r") as f:
            users_data = json.load(f)
            return [Utente.from_dict(user) for user in users_data]

    def save_users(self, users):
        with open(FILE_PATH, "w") as f:
            json.dump([user.to_dict() for user in users], f, indent=4)

    def set_tessera(self, username, telefono, codiceFiscale):
        users = self.load_users()

        for user in users:
            if user.username == username:
                if user.tessera and user.tessera.data_scadenza >= datetime.date.today():
                    return False

                user.tessera = Tessera(telefono, codiceFiscale)

                self.save_users(users)
                return True

        return False

    def create_user(self, nome, cognome, username, password, email):
        users = self.load_users()

        for user in users:
            if user.username == username:
                return False

        new_id = max([user.id for user in users], default=0) + 1
        new_user = Utente(new_id, nome, cognome, username, password, email)

        users.append(new_user)
        self.save_users(users)
        return True

    def update_user(self, updated_user):
        users = self.load_users()

        for i, user in enumerate(users):
            if user.id == updated_user.id:
                users[i] = updated_user
                self.save_users(users)
                return True

        return False

    def delete_user(self, username):
        users = self.load_users()

        updated_users = []
        for user in users:
            if user.username != username:
                updated_users.append(user)

        self.save_users(updated_users)
        return True

    def get_user(self, username):
        users = self.load_users()
        for user in users:
            if user.username == username:
                return user
        return None