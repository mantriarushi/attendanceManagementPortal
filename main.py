from cgitb import text
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import tkinter
from setuptools import Command
from student import Student
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #bg image
        img3 = Image.open(r"./assets/blue.png")
        img3=img3.resize((1530,900),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=870)

        title_lbl=Label(text="Face Recognition Attendance System",font=("MAJUSCULES",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl=Label(title_lbl,font=("MAJUSCULES",15,"bold"),bg="black",fg="white")
        lbl.place(x=0,y=0,width=110,height=50)
        time()    

        #student button
        img4 = Image.open(r"./assets/student2.png")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=250,width=150,height=20)

        #Detect face button
        img5=Image.open(r"./assets/face3.png")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=150,height=150)

        b1_1=Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=250,width=150,height=20)

        #Attendance
        img6=Image.open(r"./assets/book1.png")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=250,width=150,height=20)

        #Help Desk Button
        img7=Image.open(r"./assets/help.png")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=250,width=150,height=20)

        #Train Data Button
        img8=Image.open(r"./assets/traindata.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=150,height=150)

        b1_1=Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=550,width=150,height=20)

        #Photos Button
        img9=Image.open(r"./assets/camera.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=150,height=150)

        b1_1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=550,width=150,height=20)

        #Developer Button
        img10=Image.open(r"./assets/developer.png")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=150,height=150)

        b1_1=Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=550,width=150,height=20)

        #Exit Button
        img11=Image.open(r"./assets/exit.png")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=150,height=150)

        b1_1=Button(bg_img,text="Exit", cursor="hand2",command=self.iExit,font=("MAJUSCULES",13,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=550,width=150,height=20)

    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Do you want to exit this project?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return   
            
        ########## Function Buttons ##############
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)          


if __name__=="__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()           