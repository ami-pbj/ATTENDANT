from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
# import opencv => having machine learning algorithm
import cv2


class AboutUs:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Developer Page - About Us")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")


        # to add image in home
        img=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/Pasted Graphic.jpg")
        img=img.resize((1400,970),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=970)


        # page title on background image
        title_lbl=Label(bg_img,text="About Us",font=("Times",30,"bold"),bg="yellow",fg="green")
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
        main_frame.place(x=3,y=63,width=1387,height=636)


        # <<<<<<<<<<==========LEFT LABEL FRAME==========>>>>>>>>>>
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="My Info",font=("times new roman",12,"bold"),fg="green",bg="white")
        Left_frame.place(x=15,y=15,width=550,height=600)


        # add image on left frame
        img_left=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/PNG image 13 copy.png")
        img_left=img_left.resize((550,580),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=543,height=580)


        # <<<<<<<<<<==========RIGHT LABEL FRAME==========>>>>>>>>>>
        # right label frame
        Right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="About Me",font=("times new roman",12,"bold"),fg="green",bg="white")
        Right_frame.place(x=580,y=15,width=785,height=600)

        # # add image on right frame
        # img_right=Image.open("/Users/purnendubikashjana/Downloads/student bg.jpg")
        # img_tight=img_right.resize((778,70),Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # # frame image position
        # f_lbl=Label(Right_frame,image=self.photoimg_right)
        # f_lbl.place(x=0,y=0,width=778,height=70)

        # developer details 
        # text details
        dev_label=Label(Right_frame,text="Hello everyone, i'm Purnendu Bikash Jana from Kolkata, West Bengal. I've completed    m y    g r a d u a t i o n    i n", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=15,y=5)

        dev_label=Label(Right_frame,text="Mathematics from University of Calcutta. Now i'm pursuing MCA from Chandigarh University. ", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=5,y=30)

        dev_label=Label(Right_frame,text="I did some projects and some of those are given below: ", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=5,y=70)

        dev_label=Label(Right_frame,text="1. Online Job Portal in JAVA used HTML, CSS, JS, Servlet, JDBC and MySQL for database.  A l s o   used JSTL and", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=15,y=100)

        dev_label=Label(Right_frame,text="Tomcat as a server.", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=30,y=125)

        dev_label=Label(Right_frame,text="2. Student Management System in JAVA. This project basically focused on how SQL queries work on Database.", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=15,y=150)

        dev_label=Label(Right_frame,text="3. Library Management System in JAVA and used HTML, CSS, JDBC and MySQL database.", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=15,y=175)


        dev_label=Label(Right_frame,text="To get any help regarding this project only, reach out to me from <<Help Desk>> from <<Home>> page.", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=5,y=215)


        dev_label=Label(Right_frame,text="If you want to contact me regarding any project or want any project then Email me. I've attached my Email ID below.", font=("Times",15,"bold italic"),fg="darkblue",bg="white")
        dev_label.place(x=5,y=250)


        dev_label=Label(Right_frame,text="Email ID: ", font=("Times",15,"bold italic"),fg="blue",bg="white")
        dev_label.place(x=5,y=285)

        dev_label=Label(Right_frame,text="purnendubikash.21@gmail.com", font=("Times",15,"bold italic underline"),fg="blue",bg="white")
        dev_label.place(x=80,y=285)

        





if __name__ == "__main__":
    root=Tk()
    obj=AboutUs(root)
    root.mainloop()

