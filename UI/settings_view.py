# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_view(object):
    def setupUi(self, settings_view):
        settings_view.setObjectName("settings_view")
        settings_view.resize(797, 596)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(settings_view)
        self.plainTextEdit.setGeometry(QtCore.QRect(200, 230, 351, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_2 = QtWidgets.QFrame(settings_view)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(10, 60, 701, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(600, 5, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Guttman Yad-Brush")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scornumber = QtWidgets.QLCDNumber(self.frame_2)
        self.scornumber.setGeometry(QtCore.QRect(510, 0, 81, 71))
        self.scornumber.setProperty("value", 45.0)
        self.scornumber.setObjectName("scornumber")
        self.gameButton = QtWidgets.QPushButton(self.frame_2)
        self.gameButton.setGeometry(QtCore.QRect(60, 0, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gameButton.sizePolicy().hasHeightForWidth())
        self.gameButton.setSizePolicy(sizePolicy)
        self.gameButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gameButton.setIcon(icon)
        self.gameButton.setIconSize(QtCore.QSize(50, 50))
        self.gameButton.setObjectName("gameButton")
        self.settings = QtWidgets.QPushButton(self.frame_2)
        self.settings.setGeometry(QtCore.QRect(280, 0, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setIconSize(QtCore.QSize(50, 50))
        self.settings.setObjectName("settings")

        self.retranslateUi(settings_view)
        QtCore.QMetaObject.connectSlotsByName(settings_view)

    def retranslateUi(self, settings_view):
        _translate = QtCore.QCoreApplication.translate
        settings_view.setWindowTitle(_translate("settings_view", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("settings_view", "to be continuned..."))
        self.label.setText(_translate("settings_view", "נקודות"))
#import icon_rc
