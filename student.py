from tkinter import* # It is library used for making GUI application & software
from tkinter import ttk # for stylying purposes
from PIL import Image,ImageTk  # For opening and displaying image files 
#Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title=("Face Recognition System")


        # First Image 
        img = Image.open(r"C:\Users\KIIT01\Face Recognition System\image\face-recognition.png")
        img=img.resize((520,130),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

        # Second Image
        img2 = Image.open(r"C:\Users\KIIT01\Face Recognition System\image\sitting.jpg")
        img2=img2.resize((530,130),Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=530,y=0,width=520,height=130)

        # Third Image
        img3 = Image.open(r"C:\Users\KIIT01\Face Recognition System\image\smart-attendance.jpg")
        img3=img3.resize((540,130),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=1000,y=0,width=540,height=130)


         #bg img
        img3 = Image.open(r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        img3=img3.resize((1530,710),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)        
        bg_img.place (x=0,y=130,width=1530,height=710)
                       
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("20th Century Font",30, "bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1500,height=650)

        # Left Side Label Frame
        Left_frame = LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=800, height=620)


        img_left = Image.open(r"C:\Users\KIIT01\Face Recognition System\image\handsup.jpeg")
        img_left=img_left.resize((790,160),Image.BILINEAR)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=785,height=160)

        # Current Course Information
        current_course_frame = LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=17, y=160, width=785, height=120)

        ####### Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman", 12, "bold"), bg="white")
        ## We make grid --> rows and column
        dep_label.grid(row=0,column=0, padx=10, sticky=W)


        # Combo Box
        dep_combo=ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="read only", width=20)
        dep_combo['values']=("Select Department", "Computer Science","IT", "Electrical", "Elec.& Tele", "Mechanical","Civil")
        dep_combo.current(0)   # set the default value of combo box to first item
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        ####### Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0,column=2, padx=10, sticky=W)
        # Combo Box
        course_combo=ttk.Combobox(current_course_frame,font=("times new roman", 13, "bold"), state="read only", width=20)
        course_combo['values']=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        ######## Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1,column=0, padx=10, sticky=W)
                        
        # combo box
        year_combo=ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="read only", width=20)
        year_combo['values']=("Select Year", "2020-21", "2021-22", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        ######## Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1,column=2, padx=10, sticky=W)

        # Check box
        semester_combo=ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="read only", width=20)
        semester_combo['values']=("Select Semester", "Semester-1", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        Class_Student_course_frame = LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_course_frame.place(x=17, y=280, width=785, height=340)

        # Student ID
        studentId_label=Label(Class_Student_course_frame,text="StudentId:",font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0,column=0, padx=10, sticky=W)

        studentID_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10, sticky=W)

        # Student name
        studenName_label=Label(Class_Student_course_frame,text="Student Name:",font=("times new roman", 13, "bold"), bg="white")
        studenName_label.grid(row=0,column=2, padx=10, sticky=W)

        studentName_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10, sticky=W)

        # Class division
        class_div_label=Label(Class_Student_course_frame,text="Class Division:",font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1,column=0, padx=10, sticky=W)

        class_div_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1,column=1,padx=10, sticky=W)

        # Roll Number
        roll_no_label=Label(Class_Student_course_frame,text="Roll No:",font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1,column=2, padx=10, sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, sticky=W)

        # Gender
        gender_label=Label(Class_Student_course_frame,text="Gender",font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2,column=0, padx=10, pady=5, sticky=W)

        gender_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2,column=1,padx=10, sticky=W)

        # Date Of Birth
        dob_label=Label(Class_Student_course_frame,text="Date Of Birth:",font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2,column=2, padx=10, pady=5, sticky=W)
        dob_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2,column=3,padx=10, sticky=W)

        # Email
        email_label=Label(Class_Student_course_frame,text="Email:",font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3,column=0, padx=10, pady=5,sticky=W)

        email_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        email_entry.grid(row=3,column=1,padx=10, sticky=W)

        # Phone No:
        phone_no_label=Label(Class_Student_course_frame,text="Phone No:",font=("times new roman", 13, "bold"), bg="white")
        phone_no_label.grid(row=3,column=2, padx=10, pady=5, sticky=W)
        
        phone_no_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        phone_no_entry.grid(row=3,column=3,padx=10, sticky=W)

        # Address
        addresslabel=Label(Class_Student_course_frame,text="Address:",font=("times new roman", 13, "bold"), bg="white")
        addresslabel.grid(row=4,column=0, padx=10, pady=5,sticky=W)

        addressentry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        addressentry.grid(row=4,column=1,padx=10, sticky=W)

        # Teacher Name:
        teacher_label=Label(Class_Student_course_frame,text="Teacher Name:",font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4,column=2, padx=10, pady=5, sticky=W)

        teacher_entry=ttk.Entry(Class_Student_course_frame, width=20,font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10, pady=5, sticky=W)

        # radio buttons
        radiobtn1=ttk.Radiobutton(Class_Student_course_frame, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2=ttk.Radiobutton(Class_Student_course_frame, text="No Photo Sample", value="Yes")
        radiobtn2.grid(row=5, column=1)
        
        # button Frame
        btn_frame=Frame(Class_Student_course_frame,bd=2, relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=190,width=770,height=40)

        # Save button
        save_btn=Button(btn_frame, text="Save",width=19,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update button
        update_btn=Button(btn_frame, text="Update",width=18,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # delete button
        delete_btn=Button(btn_frame, text="Delete",width=18,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn=Button(btn_frame, text="Reset",width=19,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Sample photo and Update Sample Photo Frame
        btn_frame1=Frame(Class_Student_course_frame,bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=4, y=250, width=770, height=40)
        # Take a photo sample
        take_photo_btn=Button(btn_frame1, text="Take photo sample",width=38,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        # Update photo Sample
        update_photo_btn=Button(btn_frame1, text="Update photo sample",width=38,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


        # Right Side Label Frame
        Right_frame = LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=820, y=10, width=670, height=620)

        img_right = Image.open(r"C:\Users\KIIT01\Face Recognition System\image\student.jpg")
        img_right=img_right.resize((780,130),Image.BILINEAR)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=785,height=130)

        # ============= Search system =============
        Search_frame = LabelFrame(Right_frame,bd=2, bg="white",relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=130, width=660, height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman", 15, "bold"), bg="green", fg="white")
        search_label.grid(row=0,column=0, padx=10, pady=5, sticky=W)

        # Check box
        search_combo=ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="read only", width=15)
        search_combo['values']=("Select", "Name","Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        # Entry Fill
        search_entry=ttk.Entry(Search_frame, width=13,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2,padx=10, pady=5, sticky=W)

        # Search button
        search_btn=Button(Search_frame, text="Search",width=11,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        # Show All button
        ShowAll_btn=Button(Search_frame, text="Show All",width=11,font=("times new roman", 13, "bold"),bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4)


        # ===================== Table Frame in right Side ===================
        table_frame = LabelFrame(Right_frame,bd=2, bg="white",relief=RIDGE)
        table_frame.place(x=5, y=210, width=660, height=380)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob","email", "gender", "phone", "address", "teacher", "photo"),xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text= "Department")
        self.student_table.heading("course", text= "Course")
        self.student_table.heading("year", text= "Year")
        self.student_table.heading("sem", text= "Semester")
        self.student_table.heading("id", text= "StudentId")
        self.student_table.heading("name", text= "Name")
        self.student_table.heading("div", text= "Division")
        self.student_table.heading("dob", text= "DOB")
        self.student_table.heading("email", text= "Email")
        self.student_table.heading("phone", text= "Phone")
        self.student_table.heading("address", text= "Address")
        self.student_table.heading("teacher", text= "Teacher")
        self.student_table.heading("photo", text= "PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)

        



        


if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()