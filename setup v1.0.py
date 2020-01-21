from tkinter import *
from tkinter import filedialog
import xlrd
import classes

def import_sheet(ttl):
    # Import Excel File
    s=Tk()
    s.title(ttl)
    s.fileName=filedialog.askopenfilename(filetypes=(("Excel Sheets","*.xlsx*"),("All Files","*.*")))
    file=s.fileName
    s.destroy()
    workbook=xlrd.open_workbook(file)
    sheet=workbook.sheet_by_index(0)
    return sheet

nex=', '
f=open('students.py','w')
f.write('import classes\n\
courses=[]\n\
p=[]\n\
usernames=[]\n\
passwords=[]\n\
majors=[]\n\
minors=[]\n\
students=[]\n')
f.close()

# Opens Excel File to input student's information
sheet=import_sheet('Students File')

for i in range(0,sheet.nrows):
    new_string='\n'
    f_name=sheet.cell_value(i,0)
    l_name=sheet.cell_value(i,2)
    f_initial=f_name[0]
    if sheet.cell_value(i,1)!='':
        name=f_name+sheet.cell_value(i,1)+l_name
        username=f_initial+sheet.cell_value(i,1)+l_name
    else:
        name=f_name+l_name
        username=f_initial+l_name
    new_string=new_string+'usernames.append("'+username+'")\n'
    password=sheet.cell_value(i,3)
    new_string=new_string+'passwords.append("'+password+'")\n'
    new_string=new_string+'students.append("'+username+'")\n'
    id_number=str(int(sheet.cell_value(i,4)))
    major_a=sheet.cell_value(i,5)
    new_string=new_string+'students.append("'+major_a+'")\n'
    if sheet.cell_value(i,6)!='':
        major_b=sheet.cell_value(i,6)
        new_string=new_string+'students.append("'+major_b+'")\n'
    else:
        major_b='None'
    if sheet.cell_value(i,7)!='':
        major_c=sheet.cell_value(i,7)
        new_string=new_string+'students.append("'+major_c+'")\n'
    else:
        major_c='None'
    if sheet.cell_value(i,8)!='':
        minor_a=sheet.cell_value(i,8)
        new_string=new_string+'students.append("'+minor_a+'")\n'
    else:
        minor_a='None'
    if sheet.cell_value(i,9)!='':
        minor_b=sheet.cell_value(i,9)
        new_string=new_string+'students.append("'+minor_b+'")\n'
    else:
        minor_b='None'
    if sheet.cell_value(i,10)!='':
        minor_c=sheet.cell_value(i,10)
        new_string=new_string+'students.append("'+minor_c+'")\n'
    else:
        minor_c='None'
    if sheet.cell_value(i,11)==1:
        honors=True
    else:
        honors=False

    j=12
    a=True
    f=open('students.py','a')
    f.write('courses.append("'+username+'")\n')
    f.close()
    course=sheet.cell_value(i,j)
    
    while course!='':
        new_string=new_string+'courses.append("'+course+'")\n'
        j+=1
        try:
            course=sheet.cell_value(i,j)
        except IndexError:
            course=''

    new_string=new_string+name+'=classes.Student("'+name+'"'+nex+'"'+username+'"'+nex+'"'+password+'"'+nex+id_number+nex+'"'+major_a+'"'+nex+'"'+major_b+'"'+nex+'"'+major_c+'"'+nex+'"'+minor_a+'"'+nex+'"'+minor_b+'"'+nex+'"'+minor_c+'")\n'
    f=open('students.py','a')
    f.write(new_string)
    f.close()
        
# Opening Another Excel File to import course information from institution
sheet=import_sheet('Classes File')

