from PyQt5 import QtCore, QtGui, QtWidgets

from progetto_IS.controllers.user_controller import UserController
from progetto_IS.views.account import Ui_Account
from progetto_IS.views.backup import Ui_Backup
from progetto_IS.views.lista_utenti import Ui_Lista
from progetto_IS.views.prenotazioni import Ui_Prenotazioni
from progetto_IS.views.tesseramento import Ui_Tesseramento


class Ui_Home(object):
    def __init__(self, username, is_admin):
        self.username = username
        self.is_admin = is_admin

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 700)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_esci = QtWidgets.QPushButton(Form)
        self.pushButton_esci.setGeometry(QtCore.QRect(330, 610, 131, 51))
        self.pushButton_esci.setStyleSheet("background-color: #F4EBEC;\n"
"")
        self.pushButton_esci.setObjectName("pushButton_esci")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 10, 221, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../progetto_IS/img/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 260, 671, 81))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(60, 430, 671, 111))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_listaUtenti = QtWidgets.QPushButton(self.splitter)
        self.pushButton_listaUtenti.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #F4EBEC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 2px solid #1C69A5; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   border: 4px solid #1C69A5;\n"
"}")
        self.pushButton_listaUtenti.setObjectName("pushButton_listaUtenti")
        self.pushButton_prenotazioni = QtWidgets.QPushButton(self.splitter)
        self.pushButton_prenotazioni.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #F4EBEC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 2px solid #F7D025; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   border: 4px solid #F7D025;\n"
"}")
        self.pushButton_prenotazioni.setObjectName("pushButton_prenotazioni")
        self.pushButton_backup = QtWidgets.QPushButton(self.splitter)
        self.pushButton_backup.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #F4EBEC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 2px solid #1C69A5; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   border: 4px solid #1C69A5;\n"
"}")
        self.pushButton_backup.setObjectName("pushButton_backup")
        self.pushButton_tesseramento = QtWidgets.QPushButton(self.splitter)
        self.pushButton_tesseramento.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #F4EBEC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 2px solid #1C69A5; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   border: 4px solid #1C69A5;\n"
"}")
        self.pushButton_tesseramento.setObjectName("pushButton_tesseramento")
        self.pushButton_account = QtWidgets.QPushButton(self.splitter)
        self.pushButton_account.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: #F4EBEC;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 2px solid #F7D025; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   border: 4px solid #F7D025;\n"
"}")
        self.pushButton_account.setObjectName("pushButton_account")

        self.pushButton_listaUtenti.setFixedWidth(215)
        self.pushButton_prenotazioni.setFixedWidth(215)
        self.pushButton_backup.setFixedWidth(215)
        self.pushButton_tesseramento.setFixedWidth(215)
        self.pushButton_account.setFixedWidth(215)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if not self.is_admin:
            self.pushButton_listaUtenti.setVisible(False)
            self.pushButton_backup.setVisible(False)
        else:
            self.pushButton_tesseramento.setVisible(False)
            self.pushButton_account.setVisible(False)

        self.pushButton_esci.clicked.connect(self.esci)
        self.pushButton_listaUtenti.clicked.connect(self.open_lista_utenti)
        self.pushButton_prenotazioni.clicked.connect(self.open_prenotazioni)
        self.pushButton_backup.clicked.connect(self.open_backup)
        self.pushButton_tesseramento.clicked.connect(self.open_tesseramento)
        self.pushButton_account.clicked.connect(self.open_account)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_esci.setText(_translate("Form", "Esci"))
        self.label_2.setText(_translate("Form", f"Benvenuto/a, {self.username}!"))
        self.pushButton_listaUtenti.setText(_translate("Form", "Gestione Utenti"))
        self.pushButton_prenotazioni.setText(_translate("Form", "Prenotazioni"))
        self.pushButton_backup.setText(_translate("Form", "Backup"))
        self.pushButton_tesseramento.setText(_translate("Form", "Tesseramento"))
        self.pushButton_account.setText(_translate("Form", "Gestione Account"))

    def esci(self):
        QtWidgets.QApplication.quit()

    def open_lista_utenti(self):
        self.lista_window = QtWidgets.QWidget()
        self.ui_lista = Ui_Lista()
        self.ui_lista.setupUi(self.lista_window)

        self.lista_window.show()

    def open_prenotazioni(self):
        user_controller = UserController()
        utente = user_controller.get_user(self.username)

        self.prenotazioni_window = QtWidgets.QWidget()
        if self.is_admin:
            self.ui_prenotazioni = Ui_Prenotazioni(utente, admin=True)
        else:
            self.ui_prenotazioni = Ui_Prenotazioni(utente, admin=False)
        self.ui_prenotazioni.setupUi(self.prenotazioni_window)

        self.prenotazioni_window.show()

    def open_backup(self):
        self.backup_window = QtWidgets.QWidget()
        self.ui_backup = Ui_Backup()
        self.ui_backup.setupUi(self.backup_window)

        self.backup_window.show()

    def open_tesseramento(self):
        self.tesseramento_window = QtWidgets.QWidget()
        self.ui_tesseramento = Ui_Tesseramento(self.username, admin=False)
        self.ui_tesseramento.setupUi(self.tesseramento_window)

        self.tesseramento_window.show()

    def open_account(self):
        user_controller = UserController()
        utente = user_controller.get_user(self.username)

        self.account_window = QtWidgets.QWidget()
        self.ui_account = Ui_Account(utente, admin=False)
        self.ui_account.setupUi(self.account_window)

        self.account_window.show()
