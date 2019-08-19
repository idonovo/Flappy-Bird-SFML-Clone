class Question():
    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.type = None

    def get_question(self):
        pass

    def check_answer(self, answer):
        return self.answer == answer
