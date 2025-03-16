from PyQt5.QtWidgets import QApplication, QWidget
from progetto_IS.views.login import Ui_Form

app = QApplication([])
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)
window.show()
app.exec()
