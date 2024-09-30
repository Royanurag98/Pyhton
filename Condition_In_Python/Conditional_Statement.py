#////////////////////////////////////////////////////// CONDITIONAL STATEMENT ////////////////////////////////////

# if
# elif
# else
#EXAMPLE//////////////////////////////
traficLight='green'
if(traficLight=="Red"):
    print("STOP..................")
elif(traficLight=="yellow"):
    print("REDY FO GO..........")
else:
    print('GO.........')

#EXAMPLE//////////////////////////////

Age=int(input("Enter you age"))
if(Age>=18):
    print("your eligible for vote.......")
elif(Age<18):
    print("YOUR NOT ELIGIBLE FOR VOTE....")
else:
    print("YOUR ARE A KIDS.....")

#EXAMPLE//////////////////////////////
#Grade of studen based on marks
Student_Marks=int(input("Enter your marks"))
if(Student_Marks>=90):
    print("YOU GOT A GRADE")
elif(Student_Marks>=80 and Student_Marks<90):
    print("YOU GOT B GRADE")
elif(Student_Marks>=70 and Student_Marks<80):
     print("YOU GOT C GRADE")
elif(Student_Marks>=60 and Student_Marks<70):
     print("YOU GOT D GRADE")
else:
    print("YOU ARE FAIL")


#EXAMPLE//////////////////////////////
Student_Marks=int(input("Enter your marks"))
if(Student_Marks>=90):
    Grade="A"
elif(Student_Marks>=80 and Student_Marks<90):
    Grade="B"
elif(Student_Marks>=70 and Student_Marks<80):
    Grade="C"
elif(Student_Marks>=60 and Student_Marks<70):
    Grade="D"
else:
    Grade="Fail.........................."

print("You Got ", Grade)

