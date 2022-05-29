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


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        ######## variables #########
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_student_id=StringVar()
        self.var_Name=StringVar()
        self.var_Division=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_Dob=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()


        #bg image
        img3 = Image.open(r"./assets/blue.png")
        img3=img3.resize((1530,770),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=800)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="Student Management System",font=("MAJUSCULES",35),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("MAJUSCULES",12,"bold"),bg="white")
        left_frame.place(x=70,y=130,width=680,height=600)

        #image
        img_left = Image.open(r"./assets/blue.png")
        img_left=img_left.resize((672,135),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=75,y=153,width=675,height=100)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("MAJUSCULES",12,"bold"),bg="white")
        current_course_frame.place(x=3,y=95,width=670,height=150)

        #Department
        dept_label=Label(current_course_frame,text="Department",font=("MAJUSCULES",13),bg="white")
        dept_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("MAJUSCULES",11),state="readonly",width=20)
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("MAJUSCULES",13),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("MAJUSCULES",11),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("MAJUSCULES",13),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("MAJUSCULES",11),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("MAJUSCULES",13),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("MAJUSCULES",11),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("MAJUSCULES",12,"bold"),bg="white")
        class_student_frame.place(x=3,y=250,width=670,height=320)

        #student id
        stud_id_label=Label(class_student_frame,text="ID:",font=("MAJUSCULES",13),bg="white")
        stud_id_label.grid(row=0,column=0,padx=10,sticky=W)

        stud_id_entery=ttk.Entry(class_student_frame,textvariable=self.var_student_id,width=20,font=("MAJUSCULES",10))
        stud_id_entery.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        stud_name_label=Label(class_student_frame,text="Name:",font=("MAJUSCULES",13),bg="white")
        stud_name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        stud_name_entery=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("MAJUSCULES",10))
        stud_name_entery.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Division:",font=("MAJUSCULES",13),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Division,font=("MAJUSCULES",11),state="readonly",width=15)
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        class_rollno_label=Label(class_student_frame,text="Roll No:",font=("MAJUSCULES",13),bg="white")
        class_rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        class_rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_Roll,width=20,font=("MAJUSCULES",10))
        class_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        class_gender_label=Label(class_student_frame,text="Gender:",font=("MAJUSCULES",13),bg="white")
        class_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("MAJUSCULES",11),state="readonly",width=15)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        class_dob_label=Label(class_student_frame,text="Date Of Birth:",font=("MAJUSCULES",13),bg="white")
        class_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        class_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_Dob,width=20,font=("MAJUSCULES",10))
        class_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        class_email_label=Label(class_student_frame,text="Email:",font=("MAJUSCULES",13),bg="white")
        class_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        class_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("MAJUSCULES",10))
        class_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        class_contactno_label=Label(class_student_frame,text="Contact No:",font=("MAJUSCULES",13),bg="white")
        class_contactno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        class_contactno_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone,width=20,font=("MAJUSCULES",10))
        class_contactno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        class_address_label=Label(class_student_frame,text="Address",font=("MAJUSCULES",13),bg="white")
        class_address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        class_address_entry=ttk.Entry(class_student_frame,textvariable=self.var_Address,width=20,font=("MAJUSCULES",10))
        class_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        class_tname_label=Label(class_student_frame,text="Teacher Name:",font=("MAJUSCULES",13),bg="white")
        class_tname_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        class_tname_entry=ttk.Entry(class_student_frame,textvariable=self.var_Teacher,width=20,font=("MAJUSCULES",10))
        class_tname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radbtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No Photo Sample",value="No")
        radbtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=665,height=40)

        save_button=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("MAJUSCULES",13),bg="blue",fg="white")
        save_button.grid(row=0,column=0,padx=4)

        update_button=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("MAJUSCULES",13),bg="blue",fg="white")
        update_button.grid(row=0,column=1,padx=4)

        del_button=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("MAJUSCULES",13),bg="blue",fg="white")
        del_button.grid(row=0,column=2,padx=4)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("MAJUSCULES",13),bg="blue",fg="white")
        reset_button.grid(row=0,column=3,padx=4)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=248,width=664,height=38)

        take_photo_button=Button(btn_frame1,text="Capture Photo",command=self.generate_dataset,width=34,font=("MAJUSCULES",13),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0,padx=4)

        update_photo_button=Button(btn_frame1,text="Update Photo",width=35,font=("MAJUSCULES",13),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=1,padx=4)
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("MAJUSCULES",13,"bold"),bg="white")
        right_frame.place(x=800,y=130,width=660,height=600)

        img_right = Image.open(r"./assets/blue.png")
        img_right=img_right.resize((655,135),Image.ANTIALIAS)
        self.photoimg00 = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg00)
        f_lbl.place(x=0,y=0,width=659,height=100)

        ######### Searching System ###########
        #search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("MAJUSCULES",12,"bold"),bg="white")
        #search_frame.place(x=3,y=95,width=650,height=70)

        #search_label=Label(search_frame,text="Search By:",font=("MAJUSCULES",13),bg="pink",fg="black")
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search_combo=ttk.Combobox(search_frame,font=("MAJUSCULES",11),state="readonly",width=15)
        #search_combo["values"]=("Select","Roll No","Contact Number")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search_entry=ttk.Entry(search_frame,width=15,font=("MAJUSCULES",13))
        #search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #search_button=Button(search_frame,text="Search",width=10,font=("MAJUSCULES",11),bg="blue",fg="white")
        #search_button.grid(row=0,column=3,padx=4)

        ##showall_button=Button(search_frame,text="Show All",width=10,font=("MAJUSCULES",11),bg="blue",fg="white")
        #showall_button.grid(row=0,column=4,padx=4)

        ############ Table Frame ###############
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=105,width=650,height=470)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","semester","student_id","Name","Division","Roll","Gender","Dob","Email","Phone","Address","Teacher","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("student_id",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Email",text="Email")  
        self.student_table.heading("Phone",text="Contact No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=70)
        self.student_table.column("semester",width=100)
        self.student_table.column("student_id",width=80)
        self.student_table.column("Name",width=150)
        self.student_table.column("Division",width=50)
        self.student_table.column("Roll",width=70)
        self.student_table.column("Gender",width=70)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Email",width=170)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("PhotoSample",width=50)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ########### Function Declaration ########## 
       
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="arushi@123",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              
                                                                                                                self.var_dept.get(), 
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_student_id.get(),
                                                                                                                self.var_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_Dob.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio1.get()

                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except  Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #---------fetch data---------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="arushi@123",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=i)
            conn.commit()
        conn.close() 

    ########### get function #########
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        print("here", data);

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Division.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Dob.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="arushi@123",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                self.var_dept.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_Dob.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_student_id.get()
                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details are successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #### Delete Function #######

    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student ID is Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to remove this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="arushi@123",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted student details",parent=self.root)   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    ######### Reset ##########
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_student_id.set("")
        self.var_Name.set("")
        self.var_Division.set("Select Division")
        self.var_Roll.set("")
        self.var_Gender.set("Male")
        self.var_Dob.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio1.set("") 


    ######### Generate Dataset and Take Photo Samples ###########

    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="arushi@123",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(    
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_Name.get(),
                                                                                                                self.var_Division.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_Dob.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_student_id.get()==id+1
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                ########## load predefined data on face frontals from  opencv ##########

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
 



if __name__=="__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()         
