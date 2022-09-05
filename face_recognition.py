from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
# date and time import
from time import strftime
from datetime import datetime
# import opencv => having machine learning algorithm
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        # to set resulation
        self.root.geometry("1400x850+0+0")
        # title of the project
        self.root.title("Face Recognition")

        # # add face icon to made dekstop application
        # self.root.wm_iconbitmap("face_icon")


        # page title on background image
        title_lbl=Label(self.root,text="Face Recognition",font=("Times",30,"bold"),bg="yellow",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=60)


        # time showing
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="yellow",fg="black")
        lbl.place(x=1290,y=10,width=100,height=40)
        time()
        


        # add image on face recognition data
        img_top=Image.open("/Users/purnendubikashjana/Visual_Studio/Attendance System/photos/face recognition.jpg")
        img_top=img_top.resize((1400,900),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=1400,height=900)

        # button on face recognition data button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=464,y=250,width=466,height=40)


    # <<<<<<<<<<<<==========MARK ATTENDANCE==========>>>>>>>>>>
    def mark_attendance(self,i,r,n,d):
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    # <<<<<<<<<<<<==========FACE RECOGNITION==========>>>>>>>>>>
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors,)

            coord=[]

            for (x,y,w,h) in features:
                # create rectangle
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                # creating connection to mysql    
                conn=mysql.connector.connect(host="localhost",username="root",password="PBJ/jdbc!21",database="Attendance_System")
                my_cursor=conn.cursor()

                # create database to show student data while student photo show
                my_cursor.execute("select Name from student where Student_ID="+str(id))
                # fetching student name data 
                n=my_cursor.fetchone()
                # n=str(n)
                n="+".join(n)
                

                # create database to show student data while student photo show
                my_cursor.execute("select Roll_No from student where Student_ID="+str(id))
                # fetching student roll no data 
                r=my_cursor.fetchone()
                # r=str(r)
                r="+".join(r)
                

                # create database to show student data while student photo show
                my_cursor.execute("select Department from student where Student_ID="+str(id))
                # fetching student department data 
                d=my_cursor.fetchone()
                # d=str(d)
                d="+".join(d)


                # create database to show student data while student photo show
                my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                # fetching student department data 
                i=my_cursor.fetchone()
                # d=str(d)
                i="+".join(i)
                
                




                # to identify student by student photo ==>> image match by 80% or higher
                if confidence>80:
                    cv2.putText(img,f"ID:{r}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf) # color['blue'] => (255,25,255)
            return img
            
        # to reade classifier
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # capture video 
        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()