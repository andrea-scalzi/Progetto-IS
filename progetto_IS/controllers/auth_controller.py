from progetto_IS.controllers.user_controller import UserController

class AuthController:
    def __init__(self):
        self.user_controller = UserController()

    def login(self, username, password):
        users = self.user_controller.load_users()

        for user in users:
            if user.username == username and user.password == password:
                return True
        return False
