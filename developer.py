from cgitb import grey
from distutils.util import execute
from logging import root
from tkinter import*
from tkinter import ttk
from tokenize import String
from turtle import update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("MAJUSCULES",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"./assets/blue.png")
        img_top=img_top.resize((1530,900),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=900)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=500,y=0,width=500,height=680)
        
        img_res = Image.open(r"./assets/Resume.jpeg")
        img_res=img_res.resize((530,900),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_res)

        f_lbl = Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=0,y=26,width=500,height=900)

       

        


if __name__=="__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()         