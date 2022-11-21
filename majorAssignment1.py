def name():
    print('WELCOME STUDENT! \n')
    a=input('Enter your first name: ').title()
    b=input('Enter your middle name \n(Press ENTER if you don\'t have one): ').title()
    c=input('Enter your last name: ').title()
    print(" ")
    if b=='':
        print('Name of the student is',c,',', a, b, "\n")
    else:
        print('Name of the student is',c, ',', a,',', b,"\n")
def enroll():
    a=str(input('Enter admission year: '))
    assert len(a)==4,'Invalid input! Please enter correct four digit admission year!'
    b=str(input('Enter branch code: ')).upper()
    assert len(b)==2, 'Invalid input! Please enter the two letter abbreviated branch code.'
    c=input('Enter a unique FOUR digit number: ')
    assert len(c)==4, 'Invalid input! Please enter four digits only!'
    print(" ")
    print("Enrollment number: ", a+b+c, "\n")
def grade(a):
    if a < 40:
        return 'D (Fail)'
    elif a >= 40 and a < 60:
        return 'C';
    elif a >= 60 and a < 80:
        return 'B'
    else:
        return 'A'
def marks():
    a = str(input('Enter the 1st subject: ')).title()
    b = int(input("Enter marks in the above subject: "))
    assert b<=100, 'Invalid input! Enter marks out of 100 only!'
    c = str(input('Enter the 2nd subject: ')).title()
    d = int(input("Enter marks in the above subject: "))
    assert d<=100, 'Invalid input! Enter marks out of 100 only!'
    e = str(input('Enter the 3rd subject: ')).title()
    f = int(input("Enter marks in the above subject: "))
    assert f<=100, 'Invalid input! Enter marks out of 100 only!'
    print(" ")
    print(a,':',b,'| Grade:',grade(b))
    print(c,':',d,'| Grade:',grade(d))
    print(e,':',b,'| Grade:',grade(f))
    p=((b+d+f)*100)/300
    print(" ")
    print('Percentage (out of 300):', int(p),'%', '\nYour overall grade is', grade(p))
name()
enroll()
marks()