for i in range(0,sheet.nrows):
    new_string='\n'
    if sheet.cell_value(i,0)=='Major':
        a=False
        b=False
        c=False
        d=False
        e=False
        f=False
        m=False
        r=[]
        one=[]
        two=[]
        three=[]
        four=[]
        five=[]
        six=[]
        math=[]
        credit=str(int(sheet.cell_value(i,1)))
        nam=str(sheet.cell_value(i,2))
        if sheet.cell_value(i,3)=='Concentration':
            concentration=str(sheet.cell_value(i,4))
            z=5
        else:
            concentration=''
            z=3
        go=sheet.cell_value(i,z)
        while go!='':
            if go=='Required':
                q=True
            elif go=='A':
                q=False
                a=True
            elif go=='B':
                a=False
                b=True
            elif go=='C':
                b=False
                c=True
            elif go=='D':
                c=False
                d=True
            elif go=='E':
                d=False
                e=True
            elif go=='F':
                e=False
                f=True
            elif go=='Math':
                a=False
                b=False
                c=False
                d=False
                e=False
                f=False
                m=True
            if q:
                if go!='Required':
                    r.append(sheet.cell_value(i,z))
            # Any courses written into these arrays are interpreted as courses
            # that can be taken from a list; not all are required, however
            # some of the courses within the list must be completed, which
            # courses the student takes however is entirely up to them, so
            # long as they meet the necessary requirements
            elif a:
                if go!='A':
                    one.append(sheet.cell_value(i,z))
            elif b:
                if go!='B':
                    two.append(sheet.cell_value(i,z))
            elif c:
                if go!='C':
                    three.append(sheet.cell_value(i,z))
            elif d:
                if go!='D':
                    four.append(sheet.cell_value(i,z))
            elif e:
                if go!='E':
                    five.append(sheet.cell_value(i,z))
            elif f:
                if go!='F':
                    six.append(sheet.cell_value(i,z))
            elif m:
                if go!='Math':
                    math.append(sheet.cell_value(i,z))
            z+=1
            try:
                go=sheet.cell_value(i,z)
            except IndexError:
                go=''

        new_string=new_string+nam+'=classes.Major('+str(int(credit))+nex+'"'+concentration+'"'+nex+'"'+nam+'")\n'
        new_string=new_string+nam+'.required_courses='+str(r)+'\n'
        if one!=[]:
            new_string=new_string+nam+'.section_a='+str(one)+'\n'
        if two!=[]:
            new_string=new_string+nam+'.section_b='+str(two)+'\n'
        if three!=[]:
            new_string=new_string+nam+'.section_c='+str(three)+'\n'
        if four!=[]:
            new_string=new_string+nam+'.section_d='+str(four)+'\n'
        if five!=[]:
            new_string=new_string+nam+'.section_e='+str(five)+'\n'
        if six!=[]:
            new_string=new_string+nam+'.section_f='+str(six)+'\n'
        if math!=[]:
            new_string=new_string+nam+'.math='+str(math)+'\n'
        f=open('students.py','a')
        f.write(new_string)
        f.write('majors.append("'+nam+'")\n')
        f.close()
    elif sheet.cell_value(i,0)=='Minor':
        r=[]
        one=[]
        two=[]
        math=[]
        req=str(int(sheet.cell_value(i,1)))
        nam=str(sheet.cell_value(i,2))
        z=3
        go=sheet.cell_value(i,z)
        while go!='':
            if go=='Required':
                q=True
            elif go=='A':
                q=False
                a=True
            elif go=='B':
                a=False
                b=True
            elif go=='Math':
                a=False
                b=False
                m=True
            if q:
                if go!='Required':
                    r.append(sheet.cell_value(i,z))
            # Any courses written into these arrays are interpreted as courses
            # that can be taken from a list; not all are required, however
            # some of the courses within the list must be completed, which
            # courses the student takes however is entirely up to them, so
            # long as they meet the necessary requirements
            elif a:
                if go!='A':
                    one.append(sheet.cell_value(i,z))
            elif b:
                if go!='B':
                    two.append(sheet.cell_value(i,z))
            elif m:
                if go!='Math':
                    math.append(sheet.cell_value(i,z))
            z+=1
            try:
                go=sheet.cell_value(i,z)
            except IndexError:
                go=''

        new_string=new_string+nam+'=classes.Minor('+str(int(credit))+nex+'"'+nam+'")\n'
        new_string=new_string+nam+'.required_courses='+str(r)+'\n'
        if one!=[]:
            new_string=new_string+nam+'.section_a='+str(one)+'\n'
        if two!=[]:
            new_string=new_string+nam+'.section_b='+str(two)+'\n'
        if math!=[]:
            new_string=new_string+nam+'.math='+str(math)+'\n'
        f=open('students.py','a')
        f.write(new_string)
        f.write('minors.append("'+nam+'")\n')
        f.close()
            
    else:
        # Actual courses
        dept=str(sheet.cell_value(i,0))
        num=str(int(sheet.cell_value(i,1)))
        name=str(sheet.cell_value(i,2))
        spring=str(int(sheet.cell_value(i,3)))
        fall=str(int(sheet.cell_value(i,4)))
        odd=str(int(sheet.cell_value(i,5)))
        even=str(int(sheet.cell_value(i,6)))
        credit=str(sheet.cell_value(i,7))
        ilt=str(int(sheet.cell_value(i,8)))
        aa=str(int(sheet.cell_value(i,9)))
        p_needed=sheet.cell_value(i,10)
        nam=dept.lower()+str(num)
        notes=''
        prerequisites=[]
        
        if p_needed==1:
            j=11
            prereq=sheet.cell_value(i,j)
            while prereq!='':
                prerequisites.append(prereq)
                j+=1
                try:
                    prereq=sheet.cell_value(i,j)
                except IndexError:
                    prereq=''

        new_string=new_string+nam+'=classes.Course('+credit+nex+even+nex+odd+nex+fall+nex+spring+nex+aa+nex+ilt+nex+'p'
        if p_needed==1:
            new_string=new_string+nex+'True)\n'
        else:
            new_string=new_string+')\n'

        for i in range(0,len(prerequisites)):
            new_string=new_string+nam+'.prerequisites.append("'+str(prerequisites[i])+'")\n'

        f=open('students.py','a')
        f.write(new_string)
        f.close()
