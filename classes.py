class Course:
    def __init__(self, credit, even, odd, fall, spring, aa, ilt, prerequisites, prerequisites_needed=False):
        self.credit=credit
        self.even=even
        self.odd=odd
        self.spring=spring
        self.fall=fall
        self.aa=aa
        self.ilt=ilt
        self.prerequisites=[]
        self.prerequisites_needed=prerequisites_needed

class Minor:
    def __init__(self, required_credits, name):
        self.required_credits=required_credits
        self.required_courses=[]
        self.section_a=[]
        self.seciton_b=[]
        self.section_c=[]
        self.section_d=[]
        self.math=[]
        self.name=name

class Major:
    def __init__(self, required_credits, concentration, name):
        self.required_credits=required_credits
        self.required_courses=[]
        self.section_a=[]
        self.seciton_b=[]
        self.section_c=[]
        self.section_d=[]
        self.section_e=[]
        self.section_f=[]
        self.math=[]
        self.concentration=concentration
        self.name=name

class Student:
    def __init__(self, name, username, password, id_number, major_a, major_b, major_c, minor_a, minor_b, minor_c):
        self.name=name
        self.username=username
        self.password=password
        self.id_number=id_number
        self.major_a=major_a
        self.major_b=major_b
        self.major_c=major_c
        self.minor_a=minor_a
        self.minor_b=minor_b
        self.minor_c=minor_c

def login():
    user=str(input('Username: '))
    password=str(input('Password: '))
    a=(user, password)
    return a

def check(a):
    for j in range(0,10):
        if str(j) in a:
            return True
    return False

def split(a,i):
    two=['cs','sa','cj','fp']
    three=["bio","bus","cem","eco","eng","hhp","hst","irm","ids","jmc","mth","mus","phl","pha","pos","psy","rel","sci","srm","thr","art","wgs","wrl","wrt"]
    credit=a[0]
    d_code=str(a[1])+str(a[2])
    for j in range(0,4):
        if d_code==two[j]:
            yes=True
            break
        else:
            yes=False
    if 'H' in a:
        honors=True
    else:
        honors=False
    if yes:
        course=a[3]+a[4]+a[5]
        grade=a[6]
        if a[7]=='+' or a[7]=='-':
            grade=grade+a[7]
            percentage=a[8]+a[9]
        else:
            percentage=a[7]+a[8]
    else:
        d_code=d_code+a[3]
        course=a[4]+a[5]+a[6]
        grade=a[7]
        if a[8]=='+' or a[8]=='-':
            grade=grade+a[8]
            percentage=a[9]+a[10]
        else:
            percentage=a[8]+a[9]
    if i==0:
        return credit
    elif i==1:
        return d_code
    elif i==2:
        return course
    elif i==3:
        return grade
    elif i==4:
        return percentage
    elif i==5:
        return honors
