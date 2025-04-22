from PyQt5 import QtCore, QtWidgets

from progetto_IS.controllers.user_controller import UserController
from progetto_IS.views.account import Ui_Account
from progetto_IS.views.registrazione_utente import Ui_Registrazione
from progetto_IS.views.tesseramento import Ui_Tesseramento


class Ui_Lista(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1450, 575)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 1401, 241))
        self.tableWidget.setStyleSheet("QTableWidget::item:selected {\n"
"        background-color: rgb(244, 235, 236);\n"
"        color: black;\n"
"    }\n"
"QTableWidget:focus {\n"
"    border: none;\n"
"    outline: none;\n"
"}")
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(640, 0, 191, 61))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 1101, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.pushButton_creaUtente = QtWidgets.QPushButton(Form)
        self.pushButton_creaUtente.setGeometry(QtCore.QRect(650, 490, 171, 41))
        self.pushButton_creaUtente.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_creaUtente.setObjectName("pushButton_creaUtente")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(440, 410, 581, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(40)
        self.splitter.setObjectName("splitter")
        self.pushButton_modifica = QtWidgets.QPushButton(self.splitter)
        self.pushButton_modifica.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_modifica.setObjectName("pushButton_modifica")
        self.pushButton_tessera = QtWidgets.QPushButton(self.splitter)
        self.pushButton_tessera.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_tessera.setObjectName("pushButton_tessera")
        self.pushButton_elimina = QtWidgets.QPushButton(self.splitter)
        self.pushButton_elimina.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.pushButton_aggiorna = QtWidgets.QPushButton(Form)
        self.pushButton_aggiorna.setGeometry(QtCore.QRect(55, 380, 100, 30))
        self.pushButton_aggiorna.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_aggiorna.setObjectName("pushButton_aggiorna")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.load_lista_utenti()
        self.tableWidget.setCurrentItem(None)

        self.pushButton_modifica.clicked.connect(self.open_modifica_utente)
        self.pushButton_aggiorna.clicked.connect(self.load_lista_utenti)
        self.pushButton_tessera.clicked.connect(self.open_tessera_utente)
        self.pushButton_creaUtente.clicked.connect(self.open_aggiungi_utente)
        self.pushButton_elimina.clicked.connect(self.elimina_utente)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Lista Utenti"))
        self.label_2.setText(_translate("Form", "Seleziona un utente dalla lista per modificarlo, eliminarlo o tesserarlo, oppure creane uno nuovo."))
        self.pushButton_creaUtente.setText(_translate("Form", "Aggiungi Utente"))
        self.pushButton_modifica.setText(_translate("Form", "Modifica Utente"))
        self.pushButton_tessera.setText(_translate("Form", "Tessera Utente"))
        self.pushButton_elimina.setText(_translate("Form", "Elimina Utente"))
        self.pushButton_aggiorna.setText(_translate("Form","Aggiorna"))

    def load_lista_utenti(self):
        user_controller = UserController()
        users = user_controller.load_users()

        self.tableWidget.setRowCount(len(users))
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Nome", "Cognome", "Username", "Password", "Email", "Admin", "Tesserato",
            "Telefono", "CF", "Data T.", "Scadenza T."
        ])

        for row, user in enumerate(users):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user.nome))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user.cognome))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user.username))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("(nascosta)"))  # Password
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(user.email))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem("Sì" if user.isAdmin else "No"))

            if user.tessera:
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem("Sì"))  # Tessera
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(user.tessera.telefono))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(user.tessera.codice_fiscale))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(user.tessera.data_tesseramento)))
                self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(user.tessera.data_scadenza)))

            else:
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem("No"))  # Tessera
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem("N/A"))  # Telefono
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem("N/A"))  # Codice Fiscale
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem("N/A"))  # Data Tesseramento
                self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem("N/A"))  # Scadenza Tessera


    def get_utente_selezionato(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QtWidgets.QMessageBox.warning(None, "Errore", "Seleziona un utente prima di procedere.")
            return None

        username = self.tableWidget.item(selected_row, 3).text()

        user_controller = UserController()
        user = user_controller.get_user(username)

        if user:
            return user
        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "Utente non trovato.")
            return None

    def open_modifica_utente(self):
        user = self.get_utente_selezionato()
        if user:
            self.modifica_window = QtWidgets.QWidget()
            self.ui_modifica = Ui_Account(user, admin=True)
            self.ui_modifica.setupUi(self.modifica_window)

            self.modifica_window.show()

    def open_tessera_utente(self):
        user = self.get_utente_selezionato()
        if user:
            if user.isAdmin:
                QtWidgets.QMessageBox.critical(None, "Errore", "Gli admin non possono essere tesserati!")
                return
            if user.tessera:
                QtWidgets.QMessageBox.critical(None, "Errore", "L'utente è già tesserato!")
                return

            self.tesseramento_window = QtWidgets.QWidget()
            self.ui_tesseramento = Ui_Tesseramento(user.username, admin=True)
            self.ui_tesseramento.setupUi(self.tesseramento_window)

            self.tesseramento_window.show()

    def open_aggiungi_utente(self):
        self.registrazione_window = QtWidgets.QWidget()
        self.ui_registrazione = Ui_Registrazione(admin=True)
        self.ui_registrazione.setupUi(self.registrazione_window)

        self.registrazione_window.show()

    def elimina_utente(self):
        user = self.get_utente_selezionato()
        if not user:
            return

        conferma = QtWidgets.QMessageBox.question(
            None,
            "Conferma Eliminazione",
            f"Sei sicuro di voler eliminare l'utente '{user.username}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if conferma == QtWidgets.QMessageBox.Yes:
            user_controller = UserController()
            if user_controller.delete_user(user.username):
                QtWidgets.QMessageBox.information(None, "Successo", "Utente eliminato con successo.")
                self.load_lista_utenti()
            else:
                QtWidgets.QMessageBox.critical(None, "Errore", "Errore nell'eliminazione dell'utente.")
