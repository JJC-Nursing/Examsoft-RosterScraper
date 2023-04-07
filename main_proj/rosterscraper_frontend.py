# future updates: a date / time appender to file export (easy way to timestamp)
#                 a remembrance of where the program last saved and what its name was last (check for overwriting)

txt_version = "v1.1"

txt_updatedate = "03.30.2023"

txt_stuff = "script orig. written by Jefferson Cherrington" + "\n\n" + \
            "creates a CSV roster from a particularly formatted HTML file" + "\n" + \
            "(all scraping is done offline)" + "\n\n" + \
            "last updated: " + txt_updatedate + "\n"

import sys
import rosterscraper_backend as esv
from pathlib import Path

from PyQt6.QtCore import QSize, Qt, QAbstractAnimation, QVariantAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QInputDialog, QLabel, QVBoxLayout, \
    QGridLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase, QColor, QCursor

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

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

        self.setWindowTitle("RosterScraper Start Screen")
        btn_import = QPushButton("import location")
        # btn_import.setCheckable(True)
        btn_import.setFont(QFont("Be Vietnam", 12))
        btn_import.released.connect(self.import_location)
        btn_import.setStyleSheet(".QPushButton{"
                                 "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                 "stop:0 rgba(0, 0, 0, 20), stop:1 rgba(255, 255, 255, 60));"
                                 "border: 2px solid white; border-radius: 8.5px;"
                                 "padding: 5px;"
                                 "}"
                                 ".QPushButton:hover{"
                                 "background: rgba(0, 165, 180, 70);"

                                 "}"
                                 )

        lbl_title = QLabel("Examsoft GUI Test", self)
        lbl_title.setFont(QFont("Be Vietnam ExtraBold", 20))
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_stuff = QLabel(txt_stuff, self)
        lbl_stuff.setFont(QFont("Be Vietnam", 10))
        # lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_words = QVBoxLayout()
        layout_words.addWidget(lbl_title)
        layout_words.addWidget(lbl_stuff)
        #  layout_words.setStyleSheet()

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        layout_main.addWidget(btn_import)

        container = QWidget()
        container.setStyleSheet(".QWidget "
                                "{background: "
                                "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                "* {color: #FFFFFF};")
        container.setLayout(layout_main)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

        self.setMinimumSize(QSize(400, 110))

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
