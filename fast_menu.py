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
        FAST_MENU.resize(400, 500)
        FAST_MENU.setMinimumSize(QSize(400, 500))
        FAST_MENU.setMaximumSize(QSize(400, 500))
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
"QCheckBox{\n"
"font:9pt \"Aldrich\";\n"
"font-size: 20pt;\n"
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
"")
        self.FAST_TEXT_2 = QLabel(FAST_MENU)
        self.FAST_TEXT_2.setObjectName(u"FAST_TEXT_2")
        self.FAST_TEXT_2.setGeometry(QRect(-5, 10, 411, 41))
        self.FAST_TEXT_2.setStyleSheet(u"color: #E2E8F0; \n"
"font-size: 20px;\n"
"letter-spacing: 2px;\n"
"font:9pt \"Aldrich\";\n"
"font-size: 25pt;\n"
"font-weight: 300;\n"
"background: #151515;\n"
"border-radius: 4px;\n"
"border: 2px solid #122C4F;")
        self.FAST_TEXT_2.setAlignment(Qt.AlignCenter)
        self.checkBoxFAST1 = QCheckBox(FAST_MENU)
        self.checkBoxFAST1.setObjectName(u"checkBoxFAST1")
        self.checkBoxFAST1.setGeometry(QRect(10, 90, 381, 71))
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
        self.checkBoxFAST1.setCheckable(True)
        self.checkBoxFAST1.setChecked(False)
        self.checkBoxFAST1_2 = QCheckBox(FAST_MENU)
        self.checkBoxFAST1_2.setObjectName(u"checkBoxFAST1_2")
        self.checkBoxFAST1_2.setGeometry(QRect(10, 180, 381, 71))
        self.checkBoxFAST1_2.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.checkBoxFAST1_2.setIconSize(QSize(16, 16))
        self.checkBoxFAST1_2.setCheckable(True)
        self.checkBoxFAST1_2.setChecked(False)
        self.checkBoxFAST1_4 = QCheckBox(FAST_MENU)
        self.checkBoxFAST1_4.setObjectName(u"checkBoxFAST1_4")
        self.checkBoxFAST1_4.setGeometry(QRect(10, 260, 381, 71))
        self.checkBoxFAST1_4.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.checkBoxFAST1_4.setIconSize(QSize(16, 16))
        self.checkBoxFAST1_4.setCheckable(True)
        self.checkBoxFAST1_4.setChecked(False)

        self.retranslateUi(FAST_MENU)

        QMetaObject.connectSlotsByName(FAST_MENU)
    # setupUi

    def retranslateUi(self, FAST_MENU):
        FAST_MENU.setWindowTitle(QCoreApplication.translate("FAST_MENU", u"Dialog", None))
        self.FAST_TEXT_2.setText(QCoreApplication.translate("FAST_MENU", u"FAST", None))
        self.checkBoxFAST1.setText(QCoreApplication.translate("FAST_MENU", u" C:/Temp", None))
        self.checkBoxFAST1_2.setText(QCoreApplication.translate("FAST_MENU", u" AppData/Temp", None))
        self.checkBoxFAST1_4.setText(QCoreApplication.translate("FAST_MENU", u" Recycle Bin", None))
    # retranslateUi

