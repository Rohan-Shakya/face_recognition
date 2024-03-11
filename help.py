from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongition system")


        title_lbl=Label(self.root,text="HELP DESK",font=("time new roman",35,"bold"),bg="Blue",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Image_detail/helpdesk.jpg")
        img_top=img_top.resize((1530,720),Image.AFFINE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=1530,height=720)

        help_label=Label(f_lbl,text="Email:-karkibikram786@gmail.com ",font=("times new roman",25,"bold"),bg="white")
        help_label.place(x=600,y=450)

    




if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()               