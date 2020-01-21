import classes
import students
from tkinter import *
import login
from tkinter import ttk

# User Login
root=Tk()
root.title('Login')
lf=login.LoginFrame(root)
root.mainloop()

# Sorts out classes that logged-in student has taken
user=login.username
taken=[]
major_a=""
major_b=""
major_c=""
minor_a=""
minor_b=""
minor_c=""

for i in range(0,len(students.students)):
    if students.students[i]==user:
        a=0
        b=0
        for j in range(i+1,i+7):
            if students.students[j] in students.majors:
                a+=1
                if a==1:
                    major_a=students.students[j]
                elif a==2:
                    major_b=students.students[j]
                elif a==3:
                    major_c=students.students[j]
            elif students.students[j] in students.minors:
                b+=1
                if b==1:
                    minor_a=students.students[j]
                elif b==2:
                    minor_b=students.students[j]
                elif b==3:
                    minor_c=students.students[j]
            else:
                break

for i in range(0,len(students.courses)):
    if students.courses[i]==user:
        a=1
        while classes.check(students.courses[i+a])==True:
            taken.append(students.courses[a+i])
            a+=1

credit=0
p=[]
for i in range(0,len(taken)):
    arr=[]
    for j in range(0,6):
        a=classes.split(taken[i],j)
        arr.append(a)
    credit=credit+int(arr[0])
    c=arr[1]+arr[2]
    p.append(c)

a=0
one=True
two=True
three=True
four=True
five=True
six=True
t=0

d=Tk()
Label(d,text='Liberal Arts Course Requirements:').pack()
Label(d,text='').pack()
listbox_widget=Listbox(d)

for k in range(0,len(students.liberal_arts.required_courses)):
    if students.liberal_arts.required_courses[k] not in p:
        listbox_widget.insert(END, students.liberal_arts.required_courses[k])
    else:
        t+=1
for k in range(0,len(p)):
    if p[k] in students.liberal_arts.section_a:
        one=False
        t+=1
    if p[k] in students.liberal_arts.section_b:
        a+=1
        t+=1
        if a==2:
            two=False
    if p[k] in students.liberal_arts.section_c:
        three=False
        t+=1
    if p[k] in students.liberal_arts.section_d:
        four=False
        t+=1
    if p[k] in students.liberal_arts.section_e:
        five=False
        t+=1
    if p[k] in students.liberal_arts.section_f:
        six=False
        t+=1

def bar(progress):
    bar_width=100
    n=['[']
    pos=progress*bar_width
    for i in range(0,bar_width):
        if i<pos:
            n.append('=')
        elif i==pos:
            n.append('>')
        else:
            n.append(' ')
    n.append(']')
    res="".join(n)
    new_string=str(res)+'\n'+str(int(progress*100))+'%'
    return new_string

progress=t/11

if one:
    listbox_widget.insert(END, 'Please take 3 credits to satisfy Creative Experience:')
    for i in range(0,len(students.liberal_arts.section_a)):
        listbox_widget.insert(Tkinter.END, students.liberal_arts.section_a[i])
    listbox_widget.insert(END, '')

if two:
    listbox_widget.insert(END, 'Please take 6 credits to satisfy Global Diversity:')
    for i in range(0,len(students.liberal_arts.section_b)):
        listbox.widget.insert(Tkinter.END, students.liberal_arts.section_b[i])
    listbox_widget.insert(END, '')

if three:
    listbox_widget.insert(END, 'Please take 3 credits to satisfy Mathematics Proficiency:')
    for i in range(0,len(students.liberal_arts.section_c)):
        listbox_widget.insert(Tkinter.END, students.liberal_arts.section_c[i])
    listbox_widget.insert(END, '')

if four:
    listbox_widget.insert(END, 'Please take 3 credits to satisfy Natural World')
    for i in range(0,len(students.liberal_arts.section_d)):
        listbox_widget.insert(Tkinter.END, students.liberal_arts.section_d[i])
    listbox_widget.insert(END, '')

if five:
    listbox_widget.insert('Please take 3 credits to satisfy Service Learning')
    for i in range(0,len(students.liberal_arts.section_e)):
        listbox_widget.insert(Tkinter.END, students.liberal_arts.section_e[i])
    listbox_widget.insert(END, '')

if six:
    listbox_widget.insert(END, 'Please take 3 credits to satisfy Senior Experience')
    for i in range(0,len(students.liberal_arts.section_f)):
        listbox_widget.insert(Tkinter.END, students.liberal_arts.section_f[i])
    listbox_widget.insert(END, '')

a=True
b=0
c=0
listbox_widget.pack()

# Reset listbox
listbox_widget=Listbox(d)

