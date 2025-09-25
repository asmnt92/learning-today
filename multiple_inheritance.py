class Father:
    F_blood='*****'

class Mother:
    M_blood='%%%%%%%%'

class Child(Father,Mother):
    def show_blood(self):
        print(f"{self.F_blood+self.M_blood}")

Child().show_blood()