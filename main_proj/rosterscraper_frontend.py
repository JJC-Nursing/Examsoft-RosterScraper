# future updates: a date / time appender to file export (easy way to timestamp)
#                 a remembrance of where the program last saved and what its name was last (check for overwriting)

txt_placeholder = "Lorem ipsum dolor sit amet, " \
                  "consectetur adipiscing elit. " \
                  "Quisque imperdiet, risus vel cursus cursus, " \
                  "nibh orci ultricies ex, sed imperdiet risus erat ac turpis. " \
                  "Pellentesque habitant morbi tristique senectus et netus et malesuada " \
                  "fames ac turpis egestas. Aliquam a nunc urna. Integer interdum eu ipsum in " \
                  "viverra. Suspendisse rhoncus porttitor nisl, sit amet ornare metus molestie a. " \
                  "Donec dapibus leo vel diam vestibulum pellentesque. Orci varius natoque penatibus " \
                  "et magnis dis parturient montes, nascetur ridiculus mus. Nunc nisi mauris, egestas " \
                  "quis iaculis sed, dapibus vitae velit. Maecenas interdum lacus dolor, eu mattis " \
                  "ex feugiat non. Aliquam ac diam eu felis cursus venenatis. Sed suscipit enim ligula, " \
                  "at luctus nisi hendrerit non. Proin at malesuada enim. Orci varius natoque penatibus " \
                  "et magnis dis parturient montes, nascetur ridiculus mus. Orci varius natoque penatibus " \
                  "et magnis dis parturient montes, nascetur ridiculus mus. Praesent vulputate condimentum " \
                  "purus, vitae accumsan enim pulvinar in. Morbi blandit non elit at cursus. Fusce ullamcorper " \
                  "vulputate nunc. Phasellus et sem at ante pellentesque congue id ultrices ipsum.\n\n Nam non " \
                  "eleifend velit, ac venenatis dolor. Fusce ullamcorper sem eget libero euismod efficitur " \
                  "non vitae quam. Praesent vehicula consectetur efficitur. Nullam at elit sem. Nullam " \
                  "interdum accumsan lorem, a sagittis tellus semper a. Interdum et malesuada fames ac " \
                  "ante ipsum primis in faucibus. Ut mattis nec elit nec dignissim. Pellentesque nec " \
                  "volutpat lectus, eu mollis eros. Nulla auctor auctor ultrices. Nullam malesuada, " \
                  "enim sed tempus tristique, nulla dui ornare tortor, vitae sollicitudin dui sapien sit " \
                  "amet arcu. Pellentesque sed ullamcorper odio, in porttitor enim. Sed dui sem, gravida " \
                  "quis lobortis nec, aliquet in purus. Nam vitae odio quis erat interdum egestas ac " \
                  "consectetur libero. Vivamus nec varius augue. Aliquam erat volutpat. Aliquam tortor " \
                  "augue, molestie et aliquam quis, viverra a eros.\n\n Vestibulum molestie convallis iaculis. " \
                  "Quisque ut leo id elit fermentum semper. Duis lacinia ante ipsum, quis efficitur ex " \
                  "feugiat non. Morbi scelerisque quam ante, id malesuada elit iaculis eu. Etiam rutrum " \
                  "nisl justo, vel sollicitudin mauris imperdiet sed. Integer lacinia erat in varius elementum. " \
                  "Suspendisse a tempor magna. Sed vel ipsum ullamcorper, suscipit diam a, cursus est. Aenean " \
                  "convallis mi id quam aliquam, nec lobortis enim pretium. Fusce venenatis tempus lectus, " \
                  "non condimentum odio posuere eget. Donec luctus justo sit amet facilisis consectetur. " \
                  "Proin sagittis, neque vitae ultrices dictum, neque enim ultricies nisi, ac bibendum velit " \
                  "dui eget orci. Suspendisse in mi et est gravida egestas ut nec felis. Donec eleifend " \
                  "nulla magna, a laoreet dui placerat faucibus. Praesent purus orci, vulputate vitae mollis " \
                  "sit amet, tempus sit amet odio. In at lorem elit. Sed nec magna nec nunc sagittis lacinia. " \
                  "Nam justo turpis, pharetra ac felis nec, luctus elementum nibh. Vivamus a ultricies velit."

