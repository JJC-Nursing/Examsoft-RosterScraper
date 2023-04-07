#!/usr/bin/env python3

# future updates: a date / time appender to file export (easy way to timestamp)


import sys
import rosterscraper_backend as esv
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QInputDialog, QLabel, QVBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        fonts_name = [QFontDatabase.addApplicationFont("fonts/BeVietnam-ExtraBold.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-Regular.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-SemiBold.ttf")]
        for x in fonts_name:
            if x < 0:
                print("Error")

        # families = QFontDatabase.applicationFontFamilies(id)
        # print(families[0])

        # label = QLabel("Hello World!!!", self)
        # label.setFont(QFont("Be Vietnam ExtraBold", 20))
        # label.move(50, 50)

        self.setWindowTitle("My App")
        btn_import = QPushButton("import location")
        # btn_import.setCheckable(True)
        btn_import.setFont(QFont("Be Vietnam", 10))
        btn_import.released.connect(self.import_location)

        lbl_title = QLabel("Examsoft GUI Test", self)
        lbl_title.setFont(QFont("Be Vietnam ExtraBold", 20))
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_stuff = QLabel("Lorem ipsum decorum.", self)
        lbl_stuff.setFont(QFont("Be Vietnam", 10))
        # lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_words = QVBoxLayout()
        layout_words.addWidget(lbl_title)
        layout_words.addWidget(lbl_stuff)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        layout_main.addWidget(btn_import)

        container = QWidget()
        container.setLayout(layout_main)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

        self.setMinimumSize(QSize(400, 115))

        # Set the central widget of the Window.
        # self.setCentralWidget(btn_import)

    def import_location(self):
        home_dir = str(Path.home())
        f_name = QFileDialog.getOpenFileName(self, 'Open file:', home_dir)

        if f_name[0]:
            f = open(f_name[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.
