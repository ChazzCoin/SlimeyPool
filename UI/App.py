from PyQt6 import QtWidgets
from UI.SlimeyPool import SlimeyPool

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeyPool()
    sys.exit(app.exec())