txt_version = "v2.1"

txt_updatedate = "03.30.2023"

txt_stuff = "script orig. written by Jefferson Cherrington" + "\n\n" + \
            "creates a CSV roster from a particularly formatted HTML file" + "\n" + \
            "(all scraping is done offline)" + "\n\n" + \
            "last updated: " + txt_updatedate + "\n"

arr_titles = ["Start Screen", "Import File", "Export Folder", "Export Filename", "Preview Output"]

import sys
import rosterscraper_backend as esv
from pathlib import Path

from PyQt6.QtCore import QSize, Qt, QAbstractAnimation, QVariantAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QInputDialog, QLabel, QVBoxLayout, \
    QHBoxLayout, QGridLayout, QWidget, QStackedWidget, QStackedLayout, QProgressBar, QLineEdit, QTextEdit
from PyQt6.QtGui import QFont, QFontDatabase, QColor, QCursor, QIcon

# Only needed for access to command line arguments
import sys

obj = esv.OfflineRS()


# Subclass QWidget to customize your application's frames
class startscreen_Widget(QWidget):
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

        btn_continue = QPushButton("continue ->")
        btn_continue.clicked.connect(self.switch_widget)
        btn_continue.setFont(QFont("Be Vietnam", 14))
        btn_continue.setStyleSheet(".QPushButton{"
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
        lbl_title.setFont(QFont("Be Vietnam ExtraBold", 40))
        lbl_title.setStyleSheet("padding-left: 1px; padding-right: 0px;")
        # lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam", 40))
        lbl_version.setStyleSheet("color: #AAA;")
        # lbl_version.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lbl_stuff = QLabel(txt_stuff, self)
        lbl_stuff.setFont(QFont("Be Vietnam", 12))
        lbl_stuff.setStyleSheet("padding: 13px;")
        # lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)
        layout_title.setSpacing(0)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)
        layout_words.addWidget(lbl_stuff)
        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)

        layout_main.addWidget(btn_continue)

        widget_bkg = QWidget()
        widget_bkg.setStyleSheet(".QWidget "
                                 "{background: "
                                 "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                 "* {color: #FFFFFF;}"
                                 )
        widget_bkg.setLayout(layout_main)

        layout_fin = QStackedLayout()
        layout_fin.addWidget(widget_bkg)

        # self.setStyleSheet("{background: "
        #                         "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
        #                         "* {color: #FFFFFF};")
        self.setLayout(layout_fin)

        # Set the central widget of the Window.
        # self.setCentralWidget(widget_bkg)

        self.setMinimumSize(QSize(400, 250))

        # Set the central widget of the Window.
        # self.setCentralWidget(btn_import)

    def switch_widget(self):
        # for stacked widgets, the first one needs to be max_widgets - 1 to move to the next one
        # (it decrements backwards)

        # this needs to be screen 2

        stacked_widget.setCurrentIndex(3)
        stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[1])


