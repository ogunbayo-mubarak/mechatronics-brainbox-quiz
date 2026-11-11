"""
MECHATRONICS BRAINBOX
An interactive 20-question multiple-choice quiz application.

Student: OGUNBAYO MUBARAK ENIOLA
Course: CTE213
"""

import random

STUDENT_NAME = "OGUNBAYO MUBARAK ENIOLA"

QUESTIONS = [
    {
        "question": "Which of the following best describes mechatronics?",
        "options": [
            "A. The study of engines only",
            "B. The integration of mechanical, electronic, computer and control systems",
            "C. The study of building construction",
            "D. The design of electrical cables only",
        ],
        "answer": "B",
        "explanation": "Mechatronics combines mechanical engineering, electronics, computing and control."
    },
    {
        "question": "Which component is commonly regarded as the brain of an automated system?",
        "options": [
            "A. Sensor",
            "B. Actuator",
            "C. Controller",
            "D. Bearing",
        ],
        "answer": "C",
        "explanation": "The controller processes input information and determines the system's response."
    },
    {
        "question": "What is the main function of a sensor?",
        "options": [
            "A. To detect or measure a physical quantity",
            "B. To store mechanical energy",
            "C. To increase friction",
            "D. To supply compressed air",
        ],
        "answer": "A",
        "explanation": "A sensor detects a physical condition and converts it into a usable signal."
    },
    {
        "question": "Which device converts electrical energy into mechanical motion?",
        "options": [
            "A. Resistor",
            "B. Actuator",
            "C. Fuse",
            "D. Thermistor",
        ],
        "answer": "B",
        "explanation": "An actuator produces physical movement from an input signal or energy source."
    },
    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Power Line Connector",
            "B. Programmable Logic Controller",
            "C. Process Level Circuit",
            "D. Programmed Load Control",
        ],
        "answer": "B",
        "explanation": "PLC means Programmable Logic Controller."
    },
    {
        "question": "Which programming language is widely used for beginner programming and automation tasks?",
        "options": [
            "A. Python",
            "B. HTML only",
            "C. CSS",
            "D. XML only",
        ],
        "answer": "A",
        "explanation": "Python is widely used for scripting, automation, data analysis and control-related projects."
    },
    {
        "question": "In Python, which symbol is used to begin a comment on a single line?",
        "options": [
            "A. //",
            "B. <!--",
            "C. #",
            "D. **",
        ],
        "answer": "C",
        "explanation": "A hash symbol (#) begins a single-line comment in Python."
    },
    {
        "question": "Which Python function displays information on the screen?",
        "options": [
            "A. input()",
            "B. print()",
            "C. len()",
            "D. type()",
        ],
        "answer": "B",
        "explanation": "print() displays text or other values in the output."
    },
    {
        "question": "What is the SI unit of force?",
        "options": [
            "A. Joule",
            "B. Watt",
            "C. Newton",
            "D. Pascal",
        ],
        "answer": "C",
        "explanation": "Force is measured in newtons (N)."
    },
    {
        "question": "Which simple machine is commonly used to lift a load with a wheel and rope?",
        "options": [
            "A. Pulley",
            "B. Thermocouple",
            "C. Diode",
            "D. Capacitor",
        ],
        "answer": "A",
        "explanation": "A pulley uses a grooved wheel and rope or cable to help move a load."
    },
    {
        "question": "What is the function of a resistor in an electrical circuit?",
        "options": [
            "A. To generate magnetic fields only",
            "B. To oppose the flow of electric current",
            "C. To measure temperature",
            "D. To convert AC into DC",
        ],
        "answer": "B",
        "explanation": "A resistor provides resistance and helps control current and voltage."
    },
    {
        "question": "Which electronic component allows current to flow mainly in one direction?",
        "options": [
            "A. Diode",
            "B. Transformer",
            "C. Relay coil",
            "D. Inductor",
        ],
        "answer": "A",
        "explanation": "A diode is designed to conduct mainly in one direction."
    },
    {
        "question": "What does LED mean?",
        "options": [
            "A. Low Energy Device",
            "B. Light Emitting Diode",
            "C. Linear Electrical Display",
            "D. Light Energy Detector",
        ],
        "answer": "B",
        "explanation": "LED stands for Light Emitting Diode."
    },
    {
        "question": "Which control system uses feedback to compare actual output with a desired value?",
        "options": [
            "A. Open-loop system",
            "B. Closed-loop system",
            "C. Manual system only",
            "D. Mechanical linkage only",
        ],
        "answer": "B",
        "explanation": "A closed-loop system uses feedback to reduce the difference between desired and actual output."
    },
    {
        "question": "What is the purpose of feedback in a control system?",
        "options": [
            "A. To eliminate every component",
            "B. To provide information about the system output",
            "C. To stop all movement",
            "D. To increase supply voltage automatically",
        ],
        "answer": "B",
        "explanation": "Feedback returns output information to the controller for comparison and correction."
    },
    {
        "question": "Which device is commonly used to measure temperature?",
        "options": [
            "A. Thermistor",
            "B. Gear",
            "C. Pulley",
            "D. Fuse",
        ],
        "answer": "A",
        "explanation": "A thermistor changes its resistance as temperature changes."
    },
    {
        "question": "What is the main purpose of a relay?",
        "options": [
            "A. To act as an electrically operated switch",
            "B. To store computer files",
            "C. To measure fluid pressure only",
            "D. To reduce the weight of a shaft",
        ],
        "answer": "A",
        "explanation": "A relay uses an electrical signal to open or close contacts in another circuit."
    },
    {
        "question": "Which of these is an example of a robotic application?",
        "options": [
            "A. Automated welding in a factory",
            "B. A handwritten notebook",
            "C. A wooden ruler",
            "D. A manual paper file",
        ],
        "answer": "A",
        "explanation": "Industrial robots are commonly used for tasks such as welding, painting and assembly."
    },
    {
        "question": "What does CAD stand for in engineering?",
        "options": [
            "A. Computer-Aided Design",
            "B. Control Automation Device",
            "C. Current Analysis Diagram",
            "D. Computer Applied Data",
        ],
        "answer": "A",
        "explanation": "CAD means Computer-Aided Design and is used to create engineering drawings and models."
    },
    {
        "question": "Which instrument is used to measure electric current?",
        "options": [
            "A. Voltmeter",
            "B. Ammeter",
            "C. Barometer",
            "D. Speedometer",
        ],
        "answer": "B",
        "explanation": "An ammeter measures electric current, usually in amperes."
    },
]


