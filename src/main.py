import sys

from PyQt5.QtWidgets import QApplication
from Manager import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())