from tkinter import *
A= Tk()
A.title("Ashhad")
A.iconbitmap("Ash.ico")
A.maxsize(width=600,height=300)
A.minsize(width=600,height=300)
B=Label(A,text="Enter_your_name :",fg="white",bg="black")
B.place(x=0.3,y=5)
C=Entry(A,bd=5)
C.place(x="110",y="2.5",)
def Func():
    D= Label(text=C.get(),fg="red",font="Roquen")
    D.place(x=103,y=30,)


btn=Button(A,text="Submit",command=Func,bg="green")
btn.place(x=1,y=30)
A.mainloop()