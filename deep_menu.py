# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deep_menu.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDialog,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_DEEP_MENU(object):
    def setupUi(self, DEEP_MENU):
        if not DEEP_MENU.objectName():
            DEEP_MENU.setObjectName(u"DEEP_MENU")
        DEEP_MENU.resize(450, 730)
        DEEP_MENU.setMinimumSize(QSize(450, 730))
        DEEP_MENU.setMaximumSize(QSize(450, 730))
        DEEP_MENU.setStyleSheet(u"QDialog{\n"
"background: #151515;\n"
"color: #FBF9E4;\n"
"}\n"
"QCheckBox{\n"
"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color: #E2E8F0; \n"
"font-weight: 300;\n"
"border: 2px dotted #122C4F;\n"
"padding: 10px;\n"
"border-radius: 5px\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #888;\n"
"    border-radius: 4px;\n"
"    background: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: #2196F3;\n"
"	border: 2px solid #122C4F\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
" background-color: #3a3a3a; /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    border: 1px solid #444444; /* \u0420\u0430\u043c\u043a\u0430 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.DEEP_TEXT = QLabel(DEEP_MENU)
        self.DEEP_TEXT.setObjectName(u"DEEP_TEXT")
        self.DEEP_TEXT.setGeometry(QRect(-10, 5, 471, 40))
        self.DEEP_TEXT.setStyleSheet(u"color:white;\n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"font:9pt \"Aldrich\";\n"
"font-size: 25pt;\n"
"font-weight: 300;\n"
"background: #151515;\n"
"border-radius: 4px;\n"
"border: 2px solid #122C4F;")
        self.DEEP_TEXT.setAlignment(Qt.AlignCenter)
        self.WINDOWS = QLabel(DEEP_MENU)
        self.WINDOWS.setObjectName(u"WINDOWS")
        self.WINDOWS.setGeometry(QRect(10, 60, 431, 31))
        self.WINDOWS.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border: 2px solid  #122C4F;\n"
"\n"
"")
        self.WINDOWS.setAlignment(Qt.AlignCenter)
        self.checkBoxDEEP1 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP1.setObjectName(u"checkBoxDEEP1")
        self.checkBoxDEEP1.setGeometry(QRect(20, 100, 410, 41))
        self.checkBoxDEEP2 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP2.setObjectName(u"checkBoxDEEP2")
        self.checkBoxDEEP2.setGeometry(QRect(20, 150, 410, 41))
        self.checkBoxDEEP4 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP4.setObjectName(u"checkBoxDEEP4")
        self.checkBoxDEEP4.setGeometry(QRect(20, 200, 410, 51))
        self.CACHE = QLabel(DEEP_MENU)
        self.CACHE.setObjectName(u"CACHE")
        self.CACHE.setGeometry(QRect(10, 265, 431, 31))
        self.CACHE.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border: 2px solid  #122C4F;\n"
"\n"
"")
        self.CACHE.setAlignment(Qt.AlignCenter)
        self.checkBoxDEEP5 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP5.setObjectName(u"checkBoxDEEP5")
        self.checkBoxDEEP5.setGeometry(QRect(20, 310, 410, 51))
        self.checkBoxDEEP6 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP6.setObjectName(u"checkBoxDEEP6")
        self.checkBoxDEEP6.setGeometry(QRect(20, 370, 410, 51))
        self.USER = QLabel(DEEP_MENU)
        self.USER.setObjectName(u"USER")
        self.USER.setGeometry(QRect(10, 450, 431, 31))
        self.USER.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border: 2px solid  #122C4F;\n"
"\n"
"")
        self.USER.setAlignment(Qt.AlignCenter)
        self.checkBoxDEEP7 = QCheckBox(DEEP_MENU)
        self.checkBoxDEEP7.setObjectName(u"checkBoxDEEP7")
        self.checkBoxDEEP7.setGeometry(QRect(20, 510, 411, 51))
        self.checkBoxDEEP7.setStyleSheet(u"font-size: 18px\n"
"")
        self.Enter_number = QSpinBox(DEEP_MENU)
        self.Enter_number.setObjectName(u"Enter_number")
        self.Enter_number.setGeometry(QRect(370, 580, 61, 31))
        self.Enter_number.setStyleSheet(u"background: #151515;\n"
"color: #FBF9E4;\n"
"border: 2px solid  #122C4F;\n"
"font:9pt \"Aldrich\";\n"
"font-size: 14pt;\n"
"border-radius: 5px;")
        self.Enter_number.setAlignment(Qt.AlignCenter)
        self.Enter_number.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Enter_number.setValue(30)
        self.DELETE_FILES = QLabel(DEEP_MENU)
        self.DELETE_FILES.setObjectName(u"DELETE_FILES")
        self.DELETE_FILES.setGeometry(QRect(20, 580, 341, 31))
        self.DELETE_FILES.setStyleSheet(u"font:9pt \"Aldrich\";\n"
"font-size: 16pt;\n"
"color:  #5B88E2;\n"
"letter-spacing: 2px;\n"
"font-weight: 300;\n"
"border: 2px solid  #122C4F;\n"
"border-radius: 4px\n"
"")
        self.DELETE_FILES.setAlignment(Qt.AlignCenter)

        self.retranslateUi(DEEP_MENU)

        QMetaObject.connectSlotsByName(DEEP_MENU)
    # setupUi

    def retranslateUi(self, DEEP_MENU):
        DEEP_MENU.setWindowTitle(QCoreApplication.translate("DEEP_MENU", u"Dialog", None))
        self.DEEP_TEXT.setText(QCoreApplication.translate("DEEP_MENU", u"DEEP", None))
        self.WINDOWS.setText(QCoreApplication.translate("DEEP_MENU", u"Windows", None))
        self.checkBoxDEEP1.setText(QCoreApplication.translate("DEEP_MENU", u" Error Reports", None))
        self.checkBoxDEEP2.setText(QCoreApplication.translate("DEEP_MENU", u" Crash Dumps", None))
        self.checkBoxDEEP4.setText(QCoreApplication.translate("DEEP_MENU", u"Shader DX11 Cache", None))
        self.CACHE.setText(QCoreApplication.translate("DEEP_MENU", u"Cache", None))
        self.checkBoxDEEP5.setText(QCoreApplication.translate("DEEP_MENU", u" Chrome Cache", None))
        self.checkBoxDEEP6.setText(QCoreApplication.translate("DEEP_MENU", u" Discord Cache", None))
        self.USER.setText(QCoreApplication.translate("DEEP_MENU", u"User", None))
        self.checkBoxDEEP7.setText(QCoreApplication.translate("DEEP_MENU", u"Old Downloads", None))
        self.DELETE_FILES.setText(QCoreApplication.translate("DEEP_MENU", u"Delete files older than:", None))
    # retranslateUi

