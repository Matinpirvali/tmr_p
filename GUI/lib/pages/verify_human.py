import random
import tkinter as tk

class VerifyHumanGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Verify Human")
        
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack()

        self.verify_button = tk.Button(self.window, text="Verify", command=self.verify_human)
        self.verify_button.pack()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}? "
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return question, answer

    def verify_human(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.answer:
                result_message = "Verification successful. You are human!"
            else:
                result_message = "Incorrect answer. Please try again."
        except ValueError:
            result_message = "Invalid input. Please enter a valid integer."
        
        self.result_label = tk.Label(self.window, text=result_message)
        self.result_label.pack()

    def start(self):
        self.question, self.answer = self.generate_question()
        self.question_label.config(text=self.question)
        self.window.mainloop()

# Create an instance of the VerifyHumanGUI class and start the GUI
verify_human_gui = VerifyHumanGUI()
verify_human_gui.start()
