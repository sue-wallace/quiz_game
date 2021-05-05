from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for x in question_data:
    """method to create a question object for each question"""

    text = (x['text'])
    answer = (x['answer'])
    q = Question(text, answer)
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f'You have completed the quiz, your final score was {quiz.score}/{quiz.question_number}')


