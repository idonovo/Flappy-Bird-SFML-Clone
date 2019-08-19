from Question import Question

class MultiQuestion(Question):
    def __init__(self, question, answer, options, difficulty):
        super().__init__(question, answer, difficulty)
        self.options = options
        self.type = "multi"

    def get_question(self):
        return {
            "type": self.type,
            "question": self.question,
            "1": self.options[0],
            "2": self.options[1],
            "3": self.options[2],
            "4": self.options[3]}
