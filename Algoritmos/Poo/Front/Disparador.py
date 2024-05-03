import sys
from Algoritmos.Poo.Front import Front
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Front.MainWindow()
    window.show()
    sys.exit(app.exec_())
