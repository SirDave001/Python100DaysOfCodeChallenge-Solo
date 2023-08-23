import random
import time

class ArithmeticGame:
    def __init__(self, NumQuestions):
        self.NumQuestions = NumQuestions
    def GenerateQuestions(self):
        operand1 = random.randint(1, 45)
        operand2 = random.randint(1, 45)
        operator = random.choice(['+', '-', '//', '*'])
        if operator == '+':
            answer = operand1 + operand2
        if operator == '-':
            answer = operand1 - operand2
        if operator == '*':
            answer = operand1 * operand2
        if operator == '//':
            answer = operand1 // operand2
        question = f'{operand1} {operator} {operand2}'
        return question, answer
    def PlayGame(self):
        CorrectAns = 0
        StartTime = time.time()
        for i in range(self.NumQuestions):
            print(f'Question {i + 1}:')
            question, answer = self.GenerateQuestions()
            print(question)
            UserAnswer = int(input('What is your answer?: '))
            if UserAnswer == answer:
                CorrectAns += 1
                print('You are correct!')
            else:
                print(f'You are wrong. The correct answer is {answer}.')
        EndTime = time.time()
        print(f'You got {CorrectAns} questions right.')
        print('You used {0:.3f} seconds.'.format(EndTime - StartTime))



NewGame = ArithmeticGame(10)
NewGame.PlayGame()