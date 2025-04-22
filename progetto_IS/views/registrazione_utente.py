from PyQt5 import QtCore, QtWidgets

from progetto_IS.controllers.user_controller import UserController


class Ui_Registrazione(object):
    def __init__(self, admin):
        self.admin = admin

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 700)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 361, 111))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 120, 361, 511))
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

        if self.admin:
            spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            self.verticalLayout.addItem(spacerItem)
            self.checkBox_admin = QtWidgets.QCheckBox("Assegna ruolo di amministratore", self.layoutWidget)
            self.checkBox_admin.setObjectName("checkBox_admin")
            self.checkBox_admin.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.verticalLayout.addWidget(self.checkBox_admin, 0, QtCore.Qt.AlignHCenter)

        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_save.clicked.connect(self.registra_utente)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Crea un nuovo account"))
        self.label_10.setText(_translate("Form", "Nome"))
        self.label_11.setText(_translate("Form", "Cognome"))
        self.label_6.setText(_translate("Form", "Username"))
        self.label_8.setText(_translate("Form", "Password"))
        self.label_12.setText(_translate("Form", "Email"))
        self.pushButton_save.setText(_translate("Form", "Crea Account"))

    def registra_utente(self):
        nome = self.lineEdit_nome.text().strip()
        cognome = self.lineEdit_cognome.text().strip()
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        email = self.lineEdit_email.text().strip()

        if not (nome and cognome and username and password and email):
            QtWidgets.QMessageBox.warning(None, "Errore", "Tutti i campi sono obbligatori!")
            return

        user_controller = UserController()

        if user_controller.create_user(nome, cognome, username, password, email):
            QtWidgets.QMessageBox.information(None, "Successo", "Registrazione avvenuta con successo!")

            if self.admin and self.checkBox_admin.isChecked():
                utente = user_controller.get_user(username)
                if utente:
                    utente.isAdmin = True
                    user_controller.update_user(utente)

        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "Username già in uso, scegli un altro nome utente.")
