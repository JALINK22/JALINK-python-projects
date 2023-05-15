

class Employee:


    def __init__(self, name, salary, hire_date):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date


    def get_name(self):
        print("The employee's name is " + self.name)


    def get_salary(self):
        print("This employee's salary is " + self.salary)


    def get_hired_date(self):
        print(self.name + " was hired on " + self.hire_date)

   
class Engineer(Employee):  
    

    def __init__(self, name, salary, hire_date):
        super().__init__(name, salary, hire_date)
        self.name = name
        self.salary = salary
        self.hire_date = hire_date



    
    main_employee = Employee("Jacob Anderson", "10000000", "10.10.10")
    

    main_employee.get_name()
    main_employee.get_salary()
    
    main_employee.get_hired_date()



class Software_Engineer(Engineer, Employee):

    def get_salary(self):
    
        
        print("Sorry, but this employee's salary is private.")
        

Software_engineer_employee = Software_Engineer("Jacob Anderson", "Sorry, but this employee's salary is private.", "10.10.10")
        
    

Software_engineer_employee.get_salary()



class Manager(Employee):

    def __init__(self, job, years, degree):

        self.job = job
        self.years = years 
        self.degree = degree   


    def get_job_description(self):
        print("This employee manages all of the " + self.job)
        

    def years_experience(self):
        print("This employee has " + self.years + " years experience")


    def degree_completed(self):
        print("This employee completed the following degree: " + self.degree)
        print("from Arizona State University")


manager1 = Manager("Software Engineers", "13", "Bachelor in Software Engineering")

manager1.get_job_description()
manager1.years_experience()
manager1.degree_completed()