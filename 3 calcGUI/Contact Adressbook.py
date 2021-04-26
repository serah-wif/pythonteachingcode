from tkinter import *
import datetime

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self, master):
        self.master = master

        #frames
        #
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        #top frame design
        # self.top_image = PhotoImage(file='Icons/book.png')
        # self.top_image_label = Label(self.top, image=self.top_image)
        # self.top_image_label.place(x=120, y=10)

        self.heading = Label(self.top, text='My Phonebook App', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Today's date: " +date, font='arial 12 bold', bg='white', fg='#ebb434')
        self.date_lbl.place(x=450, y=110)

class HomePage(Application):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)





        # # # Creates the Full Name Entry Box
        self.name = Label(self, text='Full Name:')
        self.name.pack(pady=2, padx=10)
        self.name_box = Entry(self)
        self.name_box.pack()
        self.name_box.focus_set()

                #
        # # Creates the Email Entry Box
        email = Label(self, text='Email:')
        email.pack(pady=2, padx=10)
        email_box = tk.Entry(self)
        email_box.pack()
        #
        # # Creates the Phone Number Entry Box
        phone = Label(self, text='Phone Number:')
        phone.pack(pady=2, padx=10)
        phone_box = tk.Entry(self)
        phone_box.pack()

def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__=='__main__':
     main()