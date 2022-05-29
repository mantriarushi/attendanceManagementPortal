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
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Train Dataset",font=("MAJUSCULES",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"./assets/blue.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=325)

        #button
        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier, font=("MAJUSCULES",18),bg="black",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"./assets/blue.png")
        img_bottom=img_bottom.resize((1530,345),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=370)

    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml") 
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")       


if __name__=="__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop() 