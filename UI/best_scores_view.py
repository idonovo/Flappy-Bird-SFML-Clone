# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'best_scores.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_leaders_view(object):
    def setupUi(self, leaders_view):
        leaders_view.setObjectName("leaders_view")
        leaders_view.resize(801, 599)
        self.frame_2 = QtWidgets.QFrame(leaders_view)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(20, 50, 701, 80))
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
        self.home = QtWidgets.QPushButton(self.frame_2)
        self.home.setGeometry(QtCore.QRect(60, 0, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(50, 50))
        self.home.setObjectName("home")
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
        self.frame = QtWidgets.QFrame(leaders_view)
        self.frame.setGeometry(QtCore.QRect(100, 170, 631, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scores_table = QtWidgets.QTableWidget(self.frame)
        self.scores_table.setGeometry(QtCore.QRect(50, 110, 461, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scores_table.sizePolicy().hasHeightForWidth())
        self.scores_table.setSizePolicy(sizePolicy)
        self.scores_table.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.scores_table.setObjectName("scores_table")
        self.scores_table.setColumnCount(2)
        self.scores_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Guttman Yad-Brush")
        font.setPointSize(14)
        item.setFont(font)
        self.scores_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Guttman Yad-Brush")
        font.setPointSize(14)
        item.setFont(font)
        self.scores_table.setHorizontalHeaderItem(1, item)
        self.scores_table.verticalHeader().setDefaultSectionSize(30)
        self.player = QtWidgets.QLabel(self.frame)
        self.player.setGeometry(QtCore.QRect(416, 20, 81, 71))
        self.player.setText("")
        self.player.setPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/youtuber.png"))
        self.player.setScaledContents(True)
        self.player.setObjectName("player")
        self.score = QtWidgets.QLabel(self.frame)
        self.score.setGeometry(QtCore.QRect(290, 20, 71, 61))
        self.score.setText("")
        self.score.setPixmap(QtGui.QPixmap("D:/TriviaDemo/Trivia-Simulator/UI/resources/score.png"))
        self.score.setScaledContents(True)
        self.score.setObjectName("score")

        self.retranslateUi(leaders_view)
        QtCore.QMetaObject.connectSlotsByName(leaders_view)

    def retranslateUi(self, leaders_view):
        _translate = QtCore.QCoreApplication.translate
        leaders_view.setWindowTitle(_translate("leaders_view", "Dialog"))
        self.label.setText(_translate("leaders_view", "נקודות"))
        item = self.scores_table.horizontalHeaderItem(0)
        item.setText(_translate("leaders_view", "עידו נווה"))
        item = self.scores_table.horizontalHeaderItem(1)
        item.setText(_translate("leaders_view", "1500"))
#import icon_rc
