class Department:
    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name
department1 = Department(101, "Human Resources")
print(department1.department_name)
department2 = Department(102, "Information Technology")
print(department2.department_name)

class Employee:
    def __init__(self, employee_id, employee_name, department_id, employee_title):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department_id = department_id
        self.employee_title = employee_title
employee1 = Employee(1001, "Sarah Price", 102, "Software Developer")
print(employee1.employee_title, employee1.employee_name)

class Attendance:
    def __init__(self, employee_id, date, clock_in, clock_out, status):
        self.employee_id = employee_id
        self.date = date
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.status = status
attendance1 = Attendance(1001, "09/30/2026", "8:00 AM", "5:00 PM", "Present")
print(attendance1.status, attendance1.date, attendance1.clock_in, attendance1.clock_out)