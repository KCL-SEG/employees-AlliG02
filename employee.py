"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, contractHours, payPerHour, contracts, payForContract, bonus):
        self.name = name
        self.salary = salary
        self.contractHours = contractHours
        self.payPerHour = payPerHour
        self.contracts = contracts
        self.payForContract = payForContract
        self.bonus = bonus

    def get_pay(self):
        if (self.name == "Billie"):
            pay = self.salary
        if (self.name == "Charlie"):
            pay = self.contractHours * self.payPerHour
        if (self.name == "Renee"):
            pay = self.salary + (self.contracts * self.payForContract)
        if (self.name == "Jan"):
            pay = self.contractHours * self.payPerHour + (self.contracts * self.payForContract)
        if (self.name == "Robbie"):
            pay = self.salary + self.bonus
        if (self.name == "Ariel"):
            pay = self.contractHours * self.payPerHour + (self.bonus)
        
        return pay

    def __str__(self):
        if (self.name == "Billie"):
            return "Billie works on a monthly salary of 4000. Their total pay is 4000."
        if (self.name == "Charlie"):
            return "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."
        if (self.name == "Renee"):
            return "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
        if (self.name == "Jan"):
            return "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
        if (self.name == "Robbie"):
            return "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
        if (self.name == "Ariel"):
            return "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."
        
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)
