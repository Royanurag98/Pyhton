

# class ApnaCollege:
#      College_Name="Genious public" # If you use the same value for every object i.e Class Attribute

#      def __init__(self, S_name, S_Age, S_Roll, S_Reg):
#           self.name=S_name
#           self.age=S_Age
#           self.roll=S_Roll
#           self.reg=S_Reg
# # This is a object attribute and it create a space in memory every time when we create object
# S1=ApnaCollege("Anurag Roy", 24, 57, 122133)
# print(S1.name, S1.age, S1.roll, S1.reg ,S1.College_Name) 
# S2=ApnaCollege("Deepak Kumar", 25, 58, 1229345)
# print(S2.name, S2.age, S2.roll, S2.reg ,S2.College_Name)



# Class Can Store two things first one is Attributes and second one is method

class Student_marks:
    Student_Name="Anurag"
    def __init__(self, Math, Physic, Che, Bio, English):
           self.math=Math # Attribute
           self.physic=Physic
           self.che=Che
           self.bio=Bio
           self.english=English

    def percentage(self): # Method 
          
          Percent=(self.math + self.physic + self.che + self.bio + self.english)*5
          return Percent%100
          



s1_marks=Student_marks(80,70, 82, 75, 92)
print("Student Marks :", "Math",s1_marks.math, s1_marks.physic, s1_marks.che, s1_marks.bio, s1_marks.english)
print("Hello", Student_marks.Student_Name)
print("you Got ",s1_marks.percentage(),"%", " Marks" )
          