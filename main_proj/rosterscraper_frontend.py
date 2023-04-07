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
    QHBoxLayout, QGridLayout, QWidget, QStackedWidget, QStackedLayout
from PyQt6.QtGui import QFont, QFontDatabase, QColor, QCursor

# Only needed for access to command line arguments
import sys



# Subclass QWidget to customize your application's frames
class prev_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        label = QLabel("Welcome to Widget 1!")

        layout.addWidget(label)
        button = QPushButton("Switch to Widget 2")

        button.clicked.connect(self.switch_widget)

        layout.addWidget(button)
        self.setLayout(layout)

    def switch_widget(self):
        # for stacked widgets, the first one needs to be max_widgets - 1 to move to the next one
        # (it decrements backwards)
        stacked_widget.setCurrentIndex(1)

class test_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        label = QLabel("Welcome to Widget 2!")

        layout.addWidget(label)
        button = QPushButton("Switch to Widget 3")

        button.clicked.connect(self.switch_widget)

        layout.addWidget(button)
        self.setLayout(layout)

    def switch_widget(self):
        stacked_widget.setCurrentIndex(0)


class init_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        lbl_title = QLabel("Examsoft RosterScraper", self)
        lbl_title.setFont(QFont("Be Vietnam ExtraBold", 20))
        # lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam SemiBold", 20))
        lbl_version.setStyleSheet("color: #AAA;")

        lbl_stuff = QLabel(txt_stuff, self)
        lbl_stuff.setFont(QFont("Be Vietnam", 10))
        # lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)
        layout_words.addWidget(lbl_stuff)
        #  layout_words.setStyleSheet()
        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        layout_main.addWidget(btn_import)

        # layout_main.setStyle

        container = QWidget()
        container.setStyleSheet(".QWidget "
                                "{background: "
                                "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                "* {color: #FFFFFF};")
        container.setLayout(layout_main)
        layout_fin = QStackedLayout()
        layout_fin.addWidget(container)

        # self.setStyleSheet("{background: "
        #                         "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
        #                         "* {color: #FFFFFF};")
        self.setLayout(layout_fin)


        # Set the central widget of the Window.
        # self.setCentralWidget(container)

        self.setMinimumSize(QSize(400, 250))

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

    def switch_widget(self):
        stacked_widget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget and add the two widgets to it
    stacked_widget = QStackedWidget()
    widget1 = init_Widget()
    widget1_1 = test_Widget()
    widget2 = prev_Widget()
    stacked_widget.addWidget(widget1)
    stacked_widget.addWidget(widget1_1)
    stacked_widget.addWidget(widget2)

    # Show the first widget (setCurrentIndex = MAX amt. of widgets, last widget is 0)
    stacked_widget.setCurrentIndex(2)
    stacked_widget.show()

    # setCentralWidget(stacked_widget)

    sys.exit(app.exec())
