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
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Attendance System")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")

        # page title on background image
        title_lbl=Label(self.root,text="Train Data Set",font=("Times",30,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=60)

        # time showing
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        lbl.place(x=1290,y=10,width=100,height=40)
        time()


        # add image on train data
        img_top=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/train face data.jpg")
        img_top=img_top.resize((1400,850),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=1400,height=850)

        
        # button on train data button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=464,y=310,width=466,height=40)
        
        # add image on train data set 
        # img_bottom=Image.open("/Users/purnendubikashjana/Downloads/student bg.jpg")
        # img_bottom=img_bottom.resize((550,70),Image.ANTIALIAS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=60,width=543,height=70)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imageNp=np.array(img,'uint8') # alternative => (np.uint8(img)) // uint8 instead of unit8 because of module 'numpy' has no attribute 'unit8'
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        # convert ids into array using numpy
        ids=np.array(ids)


        # Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning Datasets Completed !!")



        






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
