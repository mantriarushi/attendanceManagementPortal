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


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Help Desk",font=("MAJUSCULES",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"./assets/blue.png")
        img_top=img_top.resize((1530,900),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=900)
        
        img_top = Image.open(r"./assets/blue.png")
        img_top=img_top.resize((1530,900),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=900)
        
        dev_lbl = Label(f_lbl,text="You can reach me by: ",font=("MAJUSCULES",13),bg="black",fg="white")
        dev_lbl.place(x=600,y=350)
        
        dev1_lbl = Label(f_lbl,text="Contact Number: 9119552733",font=("MAJUSCULES",13),bg="black",fg="white")
        dev1_lbl.place(x=600,y=380)
        
        dev_lbl = Label(f_lbl,text="Email: arushi.mantri@cumminscollege.in",font=("MAJUSCULES",13),bg="black",fg="white")
        dev_lbl.place(x=600,y=410)
        
        
if __name__=="__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop() 