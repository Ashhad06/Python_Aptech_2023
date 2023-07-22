from tkinter import *
A= Tk()
def Click():
    B=Label (A, text=input.get())
    B.pack()
input=Entry(A,text="name")
input.pack()
Submit = Button(A, text="Submit", command = Click)
Submit.pack()
A.mainloop()