class import_loc_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        fonts_name = [QFontDatabase.addApplicationFont("fonts/BeVietnam-ExtraBold.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-Regular.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-SemiBold.ttf")]
        for x in fonts_name:
            if x < 0:
                print("Error")

        btn_continue = QPushButton("continue ->")
        btn_continue.clicked.connect(self.switch_widget)
        btn_continue.setFont(QFont("Be Vietnam", 14))
        btn_continue.setStyleSheet(".QPushButton{"
                                   "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                   "stop:0 rgba(0, 0, 0, 20), stop:1 rgba(255, 255, 255, 60));"
                                   "border: 2px solid white; border-radius: 8.5px;"
                                   "padding: 5px;"
                                   "}"
                                   ".QPushButton:hover{"
                                   "background: rgba(0, 165, 180, 70);"

                                   "}"
                                   )

        btn_import = QPushButton("")
        # btn_import.setCheckable(True)
        btn_import.setIcon(QIcon("assets/search_icon.png"))
        # btn_import.setFont(QFont("Be Vietnam", 50))
        btn_import.setIconSize(QSize(30, 30))
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
        lbl_title.setStyleSheet("padding-left: 1px; padding-right: 0px;")

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam", 20))
        lbl_version.setStyleSheet("color: #AAA;")

        lbl_stuff = QLabel("import location (HTML):", self)
        lbl_stuff.setFont(QFont("Be Vietnam", 20))
        lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.txtbox_location = QLineEdit("text goes here.")
        self.txtbox_location.setFont(QFont("Be Vietnam", 14))
        self.txtbox_location.setStyleSheet(".QLineEdit{"
                                           "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                           "stop:0 rgba(100, 100, 100, 60), stop:1 rgba(255, 255, 255, 90));"
                                           "color: #FFF; border: 2px solid white; border-radius: 8.5px;"
                                           "padding: 5px;"
                                           "}"
                                           ".QLineEdit:hover{"
                                           "background: #B2B3B7; color: #000;}"
                                           ".QLineEdit:focus{"
                                           "background: #B2B3B7; color: #000;}"
                                           )
        self.txtbox_location.setAlignment(Qt.AlignmentFlag.AlignRight)

        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)
        layout_title.setSpacing(0)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)

        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_location = QHBoxLayout()
        layout_location.addWidget(self.txtbox_location)
        layout_location.addWidget(btn_import)
        # layout_location.setContentsMargins(0, 0, 0, 50)

        layout_center = QGridLayout()
        layout_center.addWidget(lbl_stuff, 0, 0)
        layout_center.addLayout(layout_location, 1, 0)
        layout_center.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        layout_main.addLayout(layout_center)
        layout_main.addWidget(btn_continue)

        widget_bkg = QWidget()
        widget_bkg.setStyleSheet(".QWidget "
                                 "{background: "
                                 "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                 "* {color: #FFFFFF;}"
                                 )

        widget_bkg.setWindowTitle("")
        widget_bkg.setWindowTitle("RosterScraper: Import Screen")

        widget_bkg.setLayout(layout_main)
        layout_fin = QStackedLayout()
        layout_fin.addWidget(widget_bkg)

        self.setLayout(layout_fin)
        self.setMinimumSize(QSize(400, 250))

    def import_location(self):
        home_dir = str(Path.home())
        f_name = QFileDialog.getOpenFileName(self, 'Open File:', home_dir, "HTML files (*.html)")

        if f_name[0]:
            # f = open(f_name[0], 'r')
            #
            # with f:
            #     data = f.read()
            #     self.txtbox_location.setText(data)
            self.txtbox_location.setText(f_name[0])

    def switch_widget(self):

        obj.set_inp_name(str(self.txtbox_location.text()))

        # this needs to be screen 3

        stacked_widget.setCurrentIndex(2)
        stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[2])


