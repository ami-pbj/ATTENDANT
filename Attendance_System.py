from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from aboutUs import AboutUs
from contactUs import ContactUs



class Attendance_System:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Attendance System")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")

        # to add image in home
        img=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/FACE_HOME.JPEG")
        img=img.resize((1400,850),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=850)

        # # to add another images we repeat same
        # # second image
        # img=Image.open("/Users/purnendubikashjana/Downloads/FACE_HOME-2.JPEG")
        # img=img.resize((1500,850),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1500,height=850)

        # # third image
        # img=Image.open("/Users/purnendubikashjana/Downloads/FACE_HOME-2.JPEG")
        # img=img.resize((1500,850),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1500,height=850)



        # project title on background image
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Times",30,"bold"),bg="yellow",fg="darkblue")
        title_lbl.place(x=-2,y=-2,width=1400,height=60)


        # time showing
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        lbl.place(x=1290,y=10,width=100,height=40)
        time()


        # add buttons
        # student button
        img4=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/student button.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand")
        b1.place(x=70,y=100,width=200,height=180)

        # button on student button
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=70,y=250,width=200,height=40)


        # detect face
        img5=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/face detector.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand",command=self.face_data)
        b1.place(x=410,y=100,width=200,height=180)

        # button on detect face button
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1.place(x=410,y=250,width=200,height=40)


        # attendance button
        img6=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand",command=self.attendance_data)
        b1.place(x=770,y=100,width=200,height=180)

        # button on attendance button
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1.place(x=770,y=250,width=200,height=40)


        # contact us button
        img7=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/help desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand",command=self.help_data)
        b1.place(x=1130,y=100,width=200,height=180)

        # button on contact us button
        b1=Button(bg_img,text="Contact Us",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1.place(x=1130,y=250,width=200,height=40)


        # train data button
        img8=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/train data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand",command=self.train_data)
        b1.place(x=70,y=400,width=200,height=180)

        # button on help button
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1.place(x=70,y=550,width=200,height=40)


        # photos button
        img9=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/photos.png.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand",command=self.open_img)
        b1.place(x=410,y=400,width=200,height=180)

        # button on photos button
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=410,y=550,width=200,height=40)


        # about us button
        img10=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand",command=self.developer_data)
        b1.place(x=770,y=400,width=200,height=180)

        # button on about us button
        b1_1=Button(bg_img,text="About Us",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=770,y=550,width=200,height=40)


        # exit button
        img11=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand",command=self.iExit)
        b1.place(x=1130,y=400,width=200,height=180)

        # button on exit button
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="black")
        b1_1.place(x=1130,y=550,width=200,height=40)


    def open_img(self):
        os.startfile("data")



    # exit button
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit from this page ??",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # <<<<<<<<<<==========FUNCTION BUTTONS==========>>>>>>>>>>
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
        self.app=AboutUs(self.new_window)


    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ContactUs(self.new_window)








if __name__ == "__main__":
    root=Tk()
    obj=Attendance_System(root)
    root.mainloop()