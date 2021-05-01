import datetime
import sys
from PyQt5.QtWidgets import *  # QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QDateEdit
from PyQt5.QtCore import *  # pyqtSlot, QDate
from PyQt5.QtGui import QIcon

sys.path.append("appLogic.py")
sys.path.append("static/speedometer.png")
from appLogic import PeselGen


class Pesel(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.frameGeometry().center()
        self.setFixedSize(450, 150)
        self.title = 'Generator PESEL'
        self.icon = QIcon("static/speedometer.png")

        self.giveMeDateLbl = QLabel('Podaj datę urodzenia: ')

        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(datetime.date.today())
        minDate = QDate(1800, 1, 1)
        maxDate = QDate(2299, 12, 31)
        self.dateEdit.setDateRange(minDate, maxDate)

        self.sexChoice = QComboBox()
        self.sexChoice.addItem("Dowolna płeć", 0)
        self.sexChoice.addItem("Kobieta", 2)
        self.sexChoice.addItem("Mężczyzna", 1)

        self.generateBtn = QPushButton('Generuj PESEL')
        self.generateBtn.setStyleSheet("background-color: #dda15e")
        self.generateBtn.setShortcut(' ')

        self.yourNewPeseLbl = QLabel("Twój nowy PESEL: ")

        self.newPeselLbl = QLabel("Nowy PESEL")

        self.copyPeselBtn = QPushButton("Kopiuj PESEL")

        self.infoBtn = QPushButton('Info')

        self.infoBtn.setToolTip("Informacje o autorze")

        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 6)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 4)

        self.generateBtn.clicked.connect(self.onGenerateBtnClick)
        self.infoBtn.clicked.connect(self.onInfoBtnClick)
        self.copyPeselBtn.clicked.connect(self.onCopyPeselBtnClick)

        layout.addWidget(self.giveMeDateLbl, 0, 0, 1, 2)
        layout.addWidget(self.dateEdit, 0, 2)
        layout.addWidget(self.sexChoice, 0, 3)
        layout.addWidget(self.yourNewPeseLbl, 1, 0, 1, 2)
        layout.addWidget(self.newPeselLbl, 1, 2, 1, 2)
        layout.addWidget(self.copyPeselBtn, 1, 3)
        layout.addWidget(self.generateBtn, 2, 0, 1, 3)
        layout.addWidget(self.infoBtn, 2, 3)
        self.generateBtn.setFocus()

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def onGenerateBtnClick(self):
        date = self.dateEdit.date()
        generator = PeselGen.generate(self,
                                      date.toString("yyyy"),
                                      date.toString("MM"),
                                      date.toString("dd"),
                                      self.sexChoice.currentData())
        self.newPeselLbl.setText(date.toString(generator))
        self.pesel = generator

    def onInfoBtnClick(self):
        infoTitle = "Informacje o autorze"
        dialog = QDialog()
        dialog.setFocus()
        dialog.setWindowTitle(infoTitle)
        dialog.setFixedSize(490, 110)
        layout = QGridLayout()

        infoLbl = QLabel("Program stworzony w ramach ćwiczeń z zajęć \"Języki i inżynieria oprogramowania\" \n"
                         "prowadzonych przez mgra Grzegorza Korzeniewskiego \n"
                         "Rok akademicki 2020/2021\n\n"
                         "Autor: Adam Stępień ")

        infoLbl.setAlignment(Qt.AlignCenter)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(infoLbl, 0, 0, 1, 3)
        dialog.setLayout(layout)

        dialog.exec_()

        dialog.show()

    def onCopyPeselBtnClick(self):
        try:
            QApplication.clipboard().setText(self.pesel)
        except:
            QApplication.clipboard().setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pesel()
    sys.exit(app.exec_())
