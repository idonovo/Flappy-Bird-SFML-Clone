from MultiQuestion import MultiQuestion


class QuestionSet():
    def __init__(self, q_list, mistakes_limit):
        self.q_list = q_list
        self.mistakes_limit = mistakes_limit
        self.user_mistakes = 0
        self.current_q = 0

    def get_next_question(self):
        if self.current_q < len(self.q_list):
            ++self.current_q;
            return self.q_list[self.current_q].get_question()
        else:
            return "End Of Question Set"

    def is_end_of_question_set(self):
        return self.current_q < len(self.q_list)


    def check_answer(self, answer):
        if self.q_list[self.current_q].check_answer(answer) == True:
            return True

        ++self.user_mistakes
        return -1 if self.user_mistakes < self.mistakes_limit else False

    def times_up(self):
         ++self.user_mistakes
         return -1 if self.user_mistakes < self.mistakes_limit else False
