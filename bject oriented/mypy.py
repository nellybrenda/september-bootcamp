class PayrollSystem():

    def __init__(self, id, name,monthly_salary):
      self.id  =id
      self.name = name
      self.monthly_salary = monthly_salary
     
class Employee():
    def __init__(self, id, name):
        self.id = id
        self.name = name 
class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
          self.id  =id
          self.name = name
          self.monthly_salary = monthly_salary  
          
        
        #creating methods - functions that are related

    def SalaryEmployee(self):
        return self.SalaryEmployee

        if monthly_salary in range(0,24000):
           return  tax  (0.1 * 24000)

        elif (monthly_salary in range(24001, 40667)):
          return  tax  (0.15 * (40667-24000)+(0.1 * 24000))

        elif (monthly_salary in range(40668,57333)):
          return  tax  (0.20*(57333-40667)+(0.1 * 24000)+(0.15 * (40667-24000))

        elif (monthly_salary >= 57333):
          return  tax  (0.25*(monthly_salary-57333)+(0.1 * 24000)+0.15 * (40667-24000)+0.20*(57333-40667))
        else:
            
          return tax
          