import sys
import sqlite3 as sql
from tkinter import *
conn=sql.connect('graduation_progress.db')
c=conn.cursor()
move_on=False

class Course:
    def __init__(self,master):
        # Window Information
        self.master=master
        master.title('Create Courses')

        # Course Labeling Information
        self.code_label=Label(master,text='Dept. Code: ')
        self.code_label.grid(row=0,column=0)
        self.dept_code=Entry(master)
        self.dept_code.grid(row=0,column=1)
        self.num_label=Label(master,text='Course Number: ')
        self.num_label.grid(row=1,column=0)
        self.number=Entry(master)
        self.number.grid(row=1,column=1)
        self.name_label=Label(master,text='Course Name: ')
        self.name_label.grid(row=2,column=0)
        self.course_name=Entry(master)
        self.course_name.grid(row=2,column=1)

        # Prerequisites 
        self.prereq_label=Label(master,text='Please type in the course codes you\'ve already entered to declare as a prerequisite: ')
        self.prereq_label.grid(row=3,column=0)
        self.prerequisites=Entry(master)
        self.prerequisites.grid(row=3,column=1)

        # When the course will be offered
        self.fall=IntVar()
        self.fall_check=Checkbutton(master,text='Fall Semeseter? ',variable=self.fall)
        self.fall_check.grid(row=4,column=0)
        self.spring=IntVar()
        self.spring_check=Checkbutton(master,text='Spring Semester? ',variable=self.spring)
        self.spring_check.grid(row=4,column=1)
        self.odd=IntVar()
        self.odd_check=Checkbutton(master,text='Odd Years? ',variable=self.odd)
        self.odd_check.grid(row=5,column=0)
        self.even=IntVar()
        self.even_check=Checkbutton(master,text='Even Years? ',variable=self.even)
        self.even_check.grid(row=5,column=1)

        # Number of Credits
        self.credit_list=['0','1','2','3','4','5','6']
        self.credits=StringVar()
        self.credit_label=Label(master,text='Number of Credits: ')
        self.credit_label.grid(row=6,column=0)
        self.credit_menu=OptionMenu(master,self.credits,*self.credit_list)
        self.credit_menu.grid(row=6,column=1)

        # Submit Values
        self.submit_button=Button(master, text='Submit Course',command=self.submit)
        self.submit_button.grid(row=7,column=0)
        self.next_button=Button(master,text='Next Section',command=self.next_section)
        self.next_button.grid(row=7,column=1)
        self.course_info=[]

    def submit(self):
        # Save Course Information
        self.course_info.append(str(self.dept_code.get()))
        self.course_info.append(str(self.number.get()))
        self.course_info.append(str(self.course_name.get()))
        self.course_info.append(str(self.prerequisites.get()))
        self.course_info.append(str(int(self.fall.get())))
        self.course_info.append(str(int(self.spring.get())))
        self.course_info.append(str(int(self.odd.get())))
        self.course_info.append(str(int(self.even.get())))
        self.course_info.append(str(self.credits.get()))

        # Create SQL String
        self.string="INSERT INTO Courses VALUES ("
        for i in range(0,len(self.course_info)):
            self.string=self.string+"'"+self.course_info[i]+"'"
            if i==(len(self.course_info)-1):
                self.string=self.string+")"
            else:
                self.string=self.string+", "

        # Execute SQL String and Close Old Window
        c.execute(self.string)
        conn.commit()
        self.master.destroy()

    def next_section(self):
        # Will Close Window and Close While Loop // while loop found on line 148 in add_courses() function
        global move_on
        move_on=True
        self.master.destroy()

def create_databases():
    # Creates SQL Databases Upon Startup Request
    c.execute("""CREATE TABLE Courses
            (Code text,
            Num integer,
            Name text,
            Prerequisite integer,
            Fall integer,
            Spring integer,
            Odd integer,
            Even integer,
            Credits integer
            )""")
    conn.commit()
    c.execute("""CREATE TABLE Majors
            (Name text,
            Concentration text,
            Required text,
            A text,
            B text,
            C text,
            D text,
            Electives text
            )""")
    conn.commit()
    c.execute("""CREATE TABLE Minors
            (Name text,
            Concentration text,
            Required text,
            A text,
            B text,
            Electives text
            )""")
    conn.commit()
    c.execute("""CREATE TABLE Students
            (First text,
            Initial text,
            Last text,
            Major_A text,
            Major_B text,
            Major_C text,
            Minor_A text,
            Minor_B text,
            Minor_C text,
            Credits integer,
            Honors_Credits integer
            )""")
    conn.commit()

def add_courses():
    add=Tk()
    window=Course(add)
    add.mainloop()
    while move_on==False:
        # Will Close when user clicks 'Next Section' button in window
        add=Tk()
        window=Course(add)
        add.mainloop()
    move_on=False

class Curriculum:
    def __init__(self, master,c_type):
        # Window Information
        self.master=master
        self.c_type=c_type
        master.title('Add a %s:' % self.c_type)

        # Curriculum Name
        self.name_label=Label(master,text='%s Name: ' % self.c_type)
        self.name_label.grid(row=0,column=0)
        self.name=Entry(master)
        self.name.grid(row=0,column=1)

        # Courses Required
        self.courses_label=Label(master,text='Please select the required courses to complete this %s: ' % self.c_type)
        self.courses_label.grid(row=1,column=0)
        self.courses_list=Listbox(master,selectmode="multiple")
        self.courses_list.grid(row=1,column=1)
        self.courses=[c.execute("""SELECT name FROM Courses""")]
        self.courses=c.fetchall()
        for course in self.courses:
            self.courses_list.insert(END,course)

        # Submit Values
        self.submit_button=Button(text='Submit %s' % self.c_type,command=self.submit)
        self.submit_button.grid(row=2,column=0)
        self.next_button=Button(text='Next Section',command=self.next)
        self.next_button.grid(row=2,column=1)

    def submit(self):
        self.all_index=self.courses_list.get(0,END)
        self.selected_index=self.courses_list.curselection()
        self.selected_classes=[self.all_index[course] for course in self.selected_index]
        self.string=("INSERT INTO %s VALUES (" % self.c_type)
        self.string=self.string+
        self.master.destroy()

    def next(self):
        global move_on
        move_on=True
        self.master.destroy()

def add_curriculum(c_type):
    c=Tk()
    m=Curriculum(c,c_type)
    c.mainloop()
    while move_on==False:
        # Will Close when user clicks 'Next Section' button in window
        c=Tk()
        m=Curriculum(c,c_type)
        c.mainloop()
    move_on=False

# Where Program Officially Starts    
if sys.argv[1]=='start':
    create_databases()
    add_courses()
    add_curriculum('Major')
    add_curriculum('Minor')
elif sys.argv[1]=='add':
    if sys.argv[2]=='courses':
        add_courses()
    elif sys.argv[2]=='major':
        add_curriculum('Major')
    elif sys.argv[2]=='minor':
        add_curriculum('Minor')
    elif sys.argv[2]=='student':
        pass
elif sys.argv[1]=='help':
    pass
else:
    print('Invalid Input, please type in help in the command prompt for assistance')
        
conn.close()
