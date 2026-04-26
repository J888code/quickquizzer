def run_quiz(questions, answers):
    score = 0
    for i in range(len(questions)):
        x = input(questions[i]).lower().strip()
        if x == answers[i]:
            print("Correct")
            score += 1
        else:
            print(f"Incorrect. The answer was {answers[i]}")
    print(f"score: {score}")
def restart():
    print("1. Latin")
    print("2. Spanish")
    print("3. python")
    print("4. quit")
    try:
        b = int(input())
        if b== 1:
            print("salve")
            run_quiz(latin_questions, latin_answers)
            restart()
        elif b == 2:
            print("vamos")
            run_quiz(spanish_questions, spanish_answers)
            restart()
        elif b == 3:
            print("loading...")
            print("loading complete!")
            run_quiz(python_questions, python_answers)
            restart()
        else:
            print("Invalid input")
            print("Please enter a number")
    except ValueError:
        print("Please enter an integer")
        return
def main_menu():
    print("Welcome to Quick Quizzer!")
    print("Choose a quiz:")
    print("1. Latin")
    print("2. Spanish")
    print("3. python")
    print("More coming soon!!")
    try:
        a = int(input())
    except ValueError:
        print("please enter a number")
        return
    if a == 1:
        print("salve")
        run_quiz(latin_questions, latin_answers)
        restart()
    elif a == 2:
        print("vamos")
        run_quiz(spanish_questions, spanish_answers)
        restart()
    elif a == 3:
        print("loading...")
        print("loading complete!")
        run_quiz(python_questions, python_answers)
        restart()
    else:
        print("Invalid input")
        print("Please enter a number")
latin_questions = ["I love: ", "I loved: ", "spear: "]
latin_answers = ["amo", "amavi", "hasta"]
spanish_questions = ["hello: ", "I like: ", "here: "]
spanish_answers = ["hola", "me gusta", "aqui"]
python_questions = ["print 'Hello world': "]
python_answers = ["print('Hello world')"]
main_menu()