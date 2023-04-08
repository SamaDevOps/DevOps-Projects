class QuizBrain:
    def __init__(self, question_bank):
        self.win_count = 0
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {current_question.question} True or False? : ")
        self.check_answer(answer, current_question)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer, current_question):
        if answer == current_question.answer:
            self.win_count += 1
            print(f"You are correct! {self.win_count}/{self.question_number}")