class exp_tofolder_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        fonts_name = [QFontDatabase.addApplicationFont("fonts/BeVietnam-ExtraBold.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-Regular.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-SemiBold.ttf")]
        for x in fonts_name:
            if x < 0:
                print("Error")

        btn_continue = QPushButton("continue ->")
        btn_continue.clicked.connect(self.switch_widget)
        btn_continue.setFont(QFont("Be Vietnam", 14))
        btn_continue.setStyleSheet(".QPushButton{"
                                   "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                   "stop:0 rgba(0, 0, 0, 20), stop:1 rgba(255, 255, 255, 60));"
                                   "border: 2px solid white; border-radius: 8.5px;"
                                   "padding: 5px;"
                                   "}"
                                   ".QPushButton:hover{"
                                   "background: rgba(0, 165, 180, 70);"

                                   "}"
                                   )

        btn_import = QPushButton("")
        # btn_import.setCheckable(True)
        btn_import.setIcon(QIcon("assets/search_icon.png"))
        # btn_import.setFont(QFont("Be Vietnam", 50))
        btn_import.setIconSize(QSize(30, 30))
        btn_import.released.connect(self.export_location)
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
        lbl_title.setStyleSheet("padding-left: 1px; padding-right: 0px;")
        # lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam", 20))
        lbl_version.setStyleSheet("color: #AAA;")
        # lbl_version.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lbl_stuff = QLabel("export folder (CSV):", self)
        lbl_stuff.setFont(QFont("Be Vietnam", 20))
        # lbl_stuff.setStyleSheet("padding: 5px;")
        lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.txtbox_location = QLineEdit("text goes here.")
        self.txtbox_location.setFont(QFont("Be Vietnam", 14))
        self.txtbox_location.setStyleSheet(".QLineEdit{"
                                           "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                           "stop:0 rgba(100, 100, 100, 60), stop:1 rgba(255, 255, 255, 90));"
                                           "color: #FFF; border: 2px solid white; border-radius: 8.5px;"
                                           "padding: 5px;"
                                           "}"
                                           ".QLineEdit:hover{"
                                           "background: #B2B3B7; color: #000;}"
                                           ".QLineEdit:focus{"
                                           "background: #B2B3B7; color: #000;}"
                                           )
        self.txtbox_location.setAlignment(Qt.AlignmentFlag.AlignRight)
        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)
        layout_title.setSpacing(0)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)

        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_location = QHBoxLayout()
        layout_location.addWidget(self.txtbox_location)
        layout_location.addWidget(btn_import)
        # layout_location.setContentsMargins(0, 0, 0, 50)

        layout_center = QGridLayout()
        layout_center.addWidget(lbl_stuff, 0, 0)
        layout_center.addLayout(layout_location, 1, 0)
        layout_center.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        # layout_main.addWidget(lbl_stuff)
        layout_main.addLayout(layout_center)
        layout_main.addLayout(layout_location)
        layout_main.addWidget(btn_continue)

        widget_bkg = QWidget()
        widget_bkg.setStyleSheet(".QWidget "
                                 "{background: "
                                 "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                 "* {color: #FFFFFF;}"
                                 )

        widget_bkg.setWindowTitle("")
        widget_bkg.setWindowTitle("RosterScraper: Import Screen")

        widget_bkg.setLayout(layout_main)
        layout_fin = QStackedLayout()
        layout_fin.addWidget(widget_bkg)

        # self.setStyleSheet("{background: "
        #                         "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
        #                         "* {color: #FFFFFF};")
        self.setLayout(layout_fin)

        # Set the central widget of the Window.
        # self.setCentralWidget(widget_bkg)

        self.setMinimumSize(QSize(400, 250))

        # Set the central widget of the Window.
        # self.setCentralWidget(btn_import)

    def export_location(self):
        home_dir = str(Path.home())
        f_name = QFileDialog.getExistingDirectory(self, 'Export to folder:', home_dir)

        if f_name:
            # f = open(f_name[0], 'r')
            #
            # with f:
            #     data = f.read()
            #     self.txtbox_location.setText(data)
            self.txtbox_location.setText(f_name)

    def switch_widget(self):

        obj.set_exp_folder(str(self.txtbox_location.text()))

        # this needs to be screen four

        stacked_widget.setCurrentIndex(1)
        stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[3])


