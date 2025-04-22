from PyQt5 import QtCore, QtGui, QtWidgets

from progetto_IS.controllers.user_controller import UserController


class Ui_Tesseramento(object):
    def __init__(self, username, admin):
        self.username = username
        self.admin = admin

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_messaggio = QtWidgets.QLabel(Form)
        self.label_messaggio.setGeometry(QtCore.QRect(60, 10, 381, 201))
        self.label_messaggio.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_messaggio.setTextFormat(QtCore.Qt.AutoText)
        self.label_messaggio.setScaledContents(True)
        self.label_messaggio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_messaggio.setWordWrap(True)
        self.label_messaggio.setObjectName("label_messaggio")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 220, 361, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_telefono = QtWidgets.QLabel(self.layoutWidget)
        self.label_telefono.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_telefono.setObjectName("label_telefono")
        self.verticalLayout.addWidget(self.label_telefono, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.verticalLayout.addWidget(self.lineEdit_telefono)
        self.label_codiceFiscale = QtWidgets.QLabel(self.layoutWidget)
        self.label_codiceFiscale.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_codiceFiscale.setObjectName("label_codiceFiscale")
        self.verticalLayout.addWidget(self.label_codiceFiscale, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_codiceFiscale = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_codiceFiscale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_codiceFiscale.setObjectName("lineEdit_codiceFiscale")
        self.verticalLayout.addWidget(self.lineEdit_codiceFiscale)
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_iscrizione = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_iscrizione.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_iscrizione.setObjectName("pushButton_iscrizione")
        self.verticalLayout.addWidget(self.pushButton_iscrizione)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.user_controller = UserController()

        self.pushButton_iscrizione.clicked.connect(self.iscrizione)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        if self.admin:
            self.label_messaggio.setText(_translate("Form", "Puoi tesserare un utente inserendo il suo numero di telefono e il suo codice fiscale nei campi qui sotto."))
            self.pushButton_iscrizione.setText(_translate("Form", "Iscrivi"))
        else:
            self.label_messaggio.setText(_translate("Form", "La tessera ha validità annuale e offre sconti su ogni prenotazione. Tesserarsi è facile e veloce, basta inserire il tuo numero di telefono e il codice fiscale."))
            self.pushButton_iscrizione.setText(_translate("Form", "Iscriviti"))
        self.label_telefono.setText(_translate("Form", "Numero di telefono"))
        self.label_codiceFiscale.setText(_translate("Form", "Codice fiscale"))

    def iscrizione(self):
        telefono = self.lineEdit_telefono.text().strip()
        codice_fiscale = self.lineEdit_codiceFiscale.text().strip()

        if not telefono or not codice_fiscale:
            QtWidgets.QMessageBox.warning(None, "Errore", "Tutti i campi sono obbligatori!")
            return

        if self.user_controller.set_tessera(self.username, telefono, codice_fiscale):
            QtWidgets.QMessageBox.information(None, "Successo", "Tesseramento completato con successo!")
        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "È già attiva una tessera.")
