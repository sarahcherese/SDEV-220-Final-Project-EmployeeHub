class Department:
    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name

class Employee:
    def __init__(self, employee_id, employee_name, department_id, employee_title):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department_id = department_id
        self.employee_title = employee_title

class Attendance:
    def __init__(self, employee_id, date, clock_in, clock_out, status):
        self.employee_id = employee_id
        self.date = date
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.status = status

employees = []
departments = []
def add_employee():
    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name: ")
    department_id = input("Enter Department ID: ")
    employee_title = input("Enter Employee Title: ")
    new_employee = Employee(employee_id, employee_name, department_id, employee_title)
    employees.append(new_employee)
    print("Employee added successfully!")

def view_employees(): 
   for employee in employees:
        print(f"Employee Name: {employee.employee_name}")
        print(f"Employee ID: {employee.employee_id}")
        print(f"Department ID: {employee.department_id}")
        print(f"Employee Title: {employee.employee_title}")

def search_employee():
    search_id = input("Enter Employee ID to search: ")
    for employee in employees:
        if employee.employee_id == search_id:
            print(f"Employee Name: {employee.employee_name}")
            print(f"Employee ID: {employee.employee_id}")
            print(f"Department ID: {employee.department_id}")
            print(f"Employee Title: {employee.employee_title}")
            return
    print("Employee not found.")
def update_employee():
    update_id = input("Enter Employee ID to update: ")
    for employee in employees:
        if employee.employee_id == update_id:
            employee.employee_name = input("Enter new Employee Name: ")
            employee.department_id = input("Enter new Department ID: ")
            employee.employee_title = input("Enter new Employee Title: ")
            print("Employee updated successfully!")
            return
    print("Employee not found.")
def remove_employee():
    remove_id = input("Enter Employee ID to remove: ")
    for employee in employees:
        if employee.employee_id == remove_id:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
    print("Employee not found.")
def add_department():
    department_id = input("Enter Department ID: ")
    department_name = input("Enter Department Name: ")
    new_department = Department(department_id, department_name)
    departments.append(new_department)
    print("Department added successfully!")
def view_departments():
    for department in departments:
        print(f"Department ID: {department.department_id}")
        print(f"Department Name: {department.department_name}")
add_employee()
add_employee()
view_employees()
search_employee()
update_employee()
remove_employee()
view_employees()
add_department()
view_departments()