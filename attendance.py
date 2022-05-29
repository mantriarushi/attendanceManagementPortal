from cgitb import grey
from distutils.util import execute
from logging import root
import string
from tkinter import*
from tkinter import ttk
from tokenize import String
from turtle import update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #bgimage
        img3 = Image.open(r"./assets/blue.png")
        img3=img3.resize((1530,800),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="Attendance",font=("MAJUSCULES",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=30,y=80,width=1470,height=650)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("MAJUSCULES",12,"bold"),bg="white")
        left_frame.place(x=40,y=40,width=680,height=575)

        linside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        linside_frame.place(x=10,y=140,width=658,height=400)

        ####### Labels and entry ##########

        #Attendance ID
        attendance_id_label=Label(linside_frame,text="Attendance ID:",font=("MAJUSCULES",13),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_id_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_id,font=("MAJUSCULES",10))
        attendance_id_entery.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label=Label(linside_frame,text="Roll No:",font=("MAJUSCULES",13),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        attendance_roll_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_roll,font=("MAJUSCULES",10))
        attendance_roll_entery.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        #Name
        name_label=Label(linside_frame,text="Name:",font=("MAJUSCULES",13),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        attendance_name_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_name,font=("MAJUSCULES",10))
        attendance_name_entery.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        #Department
        dep_label=Label(linside_frame,text="Department:",font=("MAJUSCULES",13),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        attendance_dep_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_dep,font=("MAJUSCULES",10))
        attendance_dep_entery.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        #Time
        time_label=Label(linside_frame,text="Time:",font=("MAJUSCULES",13),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        attendance_time_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_time,font=("MAJUSCULES",10))
        attendance_time_entery.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        #Date
        date_label=Label(linside_frame,text="Date:",font=("MAJUSCULES",13),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=8,sticky=W)

        attendance_date_entery=ttk.Entry(linside_frame,width=20,textvariable=self.var_atten_date,font=("MAJUSCULES",10))
        attendance_date_entery.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        #Attendance
        attendance_label=Label(linside_frame,text="Attendance Status:",font=("MAJUSCULES",13),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        self.atten_status=ttk.Combobox(linside_frame,font=("MAJUSCULES",11),state="readonly",width=15,textvariable=self.var_atten_attendance)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #button frame
        btn_frame=Frame(linside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=665,height=40)

        save_button=Button(btn_frame,text="Import csv",command=self.importCsv,width=23,font=("MAJUSCULES",13),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Export csv",command=self.exportCsv,width=23,font=("MAJUSCULES",13),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        #del_button=Button(btn_frame,text="Update",width=17,command=self.get_cursor,font=("MAJUSCULES",13),bg="blue",fg="white")
        #del_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",width=23,command=self.reset_data,font=("MAJUSCULES",13),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance",font=("MAJUSCULES",13,"bold"),bg="white")
        right_frame.place(x=750,y=40,width=680,height=575)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=5,width=658,height=540)

        #Scroll Bar Table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=130)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    ######### Fetch Data #########

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")                     
    
               

if __name__=="__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()         