from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
# import opencv => having machine learning algorithm
import cv2


class ContactUs:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Help Desk - Contact Us")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")


        # to add image in home
        img=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/contact us.jpg")
        img=img.resize((1400,850),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=850)


        # page title on background image
        title_lbl=Label(bg_img,text="Contact Us",font=("Times",30,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=-2,y=-2,width=1400,height=60)


        # time showing
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        lbl.place(x=1290,y=10,width=100,height=40)
        time()



        dev_label=Label(self.root,text="Welcome to Our Help Desk.", font=("Times",15,"bold italic"),fg="darkblue")
        dev_label.place(x=605,y=82)

        dev_label=Label(bg_img,text="We are happy to help you. Feel free to ask your question and queries.", font=("Times",15,"bold italic"),fg="darkblue")
        dev_label.place(x=465,y=110)

        dev_label=Label(bg_img,text="We are available Monday to Friday from 09:00AM to 06:00PM for Call Support.", font=("Times",15,"bold italic"),fg="darkblue")
        dev_label.place(x=428,y=140)

        dev_label=Label(bg_img,text="Toll-Free No: ", font=("Times",15,"bold italic"),fg="blue")
        dev_label.place(x=605,y=170)

        dev_label=Label(bg_img,text="9876543210", font=("Times",15,"bold italic underline"),fg="blue")
        dev_label.place(x=700,y=170)

        dev_label=Label(bg_img,text="We are available 24/7 for Email Support.", font=("Times",15,"bold italic"),fg="darkblue")
        dev_label.place(x=555,y=200)

        dev_label=Label(bg_img,text="Email ID: ", font=("Times",15,"bold italic"),fg="blue")
        dev_label.place(x=578,y=230)

        dev_label=Label(bg_img,text="abc.google@gmail.com", font=("Times",15,"bold italic underline"),fg="blue")
        dev_label.place(x=648,y=230)

        dev_label=Label(bg_img,text="You can also visit our office. We are open Monday - Friday, 09:00AM to 06:00PM.", font=("Times",15,"bold italic"),fg="darkblue")
        dev_label.place(x=424,y=260)

        dev_label=Label(bg_img,text="Address: ", font=("Times",15,"bold italic"),fg="blue")
        dev_label.place(x=336,y=290)
        dev_label=Label(bg_img,text="NH-95, Chandigarh-Ludhiana Highway, Gharuan, Mohali, Punjab, Chandigarh University Campus", font=("Times",15,"bold italic underline"),fg="blue")
        dev_label.place(x=396,y=290)










if __name__ == "__main__":
    root=Tk()
    obj=ContactUs(root)
    root.mainloop()

