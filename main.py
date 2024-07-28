from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(q_text,q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_qs():
    quiz.next_question()
    
print("You have completed your quiz.")
print(f"Your final score was: {quiz.score}/{quiz.q_no}")