from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
score = 0

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Billie's Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(bg=THEME_COLOR, text="Score: 0", fg="white")
        self.score_text.grid(column=1, row=0,)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="{placeholder}", fill="black",
                                                 font=("Arial", 20, "italic"))
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  padx=20, pady=20, command=self.true_selected)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   padx=20, pady=20, command=self.false_selected)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            quest_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quest_text)
        else:
            final_score = self.quiz.score
            if final_score >= 8:
                pass_fail = f"Congratulations! You've passed, your final score is {final_score}."
            else:
                pass_fail = (f"Sorry! Your final score is {final_score}. "
                             f"You didn't pass the quiz, but keep practicing!")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz!\n {pass_fail}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_selected(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_selected(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
        self.window.after(1000, self.get_next_question)

