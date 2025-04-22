from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from progetto_IS.controllers.auth_controller import AuthController
from progetto_IS.controllers.user_controller import UserController
from progetto_IS.views.home import Ui_Home
from progetto_IS.views.registrazione_utente import Ui_Registrazione


class Ui_Form(object):
    def __init__(self):
        self.auth_controller = AuthController()

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 10, 121, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../progetto_IS/img/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 120, 361, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_login = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_login.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_register = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_register.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout.addWidget(self.pushButton_register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.open_registrazione_utente)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Username"))
        self.label_8.setText(_translate("Form", "Password"))
        self.pushButton_login.setText(_translate("Form", "Accedi"))
        self.label_7.setText(_translate("Form", "Se non hai ancora un account"))
        self.pushButton_register.setText(_translate("Form", "Registrati"))

    def login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()

        if not username or not password:
            QMessageBox.warning(None, "Errore", "Inserisci username e password.")
            return

        if self.auth_controller.login(username, password):
            QMessageBox.information(None, "Successo", "Login effettuato con successo!")

            user_controller = UserController()

            user = user_controller.get_user(username)
            if user:
                self.open_home(username, user.isAdmin)
            else:
                QMessageBox.critical(None, "Errore", "Errore nel recupero dell'utente.")
        else:
            QMessageBox.critical(None, "Errore", "Username o password errati.")

    def open_registrazione_utente(self):
        self.registration_window = QtWidgets.QWidget()
        self.ui = Ui_Registrazione(admin=False)
        self.ui.setupUi(self.registration_window)
        self.registration_window.show()

    def open_home(self, username, is_admin):
        self.home_window = QtWidgets.QWidget()
        self.ui_home = Ui_Home(username, is_admin)
        self.ui_home.setupUi(self.home_window)

        self.home_window.show()
        QtWidgets.QApplication.processEvents()

        self.Form.close()
