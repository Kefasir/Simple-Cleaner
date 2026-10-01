# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fast_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QSizePolicy, QWidget)

class Ui_FAST_MENU(object):
    def setupUi(self, FAST_MENU):
        if not FAST_MENU.objectName():
            FAST_MENU.setObjectName(u"FAST_MENU")
        FAST_MENU.resize(400, 591)
        FAST_MENU.setStyleSheet(u"QDialog{\n"
"background: #151515;\n"
"color: #FBF9E4;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"font:9pt \"Aldrich\";\n"
"font-size: 18pt;\n"
"font-weight: 300;\n"
"background: #5B88E2;\n"
"border-radius: 6px\n"
"}\n"
"\n"
"")
        self.FAST_TEXT_2 = QLabel(FAST_MENU)
        self.FAST_TEXT_2.setObjectName(u"FAST_TEXT_2")
        self.FAST_TEXT_2.setGeometry(QRect(140, 20, 110, 40))
        self.FAST_TEXT_2.setStyleSheet(u"color:white;\n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"font:9pt \"Aldrich\";\n"
"font-size: 25pt;\n"
"font-weight: 300;\n"
"background: #151515;\n"
"border-radius: 4px;\n"
"border: 2px solid #122C4F;")
        self.FAST_TEXT_2.setAlignment(Qt.AlignCenter)
        self.labelFAST1 = QLabel(FAST_MENU)
        self.labelFAST1.setObjectName(u"labelFAST1")
        self.labelFAST1.setGeometry(QRect(140, 120, 221, 72))
        self.labelFAST1.setStyleSheet(u"border: 2px solid #122C4F")
        self.labelFAST1.setAlignment(Qt.AlignCenter)
        self.checkBoxFAST1 = QCheckBox(FAST_MENU)
        self.checkBoxFAST1.setObjectName(u"checkBoxFAST1")
        self.checkBoxFAST1.setGeometry(QRect(100, 150, 21, 21))
        self.checkBoxFAST1.setStyleSheet(u"QCheckBox::indicator {\n"
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
"")
        self.checkBoxFAST1.setIconSize(QSize(16, 16))
        self.labelFAST2 = QLabel(FAST_MENU)
        self.labelFAST2.setObjectName(u"labelFAST2")
        self.labelFAST2.setGeometry(QRect(140, 210, 221, 72))
        self.labelFAST2.setStyleSheet(u"border: 2px solid #122C4F;\n"
"font-size: 24px")
        self.labelFAST2.setAlignment(Qt.AlignCenter)
        self.checkBoxFAST2 = QCheckBox(FAST_MENU)
        self.checkBoxFAST2.setObjectName(u"checkBoxFAST2")
        self.checkBoxFAST2.setGeometry(QRect(100, 240, 21, 21))
        self.checkBoxFAST2.setStyleSheet(u"QCheckBox::indicator {\n"
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
"")
        self.checkBoxFAST2.setIconSize(QSize(16, 16))
        self.labelFAST3 = QLabel(FAST_MENU)
        self.labelFAST3.setObjectName(u"labelFAST3")
        self.labelFAST3.setGeometry(QRect(140, 300, 221, 72))
        self.labelFAST3.setStyleSheet(u"border: 2px solid #122C4F;\n"
"font-size: 24px")
        self.labelFAST3.setAlignment(Qt.AlignCenter)
        self.checkBoxFAST3 = QCheckBox(FAST_MENU)
        self.checkBoxFAST3.setObjectName(u"checkBoxFAST3")
        self.checkBoxFAST3.setGeometry(QRect(100, 330, 21, 21))
        self.checkBoxFAST3.setStyleSheet(u"QCheckBox::indicator {\n"
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
"")
        self.checkBoxFAST3.setIconSize(QSize(16, 16))
        self.labelFAST4 = QLabel(FAST_MENU)
        self.labelFAST4.setObjectName(u"labelFAST4")
        self.labelFAST4.setGeometry(QRect(140, 390, 221, 71))
        self.labelFAST4.setStyleSheet(u"border: 2px solid #122C4F;\n"
"font-size: 24px")
        self.labelFAST4.setAlignment(Qt.AlignCenter)
        self.checkBoxFAST4 = QCheckBox(FAST_MENU)
        self.checkBoxFAST4.setObjectName(u"checkBoxFAST4")
        self.checkBoxFAST4.setGeometry(QRect(100, 420, 21, 21))
        self.checkBoxFAST4.setStyleSheet(u"QCheckBox::indicator {\n"
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
"")
        self.checkBoxFAST4.setIconSize(QSize(16, 16))

        self.retranslateUi(FAST_MENU)

        QMetaObject.connectSlotsByName(FAST_MENU)
    # setupUi

    def retranslateUi(self, FAST_MENU):
        FAST_MENU.setWindowTitle(QCoreApplication.translate("FAST_MENU", u"Dialog", None))
        self.FAST_TEXT_2.setText(QCoreApplication.translate("FAST_MENU", u"FAST", None))
        self.labelFAST1.setText(QCoreApplication.translate("FAST_MENU", u"C:/Temp", None))
        self.checkBoxFAST1.setText("")
        self.labelFAST2.setText(QCoreApplication.translate("FAST_MENU", u"Win/Temp", None))
        self.checkBoxFAST2.setText("")
        self.labelFAST3.setText(QCoreApplication.translate("FAST_MENU", u"AppData/Temp", None))
        self.checkBoxFAST3.setText("")
        self.labelFAST4.setText(QCoreApplication.translate("FAST_MENU", u"Recycle Bin", None))
        self.checkBoxFAST4.setText("")
    # retranslateUi

