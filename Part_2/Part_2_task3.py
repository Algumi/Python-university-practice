from tkinter import *
from random import shuffle


class Application:
    window = Tk()
    refresh_btn = Button()
    next_btn = Button()
    question_lbl = Label()

    q_text1, q_text2, q_text3 = "lol that should be a question", "sas", "lul"
    questions = []

    def start_app(self):
        self.window.title('Test')
        self.window.geometry('600x350')
        self.generate_questions()
        self.main_page()

    def main_page(self):
        self.refresh_btn = Button(self.window, text='restart', width=10, height=1, command=self.refresh_click)
        self.refresh_btn.place(x=5, y=5)
        self.next_btn = Button(self.window, text='next', width=10, height=1, command=self.next_question)
        self.next_btn.place(x=250, y=250)

        self.question_lbl = Label(self.window)
        self.question_lbl.place(x=200, y=100)
        self.locate_question_type1()
        print(self.questions)

        self.window.mainloop()

    def locate_question_type1(self):
        self.question_lbl.configure(text=self.q_text1)

    def locate_question_type2(self):
        self.question_lbl.configure(text=self.q_text2)

    def locate_question_type3(self):
        self.question_lbl.configure(text=self.q_text3)

    def next_question(self):
        self.locate_question_type2()

    def refresh_click(self):
            self.start_app()

    def generate_questions(self):
        self.questions = []
        f = open("../test_data/questions.txt")
        for line in f:
            print("русский текст")
            raw_data = line.split(" || ")
            self.questions.append((raw_data[0], raw_data[1], 0))
        shuffle(self.questions)


def test():
    test_app = Application()
    test_app.start_app()


test()
