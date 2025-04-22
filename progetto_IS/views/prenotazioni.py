from PyQt5 import QtCore, QtWidgets

from progetto_IS.controllers.prenotazione_controller import PrenotazioneController


class Ui_Prenotazioni(object):
    def __init__(self, utente, admin):
        self.utente = utente
        self.admin = admin
        self.controller = PrenotazioneController()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 800)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 20, 501, 341))
        self.calendarWidget.setStyleSheet("QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
" background-color: #1C69A5;\n"
"}\n"
"QCalendarWidget QToolButton {\n"
" color: white;\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
" background-color: #0C2F68; \n"
"}")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.selectionChanged.connect(self.imposta_orari)
        self.calendarWidget.selectionChanged.connect(self.carica_lista_prenotazioni)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(45, 400, 1401, 361))
        self.tableWidget.setStyleSheet("QTableWidget::item:selected {\n"
"        background-color: rgb(244, 235, 236);\n"
"        color: black;\n"
"    }")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(455)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(1010, 70, 421, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(12, 47, 104);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit_g1s1 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_g1s1.sizePolicy().hasHeightForWidth())
        self.lineEdit_g1s1.setSizePolicy(sizePolicy)
        self.lineEdit_g1s1.setObjectName("lineEdit_g1s1")
        self.verticalLayout.addWidget(self.lineEdit_g1s1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lineEdit_g2s1 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_g2s1.sizePolicy().hasHeightForWidth())
        self.lineEdit_g2s1.setSizePolicy(sizePolicy)
        self.lineEdit_g2s1.setObjectName("lineEdit_g2s1")
        self.verticalLayout.addWidget(self.lineEdit_g2s1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(247, 208, 37);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lineEdit_g1s2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_g1s2.sizePolicy().hasHeightForWidth())
        self.lineEdit_g1s2.setSizePolicy(sizePolicy)
        self.lineEdit_g1s2.setObjectName("lineEdit_g1s2")
        self.verticalLayout_2.addWidget(self.lineEdit_g1s2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.lineEdit_g2s2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_g2s2.sizePolicy().hasHeightForWidth())
        self.lineEdit_g2s2.setSizePolicy(sizePolicy)
        self.lineEdit_g2s2.setObjectName("lineEdit_g2s2")
        self.verticalLayout_2.addWidget(self.lineEdit_g2s2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(640, 120, 251, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.timeEdit_inizio = QtWidgets.QTimeEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_inizio.sizePolicy().hasHeightForWidth())
        self.timeEdit_inizio.setSizePolicy(sizePolicy)
        self.timeEdit_inizio.setObjectName("timeEdit_inizio")
        self.verticalLayout_3.addWidget(self.timeEdit_inizio)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.timeEdit_fine = QtWidgets.QTimeEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_fine.sizePolicy().hasHeightForWidth())
        self.timeEdit_fine.setSizePolicy(sizePolicy)
        self.timeEdit_fine.setObjectName("timeEdit_fine")
        self.verticalLayout_3.addWidget(self.timeEdit_fine)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(640, 20, 251, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.comboBox_campi = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_campi.sizePolicy().hasHeightForWidth())
        self.comboBox_campi.setSizePolicy(sizePolicy)
        self.comboBox_campi.setEditable(False)
        self.comboBox_campi.setCurrentText("")
        self.comboBox_campi.setObjectName("comboBox_campi")
        self.comboBox_campi.addItems(["Campo Verde", "Campo Blu", "Campo Rosso (coperto)"])
        self.verticalLayout_4.addWidget(self.comboBox_campi)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(620, 330, 831, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_prenota = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_prenota.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(244, 235, 236);")
        self.pushButton_prenota.setObjectName("pushButton_prenota")
        self.horizontalLayout_2.addWidget(self.pushButton_prenota)
        self.pushButton_modifica = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_modifica.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(244, 235, 236);")
        self.pushButton_modifica.setCheckable(False)
        self.pushButton_modifica.setChecked(False)
        self.pushButton_modifica.setObjectName("pushButton_modifica")
        self.horizontalLayout_2.addWidget(self.pushButton_modifica)
        self.pushButton_elimina = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_elimina.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(244, 235, 236);")
        self.pushButton_elimina.setCheckable(False)
        self.pushButton_elimina.setChecked(False)
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.horizontalLayout_2.addWidget(self.pushButton_elimina)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if not self.admin:
                self.lineEdit_g1s1.setText(self.utente.nome + " " + self.utente.cognome)
                self.lineEdit_g1s1.setReadOnly(True)

        self.pushButton_modifica.setEnabled(False)
        self.pushButton_elimina.setEnabled(False)

        self.imposta_orari()
        self.configura_lista()
        self.carica_lista_prenotazioni()
        self.calendarWidget.selectionChanged.connect(self.carica_lista_prenotazioni)
        self.tableWidget.cellClicked.connect(self.seleziona_prenotazione)

        self.pushButton_prenota.clicked.connect(self.prenota_campo)
        self.pushButton_elimina.clicked.connect(self.elimina_prenotazione)
        self.pushButton_modifica.clicked.connect(self.modifica_prenotazione)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(False)
        self.label.setText(_translate("Form", "Squadra 1"))
        self.label_2.setText(_translate("Form", "Squadra 2"))
        self.label_3.setText(_translate("Form", "Orario Inizio"))
        self.timeEdit_inizio.setDisplayFormat(_translate("Form", "HH:00"))
        self.label_4.setText(_translate("Form", "Orario Fine"))
        self.timeEdit_fine.setDisplayFormat(_translate("Form", "HH:00"))
        self.label_5.setText(_translate("Form", "Seleziona un campo"))
        self.pushButton_prenota.setText(_translate("Form", "Prenota"))
        self.pushButton_modifica.setText(_translate("Form", "Modifica"))
        self.pushButton_elimina.setText(_translate("Form", "Elimina"))

    def imposta_orari(self):
            mese_corrente = self.calendarWidget.selectedDate().month()

            if 4 <= mese_corrente <= 9:
                    ora_min = QtCore.QTime(9, 0)
                    ora_max = QtCore.QTime(23, 0)
            else:
                    ora_min = QtCore.QTime(10, 0)
                    ora_max = QtCore.QTime(22, 0)

            self.timeEdit_inizio.setTime(ora_min)
            self.timeEdit_fine.setTime(ora_max)

            self.timeEdit_inizio.setMinimumTime(ora_min)
            self.timeEdit_inizio.setMaximumTime(ora_max.addSecs(-3600))
            self.timeEdit_fine.setMinimumTime(ora_min.addSecs(+3600))
            self.timeEdit_fine.setMaximumTime(ora_max)

    def configura_lista(self):
            ora_inizio = self.timeEdit_inizio.minimumTime()
            ora_fine = self.timeEdit_fine.maximumTime()

            orari = []
            while ora_inizio < ora_fine:
                    orari.append(ora_inizio.toString("HH:00"))
                    ora_inizio = ora_inizio.addSecs(3600)
            orari.append(ora_fine.toString("HH:00"))

            campi = ["Campo Verde", "Campo Blu", "Campo Rosso (coperto)"]

            self.tableWidget.setRowCount(len(orari))
            self.tableWidget.setColumnCount(len(campi))

            self.tableWidget.setHorizontalHeaderLabels(campi)

            for riga, ora in enumerate(orari):
                    item = QtWidgets.QTableWidgetItem(ora)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setVerticalHeaderItem(riga, item)

            self.tableWidget.clearContents()

    def carica_lista_prenotazioni(self):
            self.tableWidget.clearContents()

            self.comboBox_campi.setCurrentIndex(0)
            self.timeEdit_inizio.setTime(QtCore.QTime(0, 0))
            self.timeEdit_fine.setTime(QtCore.QTime(23, 0))
            if self.admin:
                    self.lineEdit_g1s1.clear()
            else:
                    self.lineEdit_g1s1.setText(self.utente.nome + " " + self.utente.cognome)
            self.lineEdit_g2s1.clear()
            self.lineEdit_g1s2.clear()
            self.lineEdit_g2s2.clear()
            self.pushButton_modifica.setEnabled(False)
            self.pushButton_elimina.setEnabled(False)

            data_selezionata = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            prenotazioni = self.controller.get_prenotazioni_per_data(data_selezionata)

            ora_minima = int(self.tableWidget.verticalHeaderItem(0).text().split(":")[0])

            for prenotazione in prenotazioni:
                    campo_index = self.comboBox_campi.findText(prenotazione.campo)
                    ora_inizio_index = int(prenotazione.orario_inizio.split(":")[0]) - ora_minima
                    ora_fine_index = int(prenotazione.orario_fine.split(":")[0]) - ora_minima

                    for riga in range(ora_inizio_index, ora_fine_index + 1):
                            item = QtWidgets.QTableWidgetItem(f"{prenotazione.squadra1[0]}, {prenotazione.squadra1[1]} / {prenotazione.squadra2[0]}, {prenotazione.squadra2[1]}")
                            self.tableWidget.setItem(riga, campo_index, item)

    def prenota_campo(self):
            data = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            campo = self.comboBox_campi.currentText()
            orario_inizio = self.timeEdit_inizio.time()
            orario_fine = self.timeEdit_fine.time()
            squadra1 = [self.lineEdit_g1s1.text(), self.lineEdit_g2s1.text()]
            squadra2 = [self.lineEdit_g1s2.text(), self.lineEdit_g2s2.text()]

            if orario_inizio >= orario_fine:
                    QtWidgets.QMessageBox.warning(None, "Errore","L'orario di inizio deve essere precedente a quello di fine.")
                    return

            orario_inizio_str = orario_inizio.toString("HH:00")
            orario_fine_str = orario_fine.toString("HH:00")

            if self.controller.create_prenotazione(data, orario_inizio_str, orario_fine_str, campo, squadra1, squadra2, self.utente.username):
                    self.carica_lista_prenotazioni()
                    QtWidgets.QMessageBox.information(None, "Successo", "Prenotazione effettuata!")
            else:
                    QtWidgets.QMessageBox.warning(None, "Errore", "Orario già occupato!")

    def seleziona_prenotazione(self, row, col):
            item = self.tableWidget.item(row, col)
            if not item or item.text().strip() == "":
                    self.comboBox_campi.setCurrentIndex(0)
                    self.timeEdit_inizio.setTime(QtCore.QTime(0, 0))
                    self.timeEdit_fine.setTime(QtCore.QTime(23, 0))
                    if self.admin:
                        self.lineEdit_g1s1.clear()
                    else:
                        self.lineEdit_g1s1.setText(self.utente.nome + " " + self.utente.cognome)
                    self.lineEdit_g2s1.clear()
                    self.lineEdit_g1s2.clear()
                    self.lineEdit_g2s2.clear()
                    self.pushButton_modifica.setEnabled(False)
                    self.pushButton_elimina.setEnabled(False)
                    return

            data_selezionata = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            prenotazioni = self.controller.get_prenotazioni_per_data(data_selezionata)

            ora_minima = int(self.tableWidget.verticalHeaderItem(0).text().split(":")[0])
            ora_selezionata = QtCore.QTime(row + ora_minima, 0)

            for prenotazione in prenotazioni:
                    orario_inizio_prenotazione = QtCore.QTime.fromString(prenotazione.orario_inizio, "HH:mm")
                    orario_fine_prenotazione = QtCore.QTime.fromString(prenotazione.orario_fine, "HH:mm")
                    colonna_prenotazione = self.comboBox_campi.findText(prenotazione.campo)

                    if orario_inizio_prenotazione <= ora_selezionata <= orario_fine_prenotazione and colonna_prenotazione == col:

                            self.comboBox_campi.setCurrentText(prenotazione.campo)
                            self.timeEdit_inizio.setTime(QtCore.QTime.fromString(prenotazione.orario_inizio, "HH:mm"))
                            self.timeEdit_fine.setTime(QtCore.QTime.fromString(prenotazione.orario_fine, "HH:mm"))

                            self.lineEdit_g1s1.setText(prenotazione.squadra1[0])
                            self.lineEdit_g2s1.setText(prenotazione.squadra1[1])
                            self.lineEdit_g1s2.setText(prenotazione.squadra2[0])
                            self.lineEdit_g2s2.setText(prenotazione.squadra2[1])

                            if not self.admin:
                                if self.utente.username == prenotazione.username:
                                        self.pushButton_modifica.setEnabled(True)
                                        self.pushButton_elimina.setEnabled(True)
                            else:
                                self.pushButton_modifica.setEnabled(True)
                                self.pushButton_elimina.setEnabled(True)

                            self.prenotazione_corrente = prenotazione
                            return

    def modifica_prenotazione(self):

            nuovo_campo = self.comboBox_campi.currentText()
            nuovo_orario_inizio = self.timeEdit_inizio.time().toString("HH:00")
            nuovo_orario_fine = self.timeEdit_fine.time().toString("HH:00")
            nuova_squadra1 = [self.lineEdit_g1s1.text(), self.lineEdit_g2s1.text()]
            nuova_squadra2 = [self.lineEdit_g1s2.text(), self.lineEdit_g2s2.text()]

            if nuovo_orario_inizio >= nuovo_orario_fine:
                    QtWidgets.QMessageBox.warning(None, "Errore","L'orario di inizio deve essere precedente a quello di fine.")
                    return

            if not self.admin:
                    if self.prenotazione_corrente.username != self.utente.username:
                        QtWidgets.QMessageBox.warning(None, "Errore", "Non puoi modificare questa prenotazione!")
                        return

            if self.controller.update_prenotazione(self.prenotazione_corrente, nuovo_campo, nuovo_orario_inizio, nuovo_orario_fine, nuova_squadra1, nuova_squadra2):

                    QtWidgets.QMessageBox.information(None, "Successo", "Prenotazione modificata!")
                    self.carica_lista_prenotazioni()
                    self.prenotazione_corrente = None
            else:
                    QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante la modifica della prenotazione.")

    def elimina_prenotazione(self):

            risposta = QtWidgets.QMessageBox.question(
                    None, "Conferma Eliminazione",
                    "Sei sicuro di voler eliminare questa prenotazione?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if risposta == QtWidgets.QMessageBox.No:
                    return

            if not self.admin:
                if self.prenotazione_corrente.username != self.utente.username:
                    QtWidgets.QMessageBox.warning(None, "Errore", "Non puoi eliminare questa prenotazione!")
                    return

            if self.controller.delete_prenotazione(self.prenotazione_corrente):
                    QtWidgets.QMessageBox.information(None, "Successo", "Prenotazione eliminata con successo.")
                    self.prenotazione_corrente = None
                    self.carica_lista_prenotazioni()
            else:
                    QtWidgets.QMessageBox.warning(None, "Errore", "Errore durante l'eliminazione della prenotazione.")
