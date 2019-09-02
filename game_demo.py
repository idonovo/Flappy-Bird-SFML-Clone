from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from UI import main_window, game_view, settings_view, special_view, best_scores_view, addQ_view
import sys

def get_settings_dial():
    u = Game_Settings_Dialog()
    u.exec_()

def show_game_dial():
    u = Game_View_Dialog()
    u.exec_()

def show_settings_dial():
    get_settings_dial()

def show_game_specials():
    u = Game_Specials_Dialog()
    u.exec_()

def show_leaders_dial():
    u = Best_Scores_Dialog()
    u.exec_()

def show_addQ_dialog():
    u = AddQ_Dialog()
    u.exec_()


class Game_Main_Window(main_window.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window.Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(show_game_dial)
        self.settings.clicked.connect(get_settings_dial)
        self.pushButton_4.clicked.connect(show_game_specials)
        self.scores_button.clicked.connect(show_leaders_dial)
        self.pushButton_5.clicked.connect(show_addQ_dialog)


class Game_View_Dialog(game_view.Ui_game_dialog, QtWidgets.QDialog):
    def __init__(self):
        super(game_view.Ui_game_dialog,self).__init__()
        self.setupUi(self)


class Game_Settings_Dialog(settings_view. Ui_settings_view, QtWidgets.QDialog):
    def __init__(self):
        super( settings_view. Ui_settings_view,self).__init__()
        self.setupUi(self)
        self.gameButton.clicked.connect(self.close)


class Best_Scores_Dialog(best_scores_view.Ui_leaders_view, QtWidgets.QDialog):
    def __init__(self):
        super(best_scores_view.Ui_leaders_view,self).__init__()
        self.setupUi(self)
        self.home.clicked.connect(self.close)
        self.settings.clicked.connect(self.show_settings_dial)

    def show_settings_dial(self):
        self.close()
        get_settings_dial()

class Game_Specials_Dialog(special_view.Ui_special_view, QtWidgets.QDialog):
    def __init__(self):
        super(special_view.Ui_special_view, self).__init__()
        self.setupUi(self)
        self.gameButton.clicked.connect(self.close)
        self.settings.clicked.connect(self.show_settings_dial)

    def show_settings_dial(self):
        self.close()
        get_settings_dial()

class AddQ_Dialog(addQ_view.Ui_add_question_view, QtWidgets.QDialog):
    def __init__(self):
        super(addQ_view.Ui_add_question_view, self).__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.close)
        self.settings.clicked.connect(self.show_settings_dial)
        self.cancelButton.clicked.connect(self.clear_fields)
        self.sendButton.clicked.connect(self.get_new_question)
        self.fields = [self.newQ, self.rightA, self.wrongA1,  self.wrongA1_2, self.wrongA1_3]

    def show_settings_dial(self):
        self.close()
        get_settings_dial()

    def clear_fields(self):
        for line in self.fields:
            line.setText("")

    def get_new_question(self):
        q_dic = {}
        q_dic[self.comboBox.objectName()] = self.comboBox.currentText()
        for line in self.fields:
            q_dic[line.objectName()] = line.text()
            line.setText("")

        return q_dic
    #def open_settings(self):
      #  u = Game_Settings_Dialog()
     #   u.exec_()
    #    self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Game_Main_Window()
    my_app.show()
    app.exec()