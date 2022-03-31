# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '毕设.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1297, 502)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.horizontalLayout_27 = QHBoxLayout(mainWindow)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.camWindow = QLabel(mainWindow)
        self.camWindow.setObjectName(u"camWindow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camWindow.sizePolicy().hasHeightForWidth())
        self.camWindow.setSizePolicy(sizePolicy1)
        self.camWindow.setMinimumSize(QSize(640, 400))

        self.verticalLayout_2.addWidget(self.camWindow)

        self.camButton = QPushButton(mainWindow)
        self.camButton.setObjectName(u"camButton")
        self.camButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.camButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gestureTips = QLabel(mainWindow)
        self.gestureTips.setObjectName(u"gestureTips")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gestureTips.sizePolicy().hasHeightForWidth())
        self.gestureTips.setSizePolicy(sizePolicy2)
        self.gestureTips.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.gestureTips)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gestureText = QLabel(mainWindow)
        self.gestureText.setObjectName(u"gestureText")
        sizePolicy2.setHeightForWidth(self.gestureText.sizePolicy().hasHeightForWidth())
        self.gestureText.setSizePolicy(sizePolicy2)
        self.gestureText.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.gestureText)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_27.addLayout(self.verticalLayout_2)

        self.line = QFrame(mainWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_27.addWidget(self.line)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.handconnectButton = QPushButton(mainWindow)
        self.handconnectButton.setObjectName(u"handconnectButton")
        self.handconnectButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_9.addWidget(self.handconnectButton)

        self.line_2 = QFrame(mainWindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.xiaozhiState = QPushButton(mainWindow)
        self.xiaozhiState.setObjectName(u"xiaozhiState")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.xiaozhiState.sizePolicy().hasHeightForWidth())
        self.xiaozhiState.setSizePolicy(sizePolicy3)
        self.xiaozhiState.setMinimumSize(QSize(0, 50))
        self.xiaozhiState.setMaximumSize(QSize(50, 16777215))
        self.xiaozhiState.setStyleSheet(u"backgroud_color: rgb(85, 170, 127);")

        self.horizontalLayout_18.addWidget(self.xiaozhiState)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.xiaozhiCheck = QCheckBox(mainWindow)
        self.xiaozhiCheck.setObjectName(u"xiaozhiCheck")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.xiaozhiCheck.sizePolicy().hasHeightForWidth())
        self.xiaozhiCheck.setSizePolicy(sizePolicy4)

        self.horizontalLayout_19.addWidget(self.xiaozhiCheck)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(7)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.xiaozhiSlider = QSlider(mainWindow)
        self.xiaozhiSlider.setObjectName(u"xiaozhiSlider")
        self.xiaozhiSlider.setMaximum(100)
        self.xiaozhiSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.xiaozhiSlider)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.xiaozhiBox = QSpinBox(mainWindow)
        self.xiaozhiBox.setObjectName(u"xiaozhiBox")
        self.xiaozhiBox.setMaximumSize(QSize(50, 16777215))
        self.xiaozhiBox.setMaximum(100)

        self.horizontalLayout_21.addWidget(self.xiaozhiBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_26.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.wumingzhiState = QPushButton(mainWindow)
        self.wumingzhiState.setObjectName(u"wumingzhiState")
        sizePolicy3.setHeightForWidth(self.wumingzhiState.sizePolicy().hasHeightForWidth())
        self.wumingzhiState.setSizePolicy(sizePolicy3)
        self.wumingzhiState.setMinimumSize(QSize(0, 50))
        self.wumingzhiState.setMaximumSize(QSize(50, 16777215))
        self.wumingzhiState.setStyleSheet(u"backgroud_color: rgb(85, 170, 127);\n"
"")

        self.horizontalLayout_22.addWidget(self.wumingzhiState)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.wumingzhiCheck = QCheckBox(mainWindow)
        self.wumingzhiCheck.setObjectName(u"wumingzhiCheck")
        sizePolicy4.setHeightForWidth(self.wumingzhiCheck.sizePolicy().hasHeightForWidth())
        self.wumingzhiCheck.setSizePolicy(sizePolicy4)

        self.horizontalLayout_23.addWidget(self.wumingzhiCheck)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.wumingzhiSlider = QSlider(mainWindow)
        self.wumingzhiSlider.setObjectName(u"wumingzhiSlider")
        self.wumingzhiSlider.setMaximum(100)
        self.wumingzhiSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_24.addWidget(self.wumingzhiSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.wumingzhiBox = QSpinBox(mainWindow)
        self.wumingzhiBox.setObjectName(u"wumingzhiBox")
        self.wumingzhiBox.setMaximumSize(QSize(50, 16777215))
        self.wumingzhiBox.setMaximum(100)

        self.horizontalLayout_25.addWidget(self.wumingzhiBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_26.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.zhongzhiState = QPushButton(mainWindow)
        self.zhongzhiState.setObjectName(u"zhongzhiState")
        sizePolicy3.setHeightForWidth(self.zhongzhiState.sizePolicy().hasHeightForWidth())
        self.zhongzhiState.setSizePolicy(sizePolicy3)
        self.zhongzhiState.setMinimumSize(QSize(0, 50))
        self.zhongzhiState.setMaximumSize(QSize(50, 16777215))
        self.zhongzhiState.setStyleSheet(u"backgroud_color: rgb(85, 170, 127);\n"
"")

        self.horizontalLayout_14.addWidget(self.zhongzhiState)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.zhongzhiCheck = QCheckBox(mainWindow)
        self.zhongzhiCheck.setObjectName(u"zhongzhiCheck")
        sizePolicy4.setHeightForWidth(self.zhongzhiCheck.sizePolicy().hasHeightForWidth())
        self.zhongzhiCheck.setSizePolicy(sizePolicy4)

        self.horizontalLayout_15.addWidget(self.zhongzhiCheck)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.zhongzhiSlider = QSlider(mainWindow)
        self.zhongzhiSlider.setObjectName(u"zhongzhiSlider")
        self.zhongzhiSlider.setMaximum(100)
        self.zhongzhiSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_16.addWidget(self.zhongzhiSlider)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.zhongzhiBox = QSpinBox(mainWindow)
        self.zhongzhiBox.setObjectName(u"zhongzhiBox")
        self.zhongzhiBox.setMaximumSize(QSize(50, 16777215))
        self.zhongzhiBox.setMaximum(100)

        self.horizontalLayout_17.addWidget(self.zhongzhiBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_26.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.shizhiState = QPushButton(mainWindow)
        self.shizhiState.setObjectName(u"shizhiState")
        sizePolicy3.setHeightForWidth(self.shizhiState.sizePolicy().hasHeightForWidth())
        self.shizhiState.setSizePolicy(sizePolicy3)
        self.shizhiState.setMinimumSize(QSize(0, 50))
        self.shizhiState.setMaximumSize(QSize(50, 16777215))
        self.shizhiState.setStyleSheet(u"backgroud_color: rgb(85, 170, 127);\n"
"")

        self.horizontalLayout_10.addWidget(self.shizhiState)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.shizhiCheck = QCheckBox(mainWindow)
        self.shizhiCheck.setObjectName(u"shizhiCheck")
        sizePolicy4.setHeightForWidth(self.shizhiCheck.sizePolicy().hasHeightForWidth())
        self.shizhiCheck.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.shizhiCheck)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.shizhiSlider = QSlider(mainWindow)
        self.shizhiSlider.setObjectName(u"shizhiSlider")
        self.shizhiSlider.setMaximum(100)
        self.shizhiSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_12.addWidget(self.shizhiSlider)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.shizhiBox = QSpinBox(mainWindow)
        self.shizhiBox.setObjectName(u"shizhiBox")
        self.shizhiBox.setMaximumSize(QSize(50, 16777215))
        self.shizhiBox.setMaximum(100)

        self.horizontalLayout_13.addWidget(self.shizhiBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_26.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.muzhiState = QPushButton(mainWindow)
        self.muzhiState.setObjectName(u"muzhiState")
        sizePolicy3.setHeightForWidth(self.muzhiState.sizePolicy().hasHeightForWidth())
        self.muzhiState.setSizePolicy(sizePolicy3)
        self.muzhiState.setMinimumSize(QSize(0, 50))
        self.muzhiState.setMaximumSize(QSize(50, 16777215))
        self.muzhiState.setStyleSheet(u"backgroud_color: rgb(85, 170, 127);\n"
"")

        self.horizontalLayout_5.addWidget(self.muzhiState)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.muzhiCheck = QCheckBox(mainWindow)
        self.muzhiCheck.setObjectName(u"muzhiCheck")
        sizePolicy4.setHeightForWidth(self.muzhiCheck.sizePolicy().hasHeightForWidth())
        self.muzhiCheck.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.muzhiCheck)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.muzhiSlider = QSlider(mainWindow)
        self.muzhiSlider.setObjectName(u"muzhiSlider")
        self.muzhiSlider.setMaximum(100)
        self.muzhiSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_7.addWidget(self.muzhiSlider)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.muzhiBox = QSpinBox(mainWindow)
        self.muzhiBox.setObjectName(u"muzhiBox")
        self.muzhiBox.setMaximumSize(QSize(50, 16777215))
        self.muzhiBox.setMaximum(100)

        self.horizontalLayout_8.addWidget(self.muzhiBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_26.addLayout(self.verticalLayout_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_27.addLayout(self.verticalLayout_9)

        self.line_4 = QFrame(mainWindow)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_27.addWidget(self.line_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.num5Button = QPushButton(mainWindow)
        self.num5Button.setObjectName(u"num5Button")
        self.num5Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num5Button, 5, 1, 1, 1)

        self.num2Button = QPushButton(mainWindow)
        self.num2Button.setObjectName(u"num2Button")
        self.num2Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num2Button, 6, 1, 1, 1)

        self.numbermodeChoice = QRadioButton(mainWindow)
        self.numbermodeChoice.setObjectName(u"numbermodeChoice")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.numbermodeChoice.sizePolicy().hasHeightForWidth())
        self.numbermodeChoice.setSizePolicy(sizePolicy5)
        self.numbermodeChoice.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.numbermodeChoice, 3, 2, 1, 1)

        self.num8Button = QPushButton(mainWindow)
        self.num8Button.setObjectName(u"num8Button")
        self.num8Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num8Button, 4, 1, 1, 1)

        self.num0Button = QPushButton(mainWindow)
        self.num0Button.setObjectName(u"num0Button")
        self.num0Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num0Button, 3, 0, 1, 1)

        self.num3Button = QPushButton(mainWindow)
        self.num3Button.setObjectName(u"num3Button")
        self.num3Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num3Button, 6, 2, 1, 1)

        self.num6Button = QPushButton(mainWindow)
        self.num6Button.setObjectName(u"num6Button")
        self.num6Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num6Button, 5, 2, 1, 1)

        self.num9Button = QPushButton(mainWindow)
        self.num9Button.setObjectName(u"num9Button")
        self.num9Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num9Button, 4, 2, 1, 1)

        self.num1Button = QPushButton(mainWindow)
        self.num1Button.setObjectName(u"num1Button")
        self.num1Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num1Button, 6, 0, 1, 1)

        self.num7Button = QPushButton(mainWindow)
        self.num7Button.setObjectName(u"num7Button")
        self.num7Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num7Button, 4, 0, 1, 1)

        self.num4Button = QPushButton(mainWindow)
        self.num4Button.setObjectName(u"num4Button")
        self.num4Button.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.num4Button, 5, 0, 1, 1)

        self.comboBox = QComboBox(mainWindow)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.line_3 = QFrame(mainWindow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 3)

        self.comboBox_2 = QComboBox(mainWindow)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 2, 1, 1)

        self.label = QLabel(mainWindow)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.line_8 = QFrame(mainWindow)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_8)

        self.followmodeChoice = QRadioButton(mainWindow)
        self.followmodeChoice.setObjectName(u"followmodeChoice")
        self.followmodeChoice.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_4.addWidget(self.followmodeChoice)

        self.line_5 = QFrame(mainWindow)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.gamblemodeChoice = QRadioButton(mainWindow)
        self.gamblemodeChoice.setObjectName(u"gamblemodeChoice")
        self.gamblemodeChoice.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_4.addWidget(self.gamblemodeChoice)

        self.line_6 = QFrame(mainWindow)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.recordmodeChoice = QRadioButton(mainWindow)
        self.recordmodeChoice.setObjectName(u"recordmodeChoice")
        self.recordmodeChoice.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_4.addWidget(self.recordmodeChoice)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.recordStart = QPushButton(mainWindow)
        self.recordStart.setObjectName(u"recordStart")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.recordStart.sizePolicy().hasHeightForWidth())
        self.recordStart.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.recordStart)

        self.recordEnd = QPushButton(mainWindow)
        self.recordEnd.setObjectName(u"recordEnd")
        sizePolicy6.setHeightForWidth(self.recordEnd.sizePolicy().hasHeightForWidth())
        self.recordEnd.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.recordEnd)

        self.recordPlay = QPushButton(mainWindow)
        self.recordPlay.setObjectName(u"recordPlay")

        self.verticalLayout_10.addWidget(self.recordPlay)


        self.verticalLayout_4.addLayout(self.verticalLayout_10)

        self.progressBar = QProgressBar(mainWindow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.line_7 = QFrame(mainWindow)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_7)

        self.onemoreThing = QRadioButton(mainWindow)
        self.onemoreThing.setObjectName(u"onemoreThing")
        self.onemoreThing.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_4.addWidget(self.onemoreThing)


        self.horizontalLayout_27.addLayout(self.verticalLayout_4)


        self.retranslateUi(mainWindow)
        self.xiaozhiBox.valueChanged.connect(self.xiaozhiSlider.setValue)
        self.zhongzhiBox.valueChanged.connect(self.zhongzhiSlider.setValue)
        self.wumingzhiBox.valueChanged.connect(self.wumingzhiSlider.setValue)
        self.shizhiBox.valueChanged.connect(self.shizhiSlider.setValue)
        self.muzhiBox.valueChanged.connect(self.muzhiSlider.setValue)
        self.xiaozhiSlider.valueChanged.connect(self.xiaozhiBox.setValue)
        self.zhongzhiSlider.valueChanged.connect(self.zhongzhiBox.setValue)
        self.wumingzhiSlider.valueChanged.connect(self.wumingzhiBox.setValue)
        self.shizhiSlider.valueChanged.connect(self.shizhiBox.setValue)
        self.muzhiSlider.valueChanged.connect(self.muzhiBox.setValue)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u57fa\u4e8e\u673a\u5668\u89c6\u89c9\u7684\u667a\u80fd\u673a\u68b0\u624b\u638c\u4e0a\u4f4d\u673a", None))
        self.camWindow.setText("")
        self.camButton.setText(QCoreApplication.translate("mainWindow", u"\u5355\u51fb\u4ee5 \u5f00\u59cb|\u7ed3\u675f \u6444\u50cf\u5934\u753b\u9762", None))
        self.gestureTips.setText(QCoreApplication.translate("mainWindow", u"\u5f53\u524d\u7684\u624b\u52bf\u5185\u5bb9\u4e3a:", None))
        self.gestureText.setText(QCoreApplication.translate("mainWindow", u"\u6570\u5b57\u4e94", None))
        self.handconnectButton.setText(QCoreApplication.translate("mainWindow", u"\u5355\u51fb\u4ee5 \u8fde\u63a5|\u65ad\u5f00 \u673a\u68b0\u624b\u638c", None))
        self.xiaozhiState.setText(QCoreApplication.translate("mainWindow", u"\u5c0f\u6307", None))
        self.xiaozhiCheck.setText("")
        self.wumingzhiState.setText(QCoreApplication.translate("mainWindow", u"\u65e0\u540d\u6307", None))
        self.wumingzhiCheck.setText("")
        self.zhongzhiState.setText(QCoreApplication.translate("mainWindow", u"\u4e2d\u6307", None))
        self.zhongzhiCheck.setText("")
        self.shizhiState.setText(QCoreApplication.translate("mainWindow", u"\u98df\u6307", None))
        self.shizhiCheck.setText("")
        self.muzhiState.setText(QCoreApplication.translate("mainWindow", u"\u62c7\u6307", None))
        self.muzhiCheck.setText("")
        self.num5Button.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.num2Button.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.numbermodeChoice.setText(QCoreApplication.translate("mainWindow", u"\u6570\u5b57\u624b\u52bf", None))
        self.num8Button.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.num0Button.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.num3Button.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.num6Button.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.num9Button.setText(QCoreApplication.translate("mainWindow", u"9", None))
        self.num1Button.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.num7Button.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.num4Button.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("mainWindow", u"9600", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("mainWindow", u"14400", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("mainWindow", u"19200", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("mainWindow", u"38400", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("mainWindow", u"56000", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("mainWindow", u"57600", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("mainWindow", u"115200", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("mainWindow", u"128000", None))

        self.label.setText(QCoreApplication.translate("mainWindow", u"\u4e32\u53e3|\u6ce2\u7279\u7387", None))
        self.followmodeChoice.setText(QCoreApplication.translate("mainWindow", u"\u624b\u52bf\u8ddf\u968f\uff08\u987b\u5f00\u542f\u6444\u50cf\u5934\uff09", None))
        self.gamblemodeChoice.setText(QCoreApplication.translate("mainWindow", u"\u4eba\u673a\u5212\u62f3\uff08\u987b\u5f00\u542f\u6444\u50cf\u5934\uff09", None))
        self.recordmodeChoice.setText(QCoreApplication.translate("mainWindow", u"\u5f55\u5236\u52a8\u4f5c\uff08\u987b\u5f00\u542f\u6444\u50cf\u5934\uff09", None))
        self.recordStart.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u5f55\u5236", None))
        self.recordEnd.setText(QCoreApplication.translate("mainWindow", u"\u7ed3\u675f\u5f55\u5236", None))
        self.recordPlay.setText(QCoreApplication.translate("mainWindow", u"\u64ad\u653e\u52a8\u4f5c", None))
        self.onemoreThing.setText(QCoreApplication.translate("mainWindow", u"(\u6a21\u5f0f\u6e05\u7a7a)\u66f4\u591a\u6a21\u5f0f\u5f00\u53d1\u4e2d\u2026\u2026", None))
    # retranslateUi

