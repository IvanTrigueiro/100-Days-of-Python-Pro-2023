from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(0, len(question_data)):
    question_text = question_data[i]['text']
    question_answer = question_data[i]['answer']
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
quiz.next_question()
