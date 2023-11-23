import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QHBoxLayout, QMainWindow, QDialog


class ChangeCow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        labels = {"info": ["id",
                           "name",
                           "age",
                           "color",
                           "height",
                           "weight"],
                  "vitamins": ["A",
                               "B1",
                               "B2",
                               "B3",
                               "B5",
                               "B6",
                               "B12",
                               "C",
                               "D",
                               "E"],
                  "minerals": ["Ca",
                               "Fe",
                               "Mg",
                               "K",
                               "Na",
                               "P",
                               "Zn",
                               "Cu",
                               "Se",
                               "I"]
                  }

        mainlayout = QHBoxLayout()
        self.lineedits = {}
        vbox = QVBoxLayout()
        label = QLabel("info")
        label.setFixedSize(150, 20)
        vbox.addWidget(label)
        save_button = QPushButton("Save cow")
        save_button.setFixedSize(200, 100)
        for i in labels["info"]:
            hbox = QHBoxLayout()
            label = QLabel(i)
            label.setFixedSize(40, 20)
            label.setAlignment(Qt.AlignLeft)
            lineedit = QLineEdit()
            lineedit.setAlignment(Qt.AlignRight)
            lineedit.setFixedSize(150, 20)
            self.lineedits[i] = lineedit
            hbox.addWidget(label)
            hbox.addWidget(lineedit)
            vbox.addLayout(hbox)
        vbox.addWidget(save_button)

        mainlayout.addLayout(vbox)
        for i in ["vitamins", "minerals"]:
            vbox = QVBoxLayout()
            label = QLabel(i)
            label.setFixedSize(150, 20)
            vbox.addWidget(label)
            for j in labels[i]:
                hbox = QHBoxLayout()
                label = QLabel(j)
                label.setFixedSize(30, 20)
                lineedit = QLineEdit()
                lineedit.setFixedSize(150, 20)
                self.lineedits[j] = lineedit
                hbox.addWidget(label)
                hbox.addWidget(lineedit)
                vbox.addLayout(hbox)
            mainlayout.addLayout(vbox)
        central_widget.setLayout(mainlayout)

    def save_cow(self):
        pass


class CowDatabaseUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        buttons = ["database lenth",
                   "add cow to database",
                   "delete cow with",
                   "change cow",
                   "import"]

        mainlayout = QVBoxLayout()
        for i in buttons:
            hbox = QHBoxLayout()
            button = QPushButton(i)
            button.setFixedSize(150, 30)
            lineedit = QLineEdit()
            lineedit.setFixedSize(150, 30)
            hbox.addWidget(button)
            button.clicked.connect(self.change_cow)
            hbox.addWidget(lineedit)
            mainlayout.addLayout(hbox)

        central_widget.setLayout(mainlayout)

    def change_cow(self):
        dialog = QDialog()
        labels = {"info": ["id",
                           "name",
                           "age",
                           "color",
                           "height",
                           "weight"],
                  "vitamins": ["A",
                               "B1",
                               "B2",
                               "B3",
                               "B5",
                               "B6",
                               "B12",
                               "C",
                               "D",
                               "E"],
                  "minerals": ["Ca",
                               "Fe",
                               "Mg",
                               "K",
                               "Na",
                               "P",
                               "Zn",
                               "Cu",
                               "Se",
                               "I"]
                  }

        mainlayout = QHBoxLayout()
        self.lineedits = {}
        vbox = QVBoxLayout()
        label = QLabel("info")
        label.setFixedSize(150, 20)
        vbox.addWidget(label)
        save_button = QPushButton("Save cow")
        save_button.clicked.connect(dialog.accept)
        save_button.setFixedSize(200, 100)
        for i in labels["info"]:
            hbox = QHBoxLayout()
            label = QLabel(i)
            label.setFixedSize(40, 20)
            label.setAlignment(Qt.AlignLeft)
            lineedit = QLineEdit()
            lineedit.setAlignment(Qt.AlignRight)
            lineedit.setFixedSize(150, 20)
            self.lineedits[i] = lineedit
            hbox.addWidget(label)
            hbox.addWidget(lineedit)
            vbox.addLayout(hbox)
        vbox.addWidget(save_button)

        mainlayout.addLayout(vbox)
        for i in ["vitamins", "minerals"]:
            vbox = QVBoxLayout()
            label = QLabel(i)
            label.setFixedSize(150, 20)
            vbox.addWidget(label)
            for j in labels[i]:
                hbox = QHBoxLayout()
                label = QLabel(j)
                label.setFixedSize(30, 20)
                lineedit = QLineEdit()
                lineedit.setFixedSize(150, 20)
                self.lineedits[j] = lineedit
                hbox.addWidget(label)
                hbox.addWidget(lineedit)
                vbox.addLayout(hbox)
            mainlayout.addLayout(vbox)
        dialog.setLayout(mainlayout)
        dialog.exec()
        print('button clicked')

if __name__ == '__main__':
    app = QApplication([])
    window = CowDatabaseUI()
    window.show()
    sys.exit(app.exec())
