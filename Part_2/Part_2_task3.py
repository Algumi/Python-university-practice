from tkinter import *
from random import shuffle


class Application:
    window = Tk()
    refresh_btn = Button()
    next_btn = Button()
    question_lbl = Label()
    answer_input = []

    questions = []
    current_question = 0

    def start_app(self):
        self.window.title('Test')
        self.window.geometry('600x350')
        self.current_question = 0
        self.generate_questions()
        self.main_page()

    def main_page(self):
        self.question_lbl = Label(self.window, width=100, height=10)
        self.question_lbl.pack(side=TOP)
        self.next_question(True)
        print(self.questions)

        self.window.mainloop()

    def locate_question_type1(self, q_data):
        print("\ni m working")
        self.question_lbl.pack(side=TOP)
        self.question_lbl.configure(text=q_data[2])
        self.answer_input = [Entry(self.window, width=50)]
        self.answer_input[0].pack(side=TOP)

    def locate_question_type2(self, q_data):
        self.question_lbl.pack(side=TOP)
        self.question_lbl.configure(text=q_data[2])
        radio_var = IntVar()
        for i, ans in enumerate(q_data[3]):
            radio_btn = Radiobutton(self.window, text=ans, variable=radio_var, value=i)
            radio_btn.pack(side=TOP)
            self.answer_input.append(radio_btn)

    def locate_question_type3(self, q_data):
        self.question_lbl.pack(side=TOP)
        self.question_lbl.configure(text=q_data[2])
        self.window.update()

    def next_question(self, num=None):
        print(num, self.current_question, self.questions)
        if not num:
            q_id = self.current_question
            cur_q = self.questions[q_id]
            if cur_q[0] == 1:
                # print(cur_q[3] + "---" + str(self.answer_input[0].text) + "---")
                if self.answer_input[0] == cur_q[3]:
                    self.questions[q_id][1] = 1
                else:
                    self.questions[q_id][1] = 2
            self.current_question += 1
        if self.current_question < len(self.questions):
            self.destroy_located()
            self.locate_buttons()
            next_q = self.questions[self.current_question]
            if next_q[0] == 1:
                self.locate_question_type1(next_q)
            if next_q[0] == 2:
                self.locate_question_type2(next_q)
            if next_q[0] == 3:
                self.locate_question_type3(next_q)

    def locate_buttons(self):
        self.refresh_btn = Button(self.window, text='restart', width=10, height=1, command=self.refresh_click)
        self.refresh_btn.pack(side=BOTTOM, pady=10)
        self.next_btn = Button(self.window, text='next', width=10, height=1, command=self.next_question)
        self.next_btn.pack(side=BOTTOM, pady=10)

    def destroy_located(self):
        if len(self.answer_input) > 0:
            for w in self.answer_input:
                w.destroy()
            self.answer_input = []
            self.question_lbl.pack_forget()
            self.next_btn.destroy()
            self.refresh_btn.destroy()

    def refresh_click(self):
        self.destroy_located()
        self.start_app()

    def generate_questions(self):
        self.questions = []
        f = open("../test_data/questions.txt", encoding="UTF-8")
        for line in f:
            raw_data = line.split(" || ")
            if raw_data[-1][-1] == "\n":
                raw_data[-1] = raw_data[-1][:-1]
            if raw_data[0] == '1':
                self.questions.append([1, 0, raw_data[1], raw_data[2]])
            elif raw_data[0] == '2':
                self.questions.append([2, 0, raw_data[1], raw_data[2].split(" | "), raw_data[3]])
            elif raw_data[0] == '3':
                self.questions.append([2, 0, raw_data[1], raw_data[2].split(" | "), raw_data[3].split(" | ")])
        shuffle(self.questions)


def test():
    test_app = Application()
    test_app.start_app()


test()
