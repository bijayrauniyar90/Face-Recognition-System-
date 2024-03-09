from tkinter import* # It is library used for making GUI application & software
from tkinter import ttk # for stylying purposes
from PIL import Image,ImageTk  # For opening and displaying image files 
#Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title=("Face Recognition System")





if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()