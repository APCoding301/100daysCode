from question_model import Question
#from data import question_data
from data import get_data_from_triviaDB
from quiz_brain import QuizBrain

question_bank = []
question_data = get_data_from_triviaDB()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
