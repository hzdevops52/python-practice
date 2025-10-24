#class
class employees:
    company = 'abc.pvt'
    
    #constructor
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept 
        self.salary = salary
     
     #method   
    def emp_info(self):
            print(f'Name is {self.name}')
            print(f'email is {self.email}')
            print(f'dept is {self.dept}')
            print(f'salary is {self.salary}')
          
    def change_dept(self, new_dept):
            self.dept = new_dept
            print(f'dept cahnged to {new_dept}')
            
            
#object      
emp1 = employees('hassan', 'hz@email.com', 'it', 50000)        
emp2 = employees('ali', 'ali@email.com', 'cs', 60000) 

#print(emp1.email)
#print(emp2.email)

emp2.emp_info()
emp2.change_dept("DevOPs")
print(employees.company)