class exp_name_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        fonts_name = [QFontDatabase.addApplicationFont("fonts/BeVietnam-ExtraBold.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-Regular.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-SemiBold.ttf")]
        for x in fonts_name:
            if x < 0:
                print("Error")

        btn_continue = QPushButton("continue ->")
        btn_continue.clicked.connect(self.switch_widget)
        btn_continue.setFont(QFont("Be Vietnam", 14))
        btn_continue.setStyleSheet(".QPushButton{"
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
        lbl_title.setStyleSheet("padding-left: 1px; padding-right: 0px;")

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam", 20))
        lbl_version.setStyleSheet("color: #AAA;")

        lbl_stuff = QLabel("name your roster datasets (CSV):", self)
        lbl_stuff.setFont(QFont("Be Vietnam", 20))
        lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.txtbox_location = QLineEdit("text goes here.")
        self.txtbox_location.setFont(QFont("Be Vietnam", 14))
        self.txtbox_location.setStyleSheet(".QLineEdit{"
                                           "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                           "stop:0 rgba(100, 100, 100, 60), stop:1 rgba(255, 255, 255, 90));"
                                           "color: #FFF; border: 2px solid white; border-radius: 8.5px;"
                                           "padding: 5px;"
                                           "}"
                                           ".QLineEdit:hover{"
                                           "background: #B2B3B7; color: #000;}"
                                           ".QLineEdit:focus{"
                                           "background: #B2B3B7; color: #000;}"
                                           )
        self.txtbox_location.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)
        layout_title.setSpacing(0)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)

        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_location = QHBoxLayout()
        layout_location.addWidget(self.txtbox_location)

        layout_center = QGridLayout()
        layout_center.addWidget(lbl_stuff, 0, 0)
        layout_center.addLayout(layout_location, 1, 0)
        layout_center.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        layout_main.addLayout(layout_center)
        layout_main.addLayout(layout_location)
        layout_main.addWidget(btn_continue)

        widget_bkg = QWidget()
        widget_bkg.setStyleSheet(".QWidget "
                                 "{background: "
                                 "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                 "* {color: #FFFFFF;}"
                                 )

        widget_bkg.setLayout(layout_main)
        layout_fin = QStackedLayout()
        layout_fin.addWidget(widget_bkg)

        self.setLayout(layout_fin)
        self.setMinimumSize(QSize(400, 250))

    def export_location(self):
        home_dir = str(Path.home())
        f_name = QFileDialog.getExistingDirectory(self, 'Export to folder:', home_dir)

        if f_name:
            # f = open(f_name[0], 'r')
            #
            # with f:
            #     data = f.read()
            #     self.txtbox_location.setText(data)
            self.txtbox_location.setText(f_name)

    def switch_widget(self):

        obj.set_exp_name(str(self.txtbox_location.text()))
        # this needs to be screen five

        obj.run_scraper()

        stacked_widget.setCurrentIndex(0)
        stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[4])


