from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from main import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setTravelWindow = QMdiArea()
        self.setCentralWidget(self.setTravelWindow)
        self.setTravelWindow.setTabsClosable(False)
        bar = self.menuBar()

        # setting geometry to the window
        # self.setGeometry(100,100,300,400)

        # Creating window for choosing desinations, etc...

        file = bar.addMenu("File")
        file.addAction("New")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        export = QAction("Export as PDF (or spreadsheet)", self)
        file.addAction(export)

        # file.triggered[QAction].connect

        # setting window title
        self.setWindowTitle("Road Trip Planner")

        self.setTravelWindow.tileSubWindows()

        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Destination")
        self.setTravelWindow.addSubWindow(sub)

        sub1 = QMdiSubWindow()
        sub1.setWidget(QTextEdit())
        sub1.setWindowTitle("Map View")
        self.setTravelWindow.addSubWindow(sub1)

        sub2 = QMdiSubWindow()
        sub2.setWidget(QTextEdit())
        sub2.setWindowTitle("Current Destinations")
        self.setTravelWindow.addSubWindow(sub2)

        # creating a group box
        self.formGroupBox = QGroupBox("Travel")
        # creating combo box to select travel mode
        self.travelMode = QComboBox()
        # adding items to the combo box
        self.travelMode.addItems(["walking", "driving",
                                  "bicycling", "transit"])
        # creating a line edit
        self.destinationLineEdit = QLineEdit()
        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                                          | QDialogButtonBox.StandardButton.Cancel)
        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)
        # adding action when form is rejected
        # self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

    # get info method called when form is accepted

    def getInfo(self):
        # printing the form information
        print(f"Desination : {self.destinationLineEdit.text()}")
        print(f"Travel Mode : {self.travelMode.currentText()}")

        # self.close()

    def createForm(self):

        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for destination and adding input text
        layout.addRow(QLabel("Desination"), self.destinationLineEdit)

        # for travel mode and adding combo box
        layout.addRow(QLabel("Travel Mode"), self.travelMode)

        # setting layout
        self.formGroupBox.setLayout(layout)


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()


def main():
    # create pyqt app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = MainWindow()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())


# main method
if __name__ == '__main__':
    main()
