from tkinter import Tk, Label, Button, Toplevel
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Top image
        top_img = self.load_image("C:\\Users\\KIIT01\\Face Recognition System\\images\\img11.jpg", (1700, 130))
        f_lbl = Label(self.root, image=top_img)
        f_lbl.place(x=0, y=0, width=1700, height=130)

        # Background image
        bg_img = self.load_image("C:\\Users\\KIIT01\\Face Recognition System\\images\\bg.jpg", (1530, 710))
        bg_label = Label(self.root, image=bg_img)
        bg_label.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_label, text="CHECKING SYSTEM COMPATIBILITY INSIGHTS", font=("20th Century Font", 30), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Functionality Buttons
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\stu.png", "Student Details", 200, 100, self.student_details)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\stu.jpg", "Face Detector", 500, 100)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\det.jpg", "Attendance", 800, 100)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\help.jpg", "Help Desk", 1100, 100)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\train.jpg", "Train Data", 200, 370)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\phot.jpg", "Photos", 500, 370)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\dev.jpg", "Developer", 800, 370)
        self.create_button(bg_label, "C:\\Users\\KIIT01\\Face Recognition System\\images\\exit.jpg", "Exit", 1100, 370)

    def load_image(self, path, size):
        img = Image.open(path)
        img = img.resize(size, Image.BILINEAR)
        return ImageTk.PhotoImage(img)

    def create_button(self, parent, image_path, text, x, y, command=None):
        photo = self.load_image(image_path, (200, 200))
        btn_image = Button(parent, image=photo, cursor="hand2", command=command)
        btn_image.image = photo  # keep a reference!
        btn_image.place(x=x, y=y, width=200, height=200)
        btn_text = Button(parent, text=text, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=command)
        btn_text.place(x=x, y=y+200, width=200, height=40)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
