# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cleaner.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: #151515;\n"
"border: 2px solid red\n"
"}\n"
"QPushButton{\n"
"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"background:  #5B88E2;\n"
"color: #151515;\n"
"border-radius: 2px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: #151515;\n"
"}")
        self.NAME = QLabel(self.centralwidget)
        self.NAME.setObjectName(u"NAME")
        self.NAME.setGeometry(QRect(0, 10, 800, 95))
        self.NAME.setStyleSheet(u"font:9pt \"Aldrich\";\n"
" font-size: 45pt;\n"
"color: #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border-top: 2px dotted  #5B88E2;\n"
"border-bottom: 2px dotted  #5B88E2;")
        self.NAME.setAlignment(Qt.AlignCenter)
        self.BY_ME = QLabel(self.centralwidget)
        self.BY_ME.setObjectName(u"BY_ME")
        self.BY_ME.setGeometry(QRect(705, 70, 90, 25))
        self.BY_ME.setStyleSheet(u"font:9pt \"Aldrich\";\n"
" font-size: 10pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;")
        self.BY_ME.setAlignment(Qt.AlignCenter)
        self.MEMORY = QLabel(self.centralwidget)
        self.MEMORY.setObjectName(u"MEMORY")
        self.MEMORY.setGeometry(QRect(40, 120, 200, 50))
        self.MEMORY.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border: 2px solid  #122C4F;\n"
"\n"
"")
        self.MEMORY.setAlignment(Qt.AlignCenter)
        self.FREE = QLabel(self.centralwidget)
        self.FREE.setObjectName(u"FREE")
        self.FREE.setGeometry(QRect(250, 120, 510, 50))
        self.FREE.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color: #151515;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"background: #5B88E2")
        self.FREE.setAlignment(Qt.AlignCenter)
        self.SCAN = QPushButton(self.centralwidget)
        self.SCAN.setObjectName(u"SCAN")
        self.SCAN.setGeometry(QRect(275, 280, 250, 61))
        self.SCAN.setStyleSheet(u"")
        self.BAR = QProgressBar(self.centralwidget)
        self.BAR.setObjectName(u"BAR")
        self.BAR.setGeometry(QRect(299, 210, 461, 40))
        self.BAR.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #122C4F;\n"
"    border-radius: 5px;\n"
"    background-color: #151515;\n"
"    text-align: center;\n"
"    color: #E2E8F0; \n"
"    font-weight: bold;\n"
"    font:9pt \"Aldrich\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #5B88E2; \n"
"    border-radius: 3px;      \n"
"}\n"
"")
        self.BAR.setValue(0)
        self.RESULTS = QLabel(self.centralwidget)
        self.RESULTS.setObjectName(u"RESULTS")
        self.RESULTS.setGeometry(QRect(30, 200, 251, 60))
        self.RESULTS.setStyleSheet(u"#RESULTS{\n"
"font:9pt \"Aldrich\";\n"
"font-size: 14pt;\n"
"color: #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border-radius: 5px;\n"
"margin: 10px;\n"
"border: 2px solid #122C4F\n"
"}")
        self.RESULTS.setAlignment(Qt.AlignCenter)
        self.SEL_MODE = QLabel(self.centralwidget)
        self.SEL_MODE.setObjectName(u"SEL_MODE")
        self.SEL_MODE.setGeometry(QRect(70, 400, 681, 71))
        self.SEL_MODE.setStyleSheet(u"\n"
"font:9pt \"Aldrich\";\n"
"font-size: 14pt;\n"
"color: #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border-radius: 5px;\n"
"margin: 10px;\n"
"border: 2px solid #122C4F")
        self.SEL_MODE.setAlignment(Qt.AlignCenter)
        self.CUSTOM = QPushButton(self.centralwidget)
        self.CUSTOM.setObjectName(u"CUSTOM")
        self.CUSTOM.setGeometry(QRect(530, 480, 191, 50))
        self.CUSTOM.setStyleSheet(u"")
        self.DEEP = QPushButton(self.centralwidget)
        self.DEEP.setObjectName(u"DEEP")
        self.DEEP.setGeometry(QRect(305, 480, 191, 50))
        self.DEEP.setStyleSheet(u"")
        self.FAST = QPushButton(self.centralwidget)
        self.FAST.setObjectName(u"FAST")
        self.FAST.setGeometry(QRect(80, 480, 191, 50))
#if QT_CONFIG(tooltip)
        self.FAST.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.FAST.setStyleSheet(u"")
        self.CLEAR = QPushButton(self.centralwidget)
        self.CLEAR.setObjectName(u"CLEAR")
        self.CLEAR.setGeometry(QRect(550, 290, 201, 41))
        self.CLEAR.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NAME.setText(QCoreApplication.translate("MainWindow", u"Cleaner", None))
        self.BY_ME.setText(QCoreApplication.translate("MainWindow", u"by VEXWA", None))
        self.MEMORY.setText(QCoreApplication.translate("MainWindow", u"Memory:", None))
        self.FREE.setText("")
        self.SCAN.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.RESULTS.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.SEL_MODE.setText(QCoreApplication.translate("MainWindow", u"Selected Clean mode: ", None))
        self.CUSTOM.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.DEEP.setText(QCoreApplication.translate("MainWindow", u"Deep", None))
        self.FAST.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.CLEAR.setText(QCoreApplication.translate("MainWindow", u"CLEAN", None))
    # retranslateUi

