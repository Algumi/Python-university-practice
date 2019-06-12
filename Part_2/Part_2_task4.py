from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np


class Application(Frame):
    img = None
    func = None
    var = None
    win = None

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pack()

        m = Menu(root, tearoff=0)
        root.config(menu=m)

        fm = Menu(m, tearoff=0)
        m.add_cascade(label="File", menu=fm)
        fm.add_command(label="Открыть...", command=self.show)
        fm.add_command(label="Построить график", command=self.plot)
        fm.add_command(label="Выход", command=self.close_win)

        m.add_command(label="Справка", command=self.about)

        self.canv = Canvas(root, width=800, height=600)
        self.imgobj = self.canv.create_image(0, 0)

        self.scroll_x = Scrollbar(root, orient="horizontal", command=self.canv.xview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(root, orient="vertical", command=self.canv.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.canv.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        self.canv.pack()

    def show(self):
        try:
            self.canvas.get_tk_widget().destroy()
        except:
            pass

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.canv.pack()

        filename = askopenfilename()
        if filename:
            src_img = Image.open(filename)
            self.img = ImageTk.PhotoImage(src_img)
            self.canv.itemconfigure(self.imgobj, image=self.img, anchor="nw")
            self.canv.configure(scrollregion=self.canv.bbox("all"))

    def close_win(self):
        root.destroy()

    def about(self):
        win = Toplevel(root)
        win.geometry("400x400")
        lab = Label(win, text="Пррограмма с использованием Tkinter")
        lab.pack()

    def sel(self):
        self.func = self.fs[self.var.get() - 1]

    def wrong_input(self):
        win = Toplevel(root)
        win.geometry("400x400")
        lab = Label(win, text="Wrong input!", bg="red")
        lab.pack()

    def plot(self):
        try:
            self.win.destroy()
        except:
            pass

        self.win = Toplevel(root, width=400, height=400)
        self.win.geometry("400x400")

        self.var = IntVar()
        self.fs = [np.sin, np.cos, np.tan, lambda x: 1.0 / np.tan(x), lambda x: x * x, lambda x: x * x * x]

        sinx = Radiobutton(self.win, text="sin x", variable=self.var, value=1, command=self.sel)
        cosx = Radiobutton(self.win, text="cos x", variable=self.var, value=2, command=self.sel)
        tgx = Radiobutton(self.win, text="tg x", variable=self.var, value=3, command=self.sel)
        ctgx = Radiobutton(self.win, text="ctg x", variable=self.var, value=4, command=self.sel)
        x2 = Radiobutton(self.win, text="x^2", variable=self.var, value=5, command=self.sel)
        x3 = Radiobutton(self.win, text="x^3", variable=self.var, value=6, command=self.sel)

        sinx.pack(anchor=W)
        cosx.pack(anchor=W)
        tgx.pack(anchor=W)
        ctgx.pack(anchor=W)
        x2.pack(anchor=W)
        x3.pack(anchor=W)

        sinx.select()

        l1 = Label(self.win, text="Minimal x")
        l2 = Label(self.win, text="Maximal x")
        e1 = Entry(self.win)
        e2 = Entry(self.win)

        l1.pack(anchor=W)
        e1.pack(anchor=W)
        l2.pack(anchor=W)
        e2.pack(anchor=W)

        btn = Button(self.win, text="Draw", command=lambda: self.draw_plot(e1, e2))
        btn.pack(anchor=W)

    def draw_plot(self, e1, e2):
        ylims = (-10, 10)

        def upd(xs, ys):
            if self.var.get() - 1 != 2 and self.var.get() - 1 != 3:
                return
            for i in range(len(xs)):
                if ys[i] <= ylims[0] or ys[i] >= ylims[1]:
                    ys[i] = np.nan
                    xs[i] = np.nan

        x1 = 0
        x2 = 0
        try:
            x1 = int(e1.get())
            x2 = int(e2.get())
            assert (x1 < x2)
        except:
            self.wrong_input()
        else:
            try:
                self.canvas.get_tk_widget().destroy()
            except:
                pass

            self.canv.pack_forget()
            self.scroll_y.pack_forget()
            self.scroll_x.pack_forget()

            fig = Figure(figsize=(5, 4), dpi=100)
            xs = np.arange(x1, x2, (x2 - x1) / 5000)
            ys = self.func(xs)
            upd(xs, ys)

            fig.add_subplot(111).plot(xs, ys)
            self.canvas = FigureCanvasTkAgg(fig, master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


root = Tk()
root.title("Part 2 - task 4")
root.geometry("600x400")
app = Application(root)
root.mainloop()
