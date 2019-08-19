from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from MultiQuestion import MultiQuestion
import sys

class GameDemoMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.toolbar = self.addToolBar('TriviaMainToolBar')

        go_to_home_window = QAction(self)
        go_to_home_window.setIcon(QIcon('house.png'))
        self.toolbar.addAction(go_to_home_window)

        go_to_settings = QAction(self)
        go_to_settings.setIcon(QIcon('settings.png'))
        self.toolbar.addAction(go_to_settings)

        self.addToolBar(self.toolbar)

        main_window_layout = QVBoxLayout()
        start_game_button = QPushButton("start_game_button")
        start_game_button.setText("התחל משחק")
        special_game_button = QPushButton("special_game_button")
        special_game_button.setText("טריויה ספיישל")

        main_window_layout.addWidget(start_game_button)
        main_window_layout.addWidget(special_game_button)

        self.setLayout(main_window_layout)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('trivia simulator')
        self.show()

      #  self.layout = QVBoxLayout()
       # self.question = QLabel("the question")
        #self.answer1 = QPushButton('1. ???')
       # self.answer2 = QPushButton('2. ???')
       # self.answer3 = QPushButton('3. ???')
        #self.answer4 = QPushButton('4. ???')

      #  self.layout.addWidget(self.question)
       # self.layout.addWidget(self.answer1)
        #self.layout.addWidget(self.answer2)
        #self.layout.addWidget(self.answer3)
        #self.layout.addWidget(self.answer4)
        #self.setLayout(self.layout)

       # self.setGeometry(700, 700, 700, 700)
        #self.setWindowTitle('Trivia Simulation')
        #self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameDemoMainWindow()
    sys.exit(app.exec_())
