class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        if self.question_number <= len(self.question_list)-1:
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it. Right!")
        else:
            print("That's Wrong!")
        print(f"The correct answer was: {current_answer}")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
        print("\n")