def show_header():
    print("=" * 62)
    print("                 MECHATRONICS BRAINBOX")
    print("              THE 20-QUESTION CHALLENGE")
    print("=" * 62)
    print(f"Student: {STUDENT_NAME}")
    print("Course: CTE213")
    print("Instructions: Choose A, B, C or D for each question.")
    print("Each correct answer earns 5 marks. Total: 100 marks.")
    print("=" * 62)


def ask_question(number, item):
    print(f"\nQUESTION {number}/20")
    print(item["question"])
    for option in item["options"]:
        print(option)

    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in ("A", "B", "C", "D"):
            return choice
        print("Invalid choice. Please enter A, B, C or D.")


def get_grade(score):
    if score >= 80:
        return "A - Excellent"
    if score >= 70:
        return "B - Very Good"
    if score >= 60:
        return "C - Good"
    if score >= 50:
        return "D - Pass"
    return "F - Needs Improvement"


def run_quiz():
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0
    correct_count = 0
    wrong_answers = []

    show_header()
    input("\nPress ENTER when you are ready to begin...")

    for number, item in enumerate(questions, start=1):
        choice = ask_question(number, item)
        if choice == item["answer"]:
            print("Correct! +5 marks")
            score += 5
            correct_count += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}")
            wrong_answers.append((item["question"], choice, item["answer"]))
        print("Explanation:", item["explanation"])

    print("\n" + "=" * 62)
    print("                    QUIZ RESULTS")
    print("=" * 62)
    print(f"Student: {STUDENT_NAME}")
    print(f"Correct answers: {correct_count}/20")
    print(f"Wrong answers:   {20 - correct_count}/20")
    print(f"Final score:     {score}/100")
    print(f"Grade:           {get_grade(score)}")
    print("=" * 62)

    if wrong_answers:
        print("\nREVISION SUMMARY")
        for question, selected, correct in wrong_answers:
            print(f"\n{question}")
            print(f"Your answer: {selected} | Correct answer: {correct}")
    else:
        print("\nPerfect score! You answered every question correctly.")

    print("\nThank you for using MECHATRONICS BRAINBOX!")


def main():
    while True:
        run_quiz()
        again = input("\nWould you like to take the quiz again? (Y/N): ").strip().upper()
        if again != "Y":
            print("\nGoodbye, and keep learning!")
            break


if __name__ == "__main__":
    main()
