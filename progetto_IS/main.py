from PyQt5.QtWidgets import QApplication, QWidget
from progetto_IS.views.login import Ui_Form
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())