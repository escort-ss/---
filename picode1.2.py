
import sys
from PySide2.QtWidgets import QApplication
from picodeFileSelect import Window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    sys.exit(app.exec_())
input()