class preview_results_Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        fonts_name = [QFontDatabase.addApplicationFont("fonts/BeVietnam-ExtraBold.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-Regular.ttf"),
                      QFontDatabase.addApplicationFont("fonts/BeVietnam-SemiBold.ttf")]
        for x in fonts_name:
            if x < 0:
                print("Error")

        # stacked_widget.setWindowTitle("RosterScraper: Import Screen")

        btn_continue = QPushButton("redo program ⟳")
        btn_continue.clicked.connect(self.switch_widget)
        btn_continue.setFont(QFont("Be Vietnam", 14))
        btn_continue.setStyleSheet(".QPushButton{"
                                   "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                   "stop:0 rgba(0, 0, 0, 20), stop:1 rgba(255, 255, 255, 60));"
                                   "border: 2px solid white; border-radius: 8.5px;"
                                   "padding: 5px;"
                                   "}"
                                   ".QPushButton:hover{"
                                   "background: rgba(0, 165, 180, 70);"

                                   "}"
                                   )

        btn_exit = QPushButton("exit program")
        btn_exit.released.connect(self.end_game)
        btn_exit.setFont(QFont("Be Vietnam", 14))
        btn_exit.setStyleSheet(".QPushButton{"
                               "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                               "stop:0 rgba(200, 0, 0, 50), stop:1 rgba(255, 255, 255, 80));"
                               "border: 2px solid white; border-radius: 8.5px;"
                               "padding: 5px;"
                               "}"
                               ".QPushButton:hover{"
                               "background: rgb(171, 7, 27);"

                               "}"
                               )

        lbl_title = QLabel("Examsoft RosterScraper", self)
        lbl_title.setFont(QFont("Be Vietnam ExtraBold", 20))
        lbl_title.setStyleSheet("padding-left: 1px; padding-right: 0px;")
        # lbl_title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        lbl_version = QLabel(txt_version, self)
        lbl_version.setFont(QFont("Be Vietnam", 20))
        lbl_version.setStyleSheet("color: #AAA;")
        # lbl_version.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lbl_stuff = QLabel(str(obj.get_num_stu()) + " students loaded:", self)
        lbl_stuff.setFont(QFont("Be Vietnam", 20))
        # lbl_stuff.setStyleSheet("padding: 5px;")
        lbl_stuff.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.txtbox_location = QTextEdit(obj.get_all_stu())
        self.txtbox_location.setFont(QFont("Be Vietnam", 14))
        self.txtbox_location.setStyleSheet(".QTextEdit{"
                                           "background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, "
                                           "stop:0 rgba(100, 100, 100, 60), stop:1 rgba(255, 255, 255, 90));"
                                           "color: #FFF; border: 2px solid white; border-radius: 8.5px;"
                                           "padding: 5px;"
                                           "}"
                                           ".QTextEdit:hover{"
                                           "background: #B2B3B7; color: #000;}"
                                           ".QTextEdit:focus{"
                                           "background: #B2B3B7; color: #000;}"
                                           )

        # this takes the labels for title and version and puts them in a horz. box layout
        layout_title = QHBoxLayout()
        layout_title.addWidget(lbl_title)
        layout_title.addWidget(lbl_version)
        layout_title.setSpacing(0)

        # this takes the horz. box layout and label for "stuff" and puts them in a vert. box layout
        layout_words = QVBoxLayout()
        layout_words.addLayout(layout_title)

        layout_words.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout_location = QHBoxLayout()
        layout_location.addWidget(self.txtbox_location)

        layout_center = QGridLayout()
        layout_center.addWidget(lbl_stuff, 0, 0)
        layout_center.addLayout(layout_location, 1, 0)
        layout_center.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)

        layout_btns = QHBoxLayout()
        layout_btns.addWidget(btn_continue)
        layout_btns.addWidget(btn_exit)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_words)
        # layout_main.addWidget(lbl_stuff)
        layout_main.addLayout(layout_center)
        layout_main.addLayout(layout_location)
        layout_main.addLayout(layout_btns)

        widget_bkg = QWidget()
        widget_bkg.setStyleSheet(".QWidget "
                                 "{background: "
                                 "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
                                 "* {color: #FFFFFF;}"
                                 )

        widget_bkg.setLayout(layout_main)
        layout_fin = QStackedLayout()
        layout_fin.addWidget(widget_bkg)

        # self.setStyleSheet("{background: "
        #                         "qlineargradient(x1:0 y1:1, x2:0.5 y2:0, stop:0 #23002A, stop:1 #00066A);}"
        #                         "* {color: #FFFFFF};")
        self.setLayout(layout_fin)

        # Set the central widget of the Window.
        # self.setCentralWidget(widget_bkg)

        self.setMinimumSize(QSize(400, 250))

        # Set the central widget of the Window.
        # self.setCentralWidget(btn_import)

    def export_location(self):
        home_dir = str(Path.home())
        f_name = QFileDialog.getExistingDirectory(self, 'Export to folder:', home_dir)

        if f_name:
            # f = open(f_name[0], 'r')
            #
            # with f:
            #     data = f.read()
            #     self.txtbox_location.setText(data)
            self.txtbox_location.setText(f_name)

    def switch_widget(self):

        # this needs to be screen 2

        stacked_widget.setCurrentIndex(3)
        stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[1])

    def end_game(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget and add the two widgets to it
    stacked_widget = QStackedWidget()

    widget0 = preview_results_Widget()
    widget1 = exp_name_Widget()
    widget2 = exp_tofolder_Widget()
    widget3 = import_loc_Widget()
    widget4 = startscreen_Widget()

    stacked_widget.addWidget(widget0)
    stacked_widget.addWidget(widget1)
    stacked_widget.addWidget(widget2)
    stacked_widget.addWidget(widget3)
    stacked_widget.addWidget(widget4)

    # Show the first widget (setCurrentIndex = MAX amt. of widgets, last widget is 0)
    stacked_widget.setCurrentIndex(4)
    stacked_widget.setWindowTitle("RosterScraper: " + arr_titles[0])
    stacked_widget.show()

    # if stacked_widget.currentWidget() == 0:
    #     stacked_widget.setWindowTitle("RosterScraper Start Screen")

    # setCentralWidget(stacked_widget)

    sys.exit(app.exec())
