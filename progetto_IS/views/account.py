from PyQt5 import QtCore, QtGui, QtWidgets

from progetto_IS.controllers.user_controller import UserController


class Ui_Account(object):
    def __init__(self, utente, admin):
        self.utente = utente
        self.admin = admin

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 900)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 361, 111))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 120, 361, 731))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.verticalLayout.addWidget(self.lineEdit_nome)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_cognome = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_cognome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cognome.setObjectName("lineEdit_cognome")
        self.verticalLayout.addWidget(self.lineEdit_cognome)
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
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.label_Tessera = QtWidgets.QLabel(self.layoutWidget)
        self.label_Tessera.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_Tessera.setObjectName("label_Tessera")
        self.verticalLayout.addWidget(self.label_Tessera, 0, QtCore.Qt.AlignHCenter)
        self.label_telefono = QtWidgets.QLabel(self.layoutWidget)
        self.label_telefono.setObjectName("label_telefono")
        self.verticalLayout.addWidget(self.label_telefono, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.verticalLayout.addWidget(self.lineEdit_telefono)
        self.label_codiceFiscale = QtWidgets.QLabel(self.layoutWidget)
        self.label_codiceFiscale.setObjectName("label_codiceFiscale")
        self.verticalLayout.addWidget(self.label_codiceFiscale, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_codiceFiscale = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_codiceFiscale.setObjectName("lineEdit_codiceFiscale")
        self.verticalLayout.addWidget(self.lineEdit_codiceFiscale)
        self.label_data_tesseramento = QtWidgets.QLabel(self.layoutWidget)
        self.label_data_tesseramento.setObjectName("label_data_tesseramento")
        self.verticalLayout.addWidget(self.label_data_tesseramento, 0, QtCore.Qt.AlignHCenter)
        self.label_data_scadenza = QtWidgets.QLabel(self.layoutWidget)
        self.label_data_scadenza.setObjectName("label_data_scadenza")
        self.verticalLayout.addWidget(self.label_data_scadenza, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.carica_dati_utente()

        if not self.utente.tessera:
            self.label_telefono.setVisible(False)
            self.label_codiceFiscale.setVisible(False)
            self.lineEdit_telefono.setVisible(False)
            self.lineEdit_codiceFiscale.setVisible(False)
            self.label_Tessera.setVisible(False)
            self.label_data_tesseramento.setVisible(False)
            self.label_data_scadenza.setVisible(False)

        self.pushButton_save.clicked.connect(self.salva_modifiche)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        if self.admin:
            self.label_5.setText(_translate("Form", "Modifica Utente"))
        else:
            self.label_5.setText(_translate("Form", "Il tuo profilo"))
        self.label_10.setText(_translate("Form", "Nome"))
        self.label_11.setText(_translate("Form", "Cognome"))
        self.label_6.setText(_translate("Form", "Username"))
        self.label_8.setText(_translate("Form", "Password"))
        self.label_12.setText(_translate("Form", "Email"))
        self.label_Tessera.setText(_translate("Form", "Dati Tessera"))
        self.label_telefono.setText(_translate("Form", "Numero di telefono"))
        self.label_codiceFiscale.setText(_translate("Form", "Codice fiscale"))
        self.label_data_tesseramento.setText(_translate("Form", "Data tesseramento:"))
        self.label_data_scadenza.setText(_translate("Form", "Data fine tesseramento:"))
        self.pushButton_save.setText(_translate("Form", "Conferma modifiche"))

    def carica_dati_utente(self):
        self.lineEdit_nome.setText(self.utente.nome)
        self.lineEdit_cognome.setText(self.utente.cognome)
        self.lineEdit_username.setText(self.utente.username)
        self.lineEdit_password.setText(self.utente.password)
        self.lineEdit_email.setText(self.utente.email)

        if self.utente.tessera:
            self.lineEdit_telefono.setText(self.utente.tessera.telefono)
            self.lineEdit_codiceFiscale.setText(self.utente.tessera.codice_fiscale)
            self.label_data_tesseramento.setText(f"Data tesseramento: {self.utente.tessera.data_tesseramento}")
            self.label_data_scadenza.setText(f"Data scadenza: {self.utente.tessera.data_scadenza}")

    def salva_modifiche(self):
        user_controller = UserController()

        self.utente.nome = self.lineEdit_nome.text()
        self.utente.cognome = self.lineEdit_cognome.text()
        self.utente.username = self.lineEdit_username.text()
        self.utente.password = self.lineEdit_password.text()
        self.utente.email = self.lineEdit_email.text()

        if not (self.utente.nome and self.utente.cognome and self.utente.username and self.utente.password and self.utente.email):
            QtWidgets.QMessageBox.warning(None, "Errore", "Tutti i campi sono obbligatori!")
            return

        if self.utente.tessera:
            self.utente.tessera.telefono = self.lineEdit_telefono.text()
            self.utente.tessera.codice_fiscale = self.lineEdit_codiceFiscale.text()

            if not (self.utente.tessera.telefono and self.utente.tessera.codice_fiscale):
                QtWidgets.QMessageBox.warning(None, "Errore", "Tutti i campi sono obbligatori!")
                return

        if user_controller.update_user(self.utente):
            QtWidgets.QMessageBox.information(None, "Successo", "Utente aggiornato!")
        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "Non è stato possibile aggiornare l'utente.")
