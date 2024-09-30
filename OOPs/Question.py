# Create Student class that takes name and marks of 3 subject as arguments in constructor then create a method to print the average

class Student:
    Student_Name="Anurag Kumar"
    def Studen_Marks(self,math, physics ,chemestry):
        Avg= (math + physics + chemestry)/3
        return Avg


Result=Student()
print(Result.Student_Name)
print(Result.Studen_Marks(80,70,90))

class Account:
    def __init__(self, balance, accountNo):
        self.balance=balance
        self.accountNo=accountNo
    def Balance(self,Cridit, Debit ):
       debit= self.balance-Debit
       cridit= self.balance+Cridit
      
       if(cridit>=20000):
        print("You are crideted RS.",Cridit,"Now your balnce is",cridit)
       elif(debit<20000):
           print("You are crideted RS.",Debit,"Now your balnce is",debit)
      
       
        

Account_Balance=Account(20000, 894673332435424)
# Account_Balance.Balance(2000,1000)
Account_Balance.Balance(int(input(" Enter your Cridit Balance:" )) ,int(input(" Enter your Debit Balance:" )))

# print(Account_Balance.balance)
# print(Account_Balance.account)

       
