from PyQt5 import QtCore, QtWidgets

from progetto_IS.controllers.backup_controller import BackupController


class Ui_Backup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 700)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(25, 270, 311, 401))
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 161, 61))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 130, 481, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_eseguiBackup = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eseguiBackup.sizePolicy().hasHeightForWidth())
        self.pushButton_eseguiBackup.setSizePolicy(sizePolicy)
        self.pushButton_eseguiBackup.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_eseguiBackup.setObjectName("pushButton_eseguiBackup")
        self.horizontalLayout.addWidget(self.pushButton_eseguiBackup)
        self.pushButton_ripristinaUltimo = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ripristinaUltimo.sizePolicy().hasHeightForWidth())
        self.pushButton_ripristinaUltimo.setSizePolicy(sizePolicy)
        self.pushButton_ripristinaUltimo.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_ripristinaUltimo.setObjectName("pushButton_ripristinaUltimo")
        self.horizontalLayout.addWidget(self.pushButton_ripristinaUltimo)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(360, 390, 221, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(90)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_ripristinaSelezionato = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ripristinaSelezionato.sizePolicy().hasHeightForWidth())
        self.pushButton_ripristinaSelezionato.setSizePolicy(sizePolicy)
        self.pushButton_ripristinaSelezionato.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_ripristinaSelezionato.setObjectName("pushButton_ripristinaSelezionato")
        self.verticalLayout.addWidget(self.pushButton_ripristinaSelezionato)
        self.pushButton_eliminaSelezionato = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eliminaSelezionato.sizePolicy().hasHeightForWidth())
        self.pushButton_eliminaSelezionato.setSizePolicy(sizePolicy)
        self.pushButton_eliminaSelezionato.setStyleSheet("background-color: rgb(244, 235, 236);")
        self.pushButton_eliminaSelezionato.setObjectName("pushButton_eliminaSelezionato")
        self.verticalLayout.addWidget(self.pushButton_eliminaSelezionato)

        self.retranslateUi(Form)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.controller = BackupController()

        self.pushButton_eseguiBackup.clicked.connect(self.esegui_backup)
        self.pushButton_ripristinaUltimo.clicked.connect(self.ripristina_ultimo_backup)
        self.pushButton_ripristinaSelezionato.clicked.connect(self.ripristina_backup_selezionato)
        self.pushButton_eliminaSelezionato.clicked.connect(self.elimina_backup_selezionato)

        self.carica_backup_disponibili()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Backup"))
        self.pushButton_eseguiBackup.setText(_translate("Form", "Esegui il Backup"))
        self.pushButton_ripristinaUltimo.setText(_translate("Form", "Ripristina ultimo Backup"))
        self.pushButton_ripristinaSelezionato.setText(_translate("Form", "Ripristina Backup selezionato"))
        self.pushButton_eliminaSelezionato.setText(_translate("Form", "Elimina Backup selezionato"))

    def esegui_backup(self):
        if self.controller.esegui_backup():
            QtWidgets.QMessageBox.information(None, "Successo", "Backup eseguito correttamente.")
            self.carica_backup_disponibili()
        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante il backup.")

    def ripristina_ultimo_backup(self):
        backup_list = self.controller.lista_backup()
        if backup_list:
            ultimo_backup = backup_list[0]
            if self.controller.ripristina_backup(ultimo_backup):
                QtWidgets.QMessageBox.information(None, "Successo", "Backup ripristinato con successo.")
            else:
                QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante il ripristino.")
        else:
            QtWidgets.QMessageBox.warning(None, "Errore", "Nessun backup disponibile.")

    def ripristina_backup_selezionato(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            backup_name = selected_item.text()
            if self.controller.ripristina_backup(backup_name):
                QtWidgets.QMessageBox.information(None, "Successo", "Backup ripristinato con successo.")
            else:
                QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante il ripristino.")

    def elimina_backup_selezionato(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            backup_name = selected_item.text()
            if self.controller.elimina_backup(backup_name):
                QtWidgets.QMessageBox.information(None, "Successo", "Backup eliminato con successo.")
                self.carica_backup_disponibili()
            else:
                QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante l'eliminazione.")

    def carica_backup_disponibili(self):
        self.listWidget.clear()
        for backup in self.controller.lista_backup():
            self.listWidget.addItem(backup)
