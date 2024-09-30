
class Students:
    Coleege_Name="Genious Public School"

    def __init__(self) -> None:
        pass
    
    def __init__(self, Sname, Physics , Chemistry, Math):
        self.Sname=Sname
        self.Physics=Physics
        self.Chemistry=Chemistry
        self.Math=Math
        print("Welcome",self.Sname)

    def Avg_Marks(self):
        avg=(self.Physics + self.Chemistry +  self.Math)/3
        return avg
        
        
S1=Students("Anurag", 90, 89,92)
print("Your Average Marks is",S1.Avg_Marks())