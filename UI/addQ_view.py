# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addQ_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_question_view(object):
    def setupUi(self, add_question_view):
        add_question_view.setObjectName("add_question_view")
        add_question_view.resize(800, 599)
        self.frame = QtWidgets.QFrame(add_question_view)
        self.frame.setGeometry(QtCore.QRect(180, 130, 551, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rightA = QtWidgets.QLineEdit(self.frame)
        self.rightA.setGeometry(QtCore.QRect(70, 140, 421, 31))
        self.rightA.setText("")
        self.rightA.setObjectName("rightA")
        self.wrongA1 = QtWidgets.QLineEdit(self.frame)
        self.wrongA1.setGeometry(QtCore.QRect(70, 220, 421, 31))
        self.wrongA1.setText("")
        self.wrongA1.setObjectName("wrongA1")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 190, 551, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(238, 30, 251, 22))
        self.comboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.newQ = QtWidgets.QLineEdit(self.frame)
        self.newQ.setGeometry(QtCore.QRect(70, 80, 421, 31))
        self.newQ.setText("")
        self.newQ.setObjectName("newQ")
        self.wrongA1_2 = QtWidgets.QLineEdit(self.frame)
        self.wrongA1_2.setGeometry(QtCore.QRect(70, 280, 421, 31))
        self.wrongA1_2.setText("")
        self.wrongA1_2.setObjectName("wrongA1_2")
        self.wrongA1_3 = QtWidgets.QLineEdit(self.frame)
        self.wrongA1_3.setGeometry(QtCore.QRect(70, 340, 421, 31))
        self.wrongA1_3.setText("")
        self.wrongA1_3.setObjectName("wrongA1_3")
        self.frame_2 = QtWidgets.QFrame(add_question_view)
        self.frame_2.setGeometry(QtCore.QRect(50, 120, 120, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.sendButton = QtWidgets.QToolButton(self.frame_2)
        self.sendButton.setGeometry(QtCore.QRect(30, 30, 71, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/send-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon)
        self.sendButton.setIconSize(QtCore.QSize(30, 30))
        self.sendButton.setObjectName("sendButton")
        self.cancelButton = QtWidgets.QToolButton(self.frame_2)
        self.cancelButton.setGeometry(QtCore.QRect(30, 110, 71, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(30, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.frame_3 = QtWidgets.QFrame(add_question_view)
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QtCore.QRect(30, 50, 701, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
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
        self.scornumber = QtWidgets.QLCDNumber(self.frame_3)
        self.scornumber.setGeometry(QtCore.QRect(510, 0, 81, 71))
        self.scornumber.setProperty("value", 45.0)
        self.scornumber.setObjectName("scornumber")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 0, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.settings = QtWidgets.QPushButton(self.frame_3)
        self.settings.setGeometry(QtCore.QRect(280, 0, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QtCore.QSize(50, 50))
        self.settings.setObjectName("settings")

        self.retranslateUi(add_question_view)
        QtCore.QMetaObject.connectSlotsByName(add_question_view)

    def retranslateUi(self, add_question_view):
        _translate = QtCore.QCoreApplication.translate
        add_question_view.setWindowTitle(_translate("add_question_view", "Dialog"))
        self.rightA.setPlaceholderText(_translate("add_question_view", "הכנס כאן תשובה נכונה"))
        self.wrongA1.setPlaceholderText(_translate("add_question_view", "הכנס כאן תשובה לא נכונה"))
        self.comboBox.setCurrentText(_translate("add_question_view", "בחר קטגוריה"))
        self.comboBox.setItemText(0, _translate("add_question_view", "בחר קטגוריה"))
        self.comboBox.setItemText(1, _translate("add_question_view", "ספורט"))
        self.comboBox.setItemText(2, _translate("add_question_view", "מפורסמים בארץ"))
        self.comboBox.setItemText(3, _translate("add_question_view", "נטפליקס"))
        self.comboBox.setItemText(4, _translate("add_question_view", "SO 90\'s"))
        self.comboBox.setItemText(5, _translate("add_question_view", "מוזיקה ים תיכונית"))
        self.newQ.setPlaceholderText(_translate("add_question_view", "הוסף שאלה כאן.."))
        self.wrongA1_2.setPlaceholderText(_translate("add_question_view", "הכנס כאן תשובה לא נכונה"))
        self.wrongA1_3.setPlaceholderText(_translate("add_question_view", "הכנס כאן תשובה לא נכונה"))
        self.sendButton.setText(_translate("add_question_view", "..."))
        self.cancelButton.setText(_translate("add_question_view", "..."))
        self.label.setText(_translate("add_question_view", "נקודות"))
#import icon_rc
