# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_demo_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(745, 474)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 724, 447))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formGroupBox = QGroupBox(self.layoutWidget)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formLayout = QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.s1__lb_1 = QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName(u"s1__lb_1")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.s1__lb_1)

        self.s1__box_1 = QPushButton(self.formGroupBox)
        self.s1__box_1.setObjectName(u"s1__box_1")
        self.s1__box_1.setAutoRepeatInterval(100)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.s1__box_1)

        self.s1__lb_2 = QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName(u"s1__lb_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.s1__lb_2)

        self.s1__box_2 = QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName(u"s1__box_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.s1__box_2)

        self.s1__lb_3 = QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName(u"s1__lb_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.s1__lb_3)

        self.s1__box_3 = QComboBox(self.formGroupBox)
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.setObjectName(u"s1__box_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.s1__box_3)

        self.s1__lb_4 = QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName(u"s1__lb_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.s1__lb_4)

        self.s1__box_4 = QComboBox(self.formGroupBox)
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.setObjectName(u"s1__box_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.s1__box_4)

        self.s1__lb_5 = QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName(u"s1__lb_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.s1__lb_5)

        self.s1__box_5 = QComboBox(self.formGroupBox)
        self.s1__box_5.addItem("")
        self.s1__box_5.setObjectName(u"s1__box_5")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.s1__box_5)

        self.open_button = QPushButton(self.formGroupBox)
        self.open_button.setObjectName(u"open_button")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.open_button)

        self.close_button = QPushButton(self.formGroupBox)
        self.close_button.setObjectName(u"close_button")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.close_button)

        self.s1__lb_6 = QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName(u"s1__lb_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.s1__lb_6)

        self.s1__box_6 = QComboBox(self.formGroupBox)
        self.s1__box_6.addItem("")
        self.s1__box_6.setObjectName(u"s1__box_6")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.s1__box_6)

        self.state_label = QLabel(self.formGroupBox)
        self.state_label.setObjectName(u"state_label")
        self.state_label.setTextFormat(Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.state_label)


        self.gridLayout.addWidget(self.formGroupBox, 0, 0, 4, 1)

        self.verticalGroupBox = QGroupBox(self.layoutWidget)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalLayout = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.s2__receive_text = QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName(u"s2__receive_text")

        self.verticalLayout.addWidget(self.s2__receive_text)


        self.gridLayout.addWidget(self.verticalGroupBox, 0, 1, 2, 3)

        self.hex_receive = QCheckBox(self.layoutWidget)
        self.hex_receive.setObjectName(u"hex_receive")

        self.gridLayout.addWidget(self.hex_receive, 0, 4, 1, 1)

        self.s2__clear_button = QPushButton(self.layoutWidget)
        self.s2__clear_button.setObjectName(u"s2__clear_button")

        self.gridLayout.addWidget(self.s2__clear_button, 1, 4, 1, 1)

        self.verticalGroupBox_2 = QGroupBox(self.layoutWidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.s3__send_text = QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName(u"s3__send_text")

        self.verticalLayout_2.addWidget(self.s3__send_text)


        self.gridLayout.addWidget(self.verticalGroupBox_2, 2, 1, 3, 3)

        self.hex_send = QCheckBox(self.layoutWidget)
        self.hex_send.setObjectName(u"hex_send")

        self.gridLayout.addWidget(self.hex_send, 2, 4, 1, 1)

        self.s3__send_button = QPushButton(self.layoutWidget)
        self.s3__send_button.setObjectName(u"s3__send_button")

        self.gridLayout.addWidget(self.s3__send_button, 3, 4, 1, 1)

        self.formGroupBox1 = QGroupBox(self.layoutWidget)
        self.formGroupBox1.setObjectName(u"formGroupBox1")
        self.formLayout_2 = QFormLayout(self.formGroupBox1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.formGroupBox1)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formGroupBox1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addWidget(self.formGroupBox1, 4, 0, 2, 1)

        self.s3__clear_button = QPushButton(self.layoutWidget)
        self.s3__clear_button.setObjectName(u"s3__clear_button")

        self.gridLayout.addWidget(self.s3__clear_button, 4, 4, 1, 1)

        self.timer_send_cb = QCheckBox(self.layoutWidget)
        self.timer_send_cb.setObjectName(u"timer_send_cb")

        self.gridLayout.addWidget(self.timer_send_cb, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 5, 2, 1, 1)

        self.dw = QLabel(self.layoutWidget)
        self.dw.setObjectName(u"dw")

        self.gridLayout.addWidget(self.dw, 5, 3, 1, 1)


        self.retranslateUi(Form)

        self.s1__box_1.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.formGroupBox.setTitle(QCoreApplication.translate("Form", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.s1__lb_1.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u68c0\u6d4b\uff1a", None))
        self.s1__box_1.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u4e32\u53e3", None))
        self.s1__lb_2.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u9009\u62e9\uff1a", None))
        self.s1__lb_3.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387\uff1a", None))
        self.s1__box_3.setItemText(0, QCoreApplication.translate("Form", u"115200", None))
        self.s1__box_3.setItemText(1, QCoreApplication.translate("Form", u"2400", None))
        self.s1__box_3.setItemText(2, QCoreApplication.translate("Form", u"4800", None))
        self.s1__box_3.setItemText(3, QCoreApplication.translate("Form", u"9600", None))
        self.s1__box_3.setItemText(4, QCoreApplication.translate("Form", u"14400", None))
        self.s1__box_3.setItemText(5, QCoreApplication.translate("Form", u"19200", None))
        self.s1__box_3.setItemText(6, QCoreApplication.translate("Form", u"38400", None))
        self.s1__box_3.setItemText(7, QCoreApplication.translate("Form", u"57600", None))
        self.s1__box_3.setItemText(8, QCoreApplication.translate("Form", u"76800", None))
        self.s1__box_3.setItemText(9, QCoreApplication.translate("Form", u"12800", None))
        self.s1__box_3.setItemText(10, QCoreApplication.translate("Form", u"230400", None))
        self.s1__box_3.setItemText(11, QCoreApplication.translate("Form", u"460800", None))

        self.s1__lb_4.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u4f4d\uff1a", None))
        self.s1__box_4.setItemText(0, QCoreApplication.translate("Form", u"8", None))
        self.s1__box_4.setItemText(1, QCoreApplication.translate("Form", u"7", None))
        self.s1__box_4.setItemText(2, QCoreApplication.translate("Form", u"6", None))
        self.s1__box_4.setItemText(3, QCoreApplication.translate("Form", u"5", None))

        self.s1__lb_5.setText(QCoreApplication.translate("Form", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.s1__box_5.setItemText(0, QCoreApplication.translate("Form", u"N", None))

        self.open_button.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e32\u53e3", None))
        self.close_button.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u4e32\u53e3", None))
        self.s1__lb_6.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.s1__box_6.setItemText(0, QCoreApplication.translate("Form", u"1", None))

        self.state_label.setText("")
        self.verticalGroupBox.setTitle(QCoreApplication.translate("Form", u"\u63a5\u53d7\u533a", None))
        self.hex_receive.setText(QCoreApplication.translate("Form", u"Hex\u63a5\u6536", None))
        self.s2__clear_button.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("Form", u"\u53d1\u9001\u533a", None))
        self.s3__send_text.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:13.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">123456</span></p></body></html>", None))
        self.hex_send.setText(QCoreApplication.translate("Form", u"Hex\u53d1\u9001", None))
        self.s3__send_button.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.formGroupBox1.setTitle(QCoreApplication.translate("Form", u"\u4e32\u53e3\u72b6\u6001", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5df2\u63a5\u6536\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5df2\u53d1\u9001\uff1a", None))
        self.s3__clear_button.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.timer_send_cb.setText(QCoreApplication.translate("Form", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"1000", None))
        self.dw.setText(QCoreApplication.translate("Form", u"ms/\u6b21", None))
    # retranslateUi

