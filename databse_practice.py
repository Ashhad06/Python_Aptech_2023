from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as Mysql

A=Tk()
A.title("Database practice")
A.minsize(width=600,height=500)
A.maxsize(width=600,height=500)
Id= Label(A,text="Enter your Id :",font="Verdana 15")
Id.place(x=2,y=20)
id_entry= Entry(A,bd=3,width=30)
id_entry.place(x=160,y=27)

Name= Label(A,text="Enter your Name :",font="Verdana 15")
Name.place(x=2,y=63)
name_entry= Entry(A,bd=3,width=30)
name_entry.place(x=200,y=70)

Phone= Label(A,text="Enter your Phone number :",font="Verdana 15")
Phone.place(x=2,y=108)
phone_entry= Entry(A,bd=3,width=30)
phone_entry.place(x=290,y=115)

def Insert():
    student_id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if (student_id == "" or name == "" or phone == ""):
        Messagebox.showinfo("Alert", "Please enter all the fields")
    else:
        con = Mysql.connect(host="localhost", user="root", database="abcd")
        cursor = con.cursor()
        cursor.execute("insert into student values('" + student_id + "','" + name + "','" + phone + "')")
        cursor.execute("commit")
        Messagebox.showinfo("Status", "Successfully inserted")
        con.close()

def Update():
    student_id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    if(student_id=="" or name=="" or phone==""):
        Messagebox.showinfo("Alert","Please enter which id you want to update")
    else:
        con= Mysql.connect(host="localhost",user="root",database="abcd")
        cursor= con.cursor()
        cursor.execute("update student set name='"+name+"',phone='"+phone+"'where id='"+ student_id +"'")
        cursor.execute("commit");
        Messagebox.showinfo("Status","successfully updated")
        con.close();
    
def Clear():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)

def Select():
    if(id_entry.get()==""):
        Messagebox.showinfo("Alert","Enter which id data you want")
    else:
        con= Mysql.connect(host="localhost",user="root",database="abcd")
        cursor=con.cursor()
        cursor.execute("select * from student where id = '"+id_entry.get()+"'")
        Rows=cursor.fetchall()
        for row in Rows:
            name_entry.insert(0,row[1])
            phone_entry.insert(0,row[2])
            con.close();
        
def Delete():
    if(id_entry.get()==""):
        Messagebox.showinfo("Alert","Please enter any id to delete")
    else:
        con= Mysql.connect(host="localhost",user="root",database="abcd")
        cursor=con.cursor()
        cursor.execute("delete from student where id='"+id_entry.get()+"'")
        cursor.execute("commit");
        
        id_entry.delete(0,"end")
        name_entry.delete(0,"end")
        phone_entry.delete(0,"end")
        Messagebox.showinfo("Status","Successfully deleted")
        con.close();
        
        
        
        
Inert_button= Button(A,text="Insert",font="verdana 15",command=Insert).place(x=150,y=160)
Update_button= Button(A,text="Update",font="verdana 15",command=Update).place(x=250,y=160)
Clear_button= Button(A,text="Clear",font="verdana 15",command=Clear).place(x=200,y=215)
Select_button= Button(A,text="Select",font="verdana 15", command=Select).place(x=340,y=260)
Delete_button= Button(A,text="Delete",font="verdana 15", command=Delete).place(x=300,y=225)



A.mainloop()