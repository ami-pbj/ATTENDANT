from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
# import opencv => having machine learning algorithm
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Attendance Window")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")


        # text variable to update data 
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # to add image in home
        img=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/attendance.jpg")
        img=img.resize((1400,1250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=1250)


        # page title on background image
        title_lbl=Label(bg_img,text="Attendance Details",font=("Times",30,"bold"),bg="yellow",fg="green")
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
        main_frame.place(x=3,y=63,width=1387,height=462)


        # <<<<<<<<<<==========LEFT LABEL FRAME==========>>>>>>>>>>
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=15,width=550,height=426)


        # add image on left frame
        img_left=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student bg.jpg")
        img_left=img_left.resize((550,70),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=543,height=70)

        # student attendance details frame
        left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        left_inside_frame.place(x=4,y=80,width=533,height=310)


        # label and entry field
        # attendance id label
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        # attendance id entry field
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        # student name label
        studentName_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)

        # student name entry field
        studentName_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        # time label
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=2,pady=2,sticky=W)

        # time entry field
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        # roll no label
        roll_no_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        # roll no entry field
        roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        # department label
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=2,pady=2,sticky=W)

        # department entry field
        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        # date label
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=2,pady=2,sticky=W)

        # date entry field
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=2,sticky=W)

        # attendance status label
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=2,pady=2,sticky=W)

        # attendance status combobox
        self.atten_status=ttk.Combobox(left_inside_frame,width=19,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=2,sticky=W)


        # first row buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=528,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=15,font=("times new roman",12,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="black")
        delete_btn.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="black")
        reset_btn.grid(row=0,column=3,padx=2,pady=2,sticky=W)







        # <<<<<<<<<<==========RIGHT LABEL FRAME==========>>>>>>>>>>
        # right label frame
        Right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        Right_frame.place(x=580,y=15,width=785,height=426)

        # add image on right frame
        img_right=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student bg.jpg")
        img_tight=img_right.resize((778,70),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        # frame image position
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=778,height=70)


        # table frame create
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=4,y=87,width=769,height=304)

        # <<<<<=====create scroll bar=====>>>>>
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # attendance report table create
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
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # fetch data 
    def FetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # import csv data 
    def importCSV(self):
        global mydata

        # to clear scroll bar 
        mydata.clear()

        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.FetchData(mydata)

    # export csv data 
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported Successfully to "+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    
    # to show data in entry field
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']

        self.var_atten_id.set(rows[0]),
        self.var_atten_roll.set(rows[1]),
        self.var_atten_name.set(rows[2]),
        self.var_atten_dep.set(rows[3]),
        self.var_atten_time.set(rows[4]),
        self.var_atten_date.set(rows[5]),
        self.var_atten_attendance.set(rows[6])


    # reset data 
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()