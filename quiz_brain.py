class QuizBrain:
    def __init__(self,q_list):
        self.q_no = 0
        self.score = 0
        self.q_list = q_list
    
    def next_question(self):
        current_question = self.q_list[self.q_no]
        self.q_no += 1
        user_ans = input(f"Q{self.q_no}. {current_question.text} (True/False):")
        self.check_ans(user_ans,current_question.answer)
        
    def still_has_qs(self):
        return self.q_no < len(self.q_list)
    
    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"Sorry, that's wrong")
        print(f"The correct answer was:{correct_ans}")
        print(f"Your current score is: {self.score}/{self.q_no}")
        print("\n")