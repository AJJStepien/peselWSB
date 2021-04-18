import datetime
import sys
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QDateEdit
from PyQt5.QtCore import pyqtSlot, QDate
sys.path.append("appLogic.py")
from appLogic import PeselGen


class Pesel(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Generator PESEL'
        self.left = 500
        self.top = 300
        self.width = 500
        self.height = 100

        self.giveMeDateLbl = QLabel('Podaj datę urodzenia: ')
        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(datetime.date.today())
        minDate = QDate(1800,1,1)
        maxDate = QDate(2299,12,31)
        self.dateEdit.setDateRange(minDate, maxDate)

        self.sexChoice = QComboBox()
        self.sexChoice.addItem("Dowolna płeć", 0)
        self.sexChoice.addItem("Kobieta", 2)
        self.sexChoice.addItem("Mężczyzna", 1)


        self.generateBtn = QPushButton('Generuj PESEL')
        self.yourNewPeseLbl = QLabel("Twój nowy PESEL: ")
        self.newPeselLbl = QLabel("Nowy PESEL")
        self.copyPeselBtn = QPushButton("Kopiuj PESEL")
        self.infoBtn = QPushButton('Info')
        self.infoBtn.setToolTip("Informacje o autorze")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

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
        layout.setRowStretch(1,2)
        layout.setRowStretch(2,4)

        self.generateBtn.clicked.connect(self.onGenerateBtnClick)
#        self.infoBtn.clicked.connect(self.onInfoBtnClick)

        layout.addWidget(self.giveMeDateLbl, 0, 0,1,2)
        layout.addWidget(self.dateEdit, 0, 2)
        layout.addWidget(self.sexChoice, 0, 3)
        layout.addWidget(self.yourNewPeseLbl, 1, 0,1,2)
        layout.addWidget(self.newPeselLbl, 1, 2,1,2)
        layout.addWidget(self.copyPeselBtn,1,3)
        layout.addWidget(self.generateBtn, 2,0,1,3)
        layout.addWidget(self.infoBtn, 2,3)

        self.horizontalGroupBox.setLayout(layout)


    @pyqtSlot()
    def onGenerateBtnClick(self):
        date = self.dateEdit.date()
        # dateStr = date.toString("yy-MM-dd")
        generator = PeselGen.generate(self,
                                      date.toString("yyyy"),
                                      date.toString("MM"),
                                      date.toString("dd"),
                                      self.sexChoice.currentData())
        # self.newPeselLbl.setText(date.toString("yyMMdd"))
        self.newPeselLbl.setText(date.toString(generator))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pesel()
    sys.exit(app.exec_())