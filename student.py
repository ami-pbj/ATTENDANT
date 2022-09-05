from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
# import opencv => having machine learning algorithm
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Attendance System")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")


        # <<<<<<<<<<==========VARIABLES==========>>>>>>>>>>
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()






        # to add image in home
        img=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student home.jpg")
        img=img.resize((1400,850),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=850)


        # page title on background image
        title_lbl=Label(bg_img,text="Student Details",font=("Times",30,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=-2,y=-2,width=1400,height=60)

        # time showing
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        lbl.place(x=1290,y=10,width=100,height=40)
        time()


        # <<<<<<<<<<==========MAIN LABEL FRAME==========>>>>>>>>>>
        # making frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=3,y=63,width=1387,height=536)

        
        # <<<<<<<<<<==========LEFT LABEL FRAME==========>>>>>>>>>>
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=15,width=550,height=500)


        # add image on left frame
        img_left=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student bg.jpg")
        img_left=img_left.resize((550,70),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=543,height=70)



        # <<<<<<<<<<==========CURRENT COURSE INFORMATION==========>>>>>>>>>>
        # current course frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=4,y=70,width=533,height=110)

        # department combobox
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","UIC","UIE","USB","HM","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course combobox
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","MCA","MBA","MTECH","ME","BSC","CSE","MCE","CIVIL","IT","ECE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year combobox
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # semester combobox
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        
        # class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=4,y=190,width=533,height=280)

        # label and entry field create
        # student id label
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        # student id entry field
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        # student name label
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)

        # student name entry field
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        # class division label
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=2,column=0,padx=2,pady=2,sticky=W)

        # class division entry field
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        # division combobox
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        # roll no label
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        # roll no entry field
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        # gender label
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=2,pady=2,sticky=W)

        # gender entry field
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        # gender combobox
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)


        # date of birth label
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2,pady=2,sticky=W)

        # date of birth entry field
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=2,sticky=W)

        # email label
        email_label=Label(class_student_frame,text="Email ID:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,pady=2,sticky=W)

        # email entry field
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=2,sticky=W)

        # phone no label
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=2,pady=2,sticky=W)

        # phone no field
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=2,sticky=W)

        # address label
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,pady=2,sticky=W)

        # address entry field
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=2,sticky=W)

        # teacher name label
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2,pady=2,sticky=W)

        # teacher name entry field
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=2,sticky=W)


        # radio button create
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=1,padx=2,pady=2)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=2,padx=2,pady=2)


        # first row buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=528,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="black")
        delete_btn.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="black")
        reset_btn.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        
        # second row button frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=220,width=528,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",12,"bold"),bg="blue",fg="black")
        take_photo_btn.grid(row=0,column=0,padx=20,pady=2)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",12,"bold"),bg="blue",fg="black")
        update_photo_btn.grid(row=0,column=1,padx=20,pady=2)




        # <<<<<<<<<<==========RIGHT LABEL FRAME==========>>>>>>>>>>
        # right label frame
        Right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        Right_frame.place(x=580,y=15,width=785,height=500)

        # add image on right frame
        img_right=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student bg.jpg")
        img_tight=img_right.resize((778,70),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        # frame image position
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=778,height=70)


        # <<<<<<<<<<==========SEARCH SYSTEM==========>>>>>>>>>>
        
        # label frame create
        # search system label frame create
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=4,y=70,width=769,height=60)

        # search label
        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=3,pady=2,sticky=W)

        # search combobox
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=25)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        # search entry field
        search_entry=ttk.Entry(search_frame,width=35,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=2,sticky=W)


        # create search button
        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        search_btn.grid(row=0,column=3,padx=5,pady=2,sticky=W)

        # create show all button 
        showAll_btn=Button(search_frame,text="Show All",width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        showAll_btn.grid(row=0,column=4,padx=4,pady=2,sticky=W)


        # table frame create
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=4,y=140,width=769,height=330)

        # create scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        # student table create
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # creating header
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    # <<<<<<<<<<==========FUNCTION DECLARATION==========>>>>>>>>>>
    # add data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required !!",parent=self.root)
        else:
            try:
                # messagebox.showinfo("Success","Data Added Successfully !!")
                # mysql database connection create
                conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Data Added Successfully !!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    # <<<<<<<<<<==========FETCH DATA==========>>>>>>>>>>
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
        my_cursor=conn.cursor()

        # query execute to fetch data
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # <<<<<<<<<<==========GET CURSOR==========>>>>>>>>>>
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required !!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want to Update This Student Data !!",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Email_ID=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Data Updated Successfully !!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID Must Be Required !!",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete Student Data","Do You Wnat to Delete Student Data ??",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Data Deleted Successfully !!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # restet function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    # <<<<<<<<<<==========GENERATE DATA SET OR TAKE PHOTO SAMPLES==========>>>>>>>>>>
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required !!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,DOB=%s,Email_ID=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # <<<<<<<<<<==========FACE DETECTION USING HAAR CASCADES==========>>>>>>>>>>
                # LOAD PREDIFINED DATA ON FACE FRONTALS FROM OPENCV
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # faces=face_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,maxSize=(500,500))
                    # scaling factor=1.3
                    # Minimum Neighbor=5
                    # minSize = (30,30)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(550,550))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed !!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



        





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

