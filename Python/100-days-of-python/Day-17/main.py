from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# win_count = 0

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# for i in range(len(question_bank)):
#     answer = input(f"{question_bank[i].question} True or false? : ")
#     if answer == question_bank[i].answer:
#         win_count += 1
#         print(f"You are correct! {win_count}/{i + 1}")

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()
