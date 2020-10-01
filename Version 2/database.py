import sys
import sqlite3
conn=sqlite3.connect('graduation_progress.db')
c=conn.cursor()
from tkinter import *
class Course:
    def __init__(self, master):
        self.master=master
        master.title('Create Courses')
        self.code_label=Label(self, text='Dept. Code: ')
        self.code_label.grid(row=0,column=0)
        self.dept_code=Entry(self)
        self.dept_code.grid(row=0,column=1)
        self.num_label=Label(self, text='Course Number: ')
        self.num_label.grid(row=1,column=0)
        self.number=Entry(self)
        self.number.grid(row=1,column=1)
        self.name_label=Label(self, text='Course Name: ')
        self.name_label.grid(row=2,column=0)
        self.course_name=Entry(self)
        self.course_name.grid(row=2,column=1)
        self.prereq_label=Label(self, text='Please type in the course codes you\'ve already entered to declare as a prerequisite: ')
        self.prereq_label.grid(row=3,column=0)
        self.prerequisites=Entry(self)
        self.prerequisites.grid(row=3,column=1)
        self.fall=IntVar()
        self.fall_check=Checkbutton(self, text='Fall Semeseter? ', variable=fall)
        self.fall_check.grid(row=4,column=0)
        self.spring=IntVar()
        self.spring_check=Checkbutton(self, text='Spring Semester? ', variable=spring)
        self.spring_check.grid(row=4,column=1)
        self.odd=IntVar()
        self.odd_check=Checkbutton(self, text='Odd Years? ', variable=odd)
        self.odd_check.grid(row=5,column=0)
        self.even=IntVar()
        self.even_check=Checkbutton(self, text='Even Years? ',variable=even)
        self.even_check.grid(row=5,column=1)
        self.credit_list=['0','1','2','3','4','5','6']
        self.credits=StringVar()
        self.credit_label=Label(self,text='Number of Credits: ')
        self.credit_label.grid(row=6,column=0)
        self.credit_menu=OptionMenu(self, self.credits, *self.credit_list)
        self.credit_menu.grid(row=6,column=1)
        self.submit_button=Button(self, text='Submit Course', command=self.submit)
        self.submit_button.grid(row=7,column=0)
        self.next_button=Button(self,text='Next Section', command=self.next_section)
        self.next_button.grid(row=7,column=1)
        self.move_on=False

    def submit(self):
        self.course_info=[]
        self.course_info.append(str(self.dept_code.get()))
        self.course_info.append(str(self.number.get()))
        self.course_info.append(str(self.course_name.get()))
        self.course_info.append(str(self.prerequisites.get()))
        self.course_info.append(str(int(self.fall.get())))
        self.course_info.append(str(int(self.spring.get())))
        self.course_info.append(str(int(self.odd.get())))
        self.course_info.append(str(int(self.even.get())))
        self.course_info.append(str(self.credits.get()))

    def next_section(self):
        self.move_on=True

def create_databases():
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
    c.execute("""INSERT INTO Courses VALUES
            (%s, %s, %s, %s, %i, %i, %i, %i, %s)""" % add.course_info[0],
                add.course_info[1], add.course_info[2], add.course_info[3],
                add.course_info[4], add.course_info[5], add.course_info[6],
                add.course_info[7])
    conn.commit()
    while add.move_on==False:
        add=Tk()
        window=Course(add)
        add.mainloop()
        if add.move_on==False:
            c.execute("""INSERT INTO Courses VALUES
                    (%s, %s, %s, %s, %i, %i, %i, %i, %s)""" % add.course_info[0],
                      add.course_info[1], add.course_info[2], add.course_info[3],
                      add.course_info[4], add.course_info[5], add.course_info[6],
                      add.course_info[7])
            conn.commit()
        else:
            break

class Minor:
    def __init__(self, master):
        self.master=master
        
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
if sys.argv[1]=='start':
    create_databases()
    add_courses()
elif sys.argv[1]=='add':
    if sys.argv[2]=='courses':
        add_courses()
    elif sys.argv[2]=='major':
        pass
    elif sys.argv[2]=='minor':
        pass
    elif sys.argv[2]=='student':
        pass
elif sys.argv[1]=='help':
    pass
else:
    print('Invalid Input')
        
conn.close()
