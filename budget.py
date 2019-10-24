
"""
Is it in my budget ?
Fonction to calcultae the price with taxes, and to know if it's my budget
10/2019
Author:
        Juliette Forest
"""


class shopping(): #name of our class
        def __init__(self, my_budget): #give default values
        self.budget = my_budget # initialisation value (default)
        self.HT = int(input("Price without taxes?")) # initialisation value (default)

    # utility 1: calculate the price with taxes
    def add_tva(self):
        TVA = self.HT*19.6 / 100
        TTC = self.HT + TVA
        return TTC

    # utility 2: does it fit my budget ?
    def can_I_buy_it(self):
        if self.HT > self.budget:
            return "NO, Too expensive"
        else:
            return "YES, buy it!"