if major_a=="biology_gen" or major_b=="biology_gen" or major_c=="biology_gen":
    Label=(d,'Biology: General Biology Concentration').pack()
    for i in range(0,len(students.biology_gen.required_courses)):
        if students.biology_gen.required_courses[i] not in p:
            listbox_widget.insert(END, students.biology_gen.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.biology_gen.section_a:
            b+=1
            c+=b
            if b>4:
                listbox_widget.insert(END, 'Other credits completed')
                a=False
                break
    if b<5:
        listbox_widget.insert(END, 'Please complete several of the following:')
        for i in range(0,len(students.biology_gen.section_a)):
            listbox_widget.insert(END, students.biology_gen.section_a[i])

    d=len(students.biology_gen.required_courses)+5

    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

b=0
c=0
if major_a=="biology_bm" or major_b=="biology_bm" or major_c=="biology_bm":
    Label(d,text='Biology: Mollecular Biology Concentration:').pack()
    for i in range(0,len(students.biology_bm.required_courses)):
        if students.biology_bm.required_courses[i] not in p:
            listbox_widget.insert(END, students.biology_bm.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.biology_bm.section_a:
            b+=1
            c+=1
            if b>3:
                listbox_widget.insert(END, 'Other credits completed')
                a=False
                break
    if b<4:
        listbox_widget.insert(END, 'Please complete several of the following:')
        for i in range(0,len(biology_bm.section_a)):
            listbox_widget.insert(END, students.biology_bm.section_a[i])

    d=len(students.biology_bm.required_courses)+4

    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

b=0
c=0
if major_a=="biology_prem" or major_b=="biology_prem" or major_c=="biology_prem":
    Label(d,text='Biology: Pre-Medical Concentration:').pack()
    for i in range(0,len(students.biology_prem.required_courses)):
        if students.biology_prem.required_courses[i] not in p:
            print(students.biology_prem.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.biology_prem.section_a:
            b+=1
            c+=1
            if b>2:
                print('Other credits completed')
                a=False
                break
    if b<3:
        print('Please complete several of the following:')
        for i in range(0,len(students.biology_prem.section_a)):
            print(students.biology_prem.section_a[i])

    d=len(students.biology_prem.required_courses)+3
    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

b=0
c=0
if major_a=="biology_eco" or major_b=="biology_eco" or major_c=="biology_eco":
    Label(d,text='Biology: Ecological Studies Concentration:').pack()
    for i in range(0,len(students.biology_eco.required_courses)):
        if students.biology_eco.required_courses[i] not in p:
            listbox_widget.insert(END, students.biology_eco.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.biology_eco.section_a:
            b+=1
            c+=1
            if b>4:
                listbox_widget.insert(END,'Other credits completed')
                a=False
                break
    if b<5:
        listbox_widget.insert(END,'Please complete several of the following:')
        for i in range(0,len(students.biology_eco.section_a)):
            listbox_widget.insert(END, students.biology_eco.section_a[i])

    d=len(students.biology_eco.required_courses)+5
    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

c=0
if major_a=="it_management" or major_b=="it_management" or major_c=="it_management":
    Label(d,text='Information Technology Management Major:').pack()
    for i in range(0,len(students.it_management.required_courses)):
        if students.it_management.required_courses[i] not in p:
            listbox_widget.insert(END,students.it_management.required_courses[i])
        else:
            c+=1

    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

b=0
c=0
if major_a=="computerscience" or major_b=="computerscience" or major_c=="computerscience":
    Label(d,text='Computer Science Major:').pack()
    for i in range(0,len(students.computerscience.required_courses)):
        if students.computerscience.required_courses[i] not in p:
            listbox_widget.insert(END,students.computerscience.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.computerscience.section_a:
            b+=1
            c+=1
            if b>2:
                listbox_widget.insert(END,'Other credits completed')
                a=False
                break
    if b<3:
        listbox_widget.insert(END,'Please complete several of the following:')
        for i in range(0,len(students.computerscience.section_a)):
            listbox_widget.insert(END,students.computerscience.section_a[i])

    d=len(students.computerscience.required_courses)+3
    listbox_widget.pack()
    # Int object has no attribute 'tk'
    del listbox_widget
    listbox_widget=Listbox(d)
    
b=0
c=0
if minor_a=="comp_sci" or minor_b=="comp_sci" or minor_c=="comp_sci":
    Label(d,text='Computer Science Minor:').pack()
    for i in range(0,len(students.comp_sci.required_courses)):
        if students.comp_sci.required_courses[i] not in p:
            listbox_widget.insert(END,students.comp_sci.required_courses[i])
        else:
            c+=1
    for i in range(0,len(p)):
        if p[i] in students.comp_sci.section_a:
            b+=1
            c+=1
            if b>2:
                listbox_widget.insert(END,'Other Credits Completed')
                a=False
                break
    if b<3:
        print('Please complete several of the following:')
        for i in range(0,len(students.comp_sci.section_a)):
            print(students.comp_sci.section_a[i])

    d=len(students.comp_sci.required_courses)+3
    listbox_widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

c=0
if minor_a=='bio' or minor_b=='bio' or minor_c=='bio':
    Label(d,text='Biology Minor').pack()
    for i in range(0,len(students.bio.required_courses)):
        if students.bio.required_courses[i] not in p:
            print(students.bio.required_courses[i])
        else:
            c+=1

    listbox.widget.pack()
    del listbox_widget
    listbox_widget=Listbox(d)

def close():
    exit(0)

# Int object has no attribute 'tk'
b=Button(d,text='Close',command=close)
b.pack()
