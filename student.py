class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
students = []
n = int(input("enter the number of student : "))
for i in range(n):
    print(f"\nSTUDENT DETAILS {i + 1}")
    name = input("enter the Name :")
    roll = int(input("enter the roll number :"))
    marks = int(input("enter the marks :"))
    s1 = student(name,roll,marks)
    students.append(s1)
#Append data    
    f = open("file.txt","a")
    f.write(f"{name},{roll},{marks}\n")



remove_name = input("\n enter the name to remove student :")
for j in students :
    if j.name == remove_name:
        students.remove(j)
        print("student remove successfully")
        break
    else:
        print("student not found")
#Write data
f = open("file.txt","w")
for s in students:
    f.write(f"{s.name},{s.roll},{s.marks}\n")
f.close()
#read data 
print("\n---file---")

f = open("file.txt","r")
data = f.readlines()

for line in data:
    print(line.strip())
f.close()    



print("\n===RESULT===")
f = open("file.txt","r")
data = f.readlines()
for s in students :


    if(90<=s.marks<=100):
        GRADE = "A+"
        
    elif(80<=s.marks<90):
        GRADE = "A"
        
    elif(70<=s.marks<80):
        GRADE = "B"
    elif(60<=s.marks<70):
        GRADE = "C"
    elif(50<=s.marks<60):
        GRADE = "D"
    else:
        GRADE = "FAIL"


    print("\nNAME OF THE STUDENT :",s.name)
    print("ROLL NUMBER :",s.roll)
    print("MARKS OF THE STUDENT :",s.marks) 
    print("Grade :",GRADE)   






