from Question import Question
question_prompts = [
    "LCD or LED monitors are also called?\n(a) vertical panal display\n(b) round panael display\n(c) flat panel display\n(d) straight panel displays "
    " The metal or plastic box that contains all the components is called?\n(a) brief case\n(b) computer case\n(c) metal case\n(d) box case "
    " One of the following cannot be connected to the computer?\n(a) microphone\n(b) light pen\n(c) mouse\n(d) none of the above "
    " There are ------ types of keyboards?\n(a) 5\n(b) 6\n(c) 2\n(d) 4 "
    " The ------- and ------ are the types of mouse?\n(a) optical, nautical\n(b) mechanical and technical\n(c) optical and mechanical\n(d) cordless and wired "
    " Power button, DVD drive, audio port are found in the ----- of the computer case?\n(a) side\n(b) back\n(c) front\n(d) under "
    
]
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "c"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" (len(questions)) + " correct ")

run_test(questions)

