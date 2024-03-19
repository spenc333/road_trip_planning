from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#from main import *


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Road Trip Planner")
        self.mainWindow = QMdiArea()
        self.setCentralWidget(self.mainWindow)
        self.mainWindow.tileSubWindows()

        """
        Creating the menu bar
        """
        # toolbar = QToolBar("Main toolbar")
        # toolbar.setIconSize(QSize(16, 16))
        # self.addToolBar(toolbar)

        save = QAction("&Save", self)
        save.setStatusTip("Save your current trip")
        save.triggered.connect(self.buttonClick)
        save.setCheckable(True)
        save.setShortcut(QKeySequence("Ctrl+s"))
        save.hover()
        # toolbar.addAction(save)

        # toolbar.addSeparator()

        saveAs = QAction("&Save As", self)
        saveAs.setStatusTip("Save your new trip")
        saveAs.triggered.connect(self.buttonClick)
        saveAs.setCheckable(True)
        saveAs.setShortcut(QKeySequence("Ctrl+w"))
        saveAs.hover()
        # toolbar.addAction(saveAs)

        # toolbar.addSeparator()

        new = QAction("&New", self)
        new.setStatusTip("Open a new project window")
        new.triggered.connect(self.buttonClick)
        new.setCheckable(True)
        new.setShortcut(QKeySequence("Ctrl+n"))
        new.hover()
        # toolbar.addAction(new)

        # toolbar.addSeparator()

        open = QAction("&Open", self)
        open.setStatusTip("Open an existing trip")
        open.triggered.connect(self.buttonClick)
        open.setCheckable(True)
        open.setShortcut(QKeySequence("Ctrl+o"))
        open.hover()
        # toolbar.addAction(open)

        # toolbar.addSeparator()

        export = QAction("&Export", self)
        export.setStatusTip("Export as PDF (or spreadsheet)")
        export.triggered.connect(self.buttonClick)
        export.setCheckable(True)
        export.setShortcut(QKeySequence("Ctrl+e"))
        export.hover()
        # toolbar.addAction(export)

        # toolbar.addWidget(QLabel("Road Trip"))
        # toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(save)
        file_menu.addSeparator()
        file_menu.addAction(saveAs)
        file_menu.addSeparator()
        file_menu.addAction(new)
        file_menu.addSeparator()
        file_menu.addAction(open)
        file_menu.addSeparator()
        file_menu.addAction(export)

        """
        Setting the desired destinations window
        """

        sub1 = QMdiSubWindow()
        sub1.setWindowTitle("Desired Destination(s)")
        widget1 = QWidget()
        layout1 = QVBoxLayout(widget1)
        destination = QLineEdit()
        destinationList = QListWidget()
        layout1.addWidget(destination)
        layout1.addWidget(destinationList)
        widget1.setLayout(layout1)
        sub1.setWidget(widget1)
        self.mainWindow.addSubWindow(sub1)

        """"
        Setting the directions window
        """
        sub2 = QMdiSubWindow()
        sub2.setWindowTitle("Directions")
        widget2 = QListWidget()

        sub2.setWidget(widget2)
        self.mainWindow.addSubWindow(sub2)

        """
        Setting the map window
        """
        sub = QMdiSubWindow()
        sub.setWindowTitle("Map View")
        widget = QWidget()
        layout = QHBoxLayout(widget)
        self.walkingMode = QRadioButton("Walking")

        self.drivingMode = QRadioButton("Driving")
        self.drivingMode.setChecked(True)
        layout.addWidget(self.drivingMode)
        layout.addWidget(self.walkingMode)
        widget.setLayout(layout)
        sub.setWidget(widget)
        self.mainWindow.addSubWindow(sub)

        self.mainWindow.addSubWindow(sub)

    def buttonClick(self, c):
        print("click", c)

    def openFunc(self):
        # opens an existing session
        pass

    def addNew(self, c):
        # adds new session
        pass

    def save(self, name="session"):
        # need to figure out how to save session (maybe .ses) extension and what gets saved
        pass

    def export(self, name="directions"):
        # export list of shortest directions maybe using google api
        pass

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

    def addItem(self):
        """
        adds item to desired destination list
        """
        pass

    def clear(self):
        """
        clears desired destination box
        """
        pass

        # setting geometry to the window
        # self.setGeometry(100,100,300,400)

        # Creating window for choosing desinations, etc...

        # self.setTravelWindow = QMdiArea()
        # self.setCentralWidget(self.setTravelWindow)
        # self.setTravelWindow.setTabsClosable(False)
        # # setting window title
        # self.setWindowTitle("Road Trip Planner")

        # self.setTravelWindow.tileSubWindows()

        # # Setting the first window: Map view

        # sub2 = QMdiSubWindow()
        # sub2.setWidget(QTextEdit())
        # sub2.setWindowTitle("Current Destinations")
        # self.setTravelWindow.addSubWindow(sub2)

        # sub = QMdiSubWindow()
        # sub.setWidget(QTextEdit())
        # sub.setWindowTitle("Destination")
        # self.setTravelWindow.addSubWindow(sub)

        # sub1 = QMdiSubWindow()
        # sub1.addWidget(QComboBox())

        # sub1.setWindowTitle("Map View")
        # self.setTravelWindow.addSubWindow(sub1)

        # # creating a group box
        # self.formGroupBox = QGroupBox("Travel")
        # # creating combo box to select travel mode
        # self.travelMode = QComboBox()
        # # adding items to the combo box
        # self.travelMode.addItems(["walking", "driving",
        #                           "bicycling", "transit"])
        # # creating a line edit
        # self.destinationLineEdit = QLineEdit()
        # # calling the method that create the form
        # self.createForm()

        # # creating a dialog button for ok and cancel
        # self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
        #                                   | QDialogButtonBox.StandardButton.Cancel)
        # # adding action when form is accepted
        # self.buttonBox.accepted.connect(self.getInfo)
        # # adding action when form is rejected
        # # self.buttonBox.rejected.connect(self.reject)

        # # creating a vertical layout
        # mainLayout = QVBoxLayout()

        # # adding form group box to the layout
        # mainLayout.addWidget(self.formGroupBox)

        # # adding button box to the layout
        # mainLayout.addWidget(self.buttonBox)

        # # setting lay out
        # # self.setLayout(mainLayout)

    # defining actions

    # get info method called when form is accepted

    def getInfo(self):
        # printing the form information
        print(f"Desination : {self.destinationLineEdit.text()}")
        print(f"Travel Mode : {self.travelMode.currentText()}")

        # self.close()
        pass

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
        pass


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        pass


def main():
    # create pyqt app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = mainWindow()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())


# main method
if __name__ == '__main__':
    main()
