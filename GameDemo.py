from PyQt5.QtWidgets import QWidget, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QMainWindow, QAction, qApp, QApplication
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from MultiQuestion import MultiQuestion
import sys

class GameDemoMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #set toolbar

        self.toolbar = self.addToolBar('TriviaMainToolBar')
        go_to_home_window = QAction(self)
        go_to_home_window.setIcon(QIcon('house.png'))
        self.toolbar.addAction(go_to_home_window)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()

        go_to_settings = QAction(self)
        go_to_settings.setIcon(QIcon('settings.png'))
        go_to_settings.triggered.connect(self.go_to_settings_onClick)
        self.toolbar.addAction(go_to_settings)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()

        coin = QAction(self)
        coin.setIcon(QIcon('coin.png'))
        self.toolbar.addAction(coin)
        score = QLabel('score')
        self.toolbar.addWidget(score)

        self.addToolBar(self.toolbar)
        # set homepage main layout
        main_window_layout = QVBoxLayout()
        main_window_layout.setAlignment(QtCore.Qt.AlignCenter)
        start_game_button = QPushButton("start_game_button")
        start_game_button.setText("התחל משחק")
        start_game_button.clicked.connect(self.go_to_game_onClick)

        special_game_button = QPushButton("special_game_button")
        special_game_button.setText("טריוויה ספיישל")
        add_qustion_button = QPushButton("add_qustion_button")
        add_qustion_button.setText("הוסף שאלה")
        scoring_button = QPushButton()
        scoring_button.setIcon(QIcon('podium.png'))
        main_window_layout.addWidget(start_game_button)
        main_window_layout.addWidget(special_game_button)
        main_window_layout.addWidget(add_qustion_button)
        main_window_layout.addWidget(scoring_button)
        main_window_layout.setStretch(0, 1);
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_window_layout)
        self.setCentralWidget(self.central_widget)

        self.setGeometry(600, 600, 650, 550)
        self.setWindowTitle('trivia simulator')
        self.show()


        #self.show()
    def go_to_game_onClick(self):
        self.cams = GameWindow()
        self.cams.show()
        self.close()

    def go_to_settings_onClick(self):
        settings_window_layout = QVBoxLayout()
        settings_window_layout.addWidget()
        settings_screen = QWidget()
        self.central_widget = QLabel("settings")


class GameWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Game!')

        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.question = QLabel("the question")

        self.answer1 = QPushButton('1. ???')
        self.answer2 = QPushButton('2. ???')
        self.answer3 = QPushButton('3. ???')
        self.answer4 = QPushButton('4. ???')

        self.layout.addWidget(self.question)
        self.layout.addWidget(self.answer1)
        self.layout.addWidget(self.answer2)
        self.layout.addWidget(self.answer3)
        self.layout.addWidget(self.answer4)
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 250, 250)

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('settings')

        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.question = QLabel("the question")

        self.answer1 = QPushButton('1. ???')
        self.answer2 = QPushButton('2. ???')
        self.answer3 = QPushButton('3. ???')
        self.answer4 = QPushButton('4. ???')

        self.layout.addWidget(self.question)
        self.layout.addWidget(self.answer1)
        self.layout.addWidget(self.answer2)
        self.layout.addWidget(self.answer3)
        self.layout.addWidget(self.answer4)
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 250, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Plastique')
    ex = GameDemoMainWindow()
    sys.exit(app.exec_())
