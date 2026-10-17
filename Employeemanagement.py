import tkinter as tk
from tkinter import messagebox
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
attendance_records = []
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
def record_attendance():
    employee_id = input("Enter Employee ID: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    clock_in = input("Enter Clock In Time (HH:MM): ")
    clock_out = input("Enter Clock Out Time (HH:MM): ")
    status = input("Enter Attendance Status (Present/Absent): ")
    new_attendance = Attendance(employee_id, date, clock_in, clock_out, status)
    attendance_records.append(new_attendance)
    print("Attendance recorded successfully!")
# add_employee()
# add_employee()
# view_employees()
# search_employee()
# update_employee()
# record_attendance()
# remove_employee()
# view_employees()
# add_department()
# view_departments()
def open_add_employee():
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")
    add_window.geometry("400x300")
    tk.Label(add_window, text="Employee ID:").pack()
    employee_id_entry = tk.Entry(add_window)
    employee_id_entry.pack()
    tk.Label(add_window, text="Employee Name:").pack()
    employee_name_entry = tk.Entry(add_window)
    employee_name_entry.pack()
    tk.Label(add_window, text="Department ID:").pack()
    department_id_entry = tk.Entry(add_window)
    department_id_entry.pack()
    tk.Label(add_window, text="Employee Title:").pack()
    employee_title_entry = tk.Entry(add_window)
    employee_title_entry.pack()
    
    def save_employee():
        employee_id = employee_id_entry.get()
        employee_name = employee_name_entry.get()
        department_id = department_id_entry.get()
        employee_title = employee_title_entry.get()
        
        new_employee = Employee(employee_id, employee_name, department_id, employee_title)
        employees.append(new_employee)
        messagebox.showinfo("Success", "Employee added successfully!")
        add_window.destroy()
    save_button = tk.Button(add_window, text="Save Employee", command=save_employee)
    save_button.pack(pady=10)
def open_view_employees():
    view_window = tk.Toplevel(root)
    view_window.title("View Employees")
    view_window.geometry("400x300")
    for employee in employees:
        employee_info = f"ID: {employee.employee_id}, Name: {employee.employee_name}, Department ID: {employee.department_id}, Title: {employee.employee_title}"
        tk.Label(view_window, text=employee_info).pack()
def open_search_employee():
    search_window = tk.Toplevel(root)
    search_window.title("Search Employee")
    search_window.geometry("400x200")
    tk.Label(search_window, text="Enter Employee ID:").pack()
    search_id_entry = tk.Entry(search_window)
    search_id_entry.pack()
    
    def search():
        search_id = search_id_entry.get()
        for employee in employees:
            if employee.employee_id == search_id:
                employee_info = f"ID: {employee.employee_id}, Name: {employee.employee_name}, Department ID: {employee.department_id}, Title: {employee.employee_title}"
                messagebox.showinfo("Employee Found", employee_info)
                return
        messagebox.showerror("Error", "Employee not found.")
    
    search_button = tk.Button(search_window, text="Search", command=search)
    search_button.pack(pady=10)
def open_update_employee():
    update_window = tk.Toplevel(root)
    update_window.title("Update Employee")
    update_window.geometry("400x300")
    tk.Label(update_window, text="Enter Employee ID to Update:").pack()
    update_id_entry = tk.Entry(update_window)
    update_id_entry.pack()
    
    def load_employee():
        update_id = update_id_entry.get()
        for employee in employees:
            if employee.employee_id == update_id:
                tk.Label(update_window, text="New Employee Name:").pack()
                employee_name_entry = tk.Entry(update_window)
                employee_name_entry.insert(0, employee.employee_name)
                employee_name_entry.pack()
                
                tk.Label(update_window, text="New Department ID:").pack()
                department_id_entry = tk.Entry(update_window)
                department_id_entry.insert(0, employee.department_id)
                department_id_entry.pack()
                
                tk.Label(update_window, text="New Employee Title:").pack()
                employee_title_entry = tk.Entry(update_window)
                employee_title_entry.insert(0, employee.employee_title)
                employee_title_entry.pack()
                
                def save_updates():
                    employee.employee_name = employee_name_entry.get()
                    employee.department_id = department_id_entry.get()
                    employee.employee_title = employee_title_entry.get()
                    messagebox.showinfo("Success", "Employee updated successfully!")
                    update_window.destroy()
                
                save_button = tk.Button(update_window, text="Save Updates", command=save_updates)
                save_button.pack(pady=10)
                return
        messagebox.showerror("Error", "Employee not found.")
    
    load_button = tk.Button(update_window, text="Load Employee", command=load_employee)
    load_button.pack(pady=10)
def open_remove_employee():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Employee")
    remove_window.geometry("400x200")
    tk.Label(remove_window, text="Enter Employee ID to Remove:").pack()
    remove_id_entry = tk.Entry(remove_window)
    remove_id_entry.pack()
    
    def remove():
        remove_id = remove_id_entry.get()
        for employee in employees:
            if employee.employee_id == remove_id:
                employees.remove(employee)
                messagebox.showinfo("Success", "Employee removed successfully!")
                remove_window.destroy()
                return
        messagebox.showerror("Error", "Employee not found.")
    
    remove_button = tk.Button(remove_window, text="Remove", command=remove)
    remove_button.pack(pady=10)
def open_add_department():
    department_window = tk.Toplevel(root)
    department_window.title("Add Department")
    department_window.geometry("400x300")
    tk.Label(department_window, text="Department ID:").pack()
    department_id_entry = tk.Entry(department_window)
    department_id_entry.pack()

    tk.Label(department_window, text="Department Name:").pack()
    department_name_entry = tk.Entry(department_window)
    department_name_entry.pack()
    def save_department():
        department_id = department_id_entry.get()
        department_name = department_name_entry.get()
        new_department = Department(department_id, department_name)
        departments.append(new_department)
        messagebox.showinfo("Success", "Department added successfully!")
        department_window.destroy()
    save_button = tk.Button(department_window, text="Save Department", command=save_department)
    save_button.pack(pady=10)
def open_view_departments():
    view_window = tk.Toplevel(root)
    view_window.title("View Departments")
    view_window.geometry("400x300")
    for department in departments:
        department_info = f"ID: {department.department_id}, Name: {department.department_name}"
        tk.Label(view_window, text=department_info).pack()
def open_record_attendance():
    attendance_window = tk.Toplevel(root)
    attendance_window.title("Record Attendance")
    attendance_window.geometry("400x400")
    tk.Label(attendance_window, text="Employee ID:").pack()
    employee_id_entry = tk.Entry(attendance_window)
    employee_id_entry.pack()
    
    tk.Label(attendance_window, text="Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(attendance_window)
    date_entry.pack()
    
    tk.Label(attendance_window, text="Clock In Time (HH:MM):").pack()
    clock_in_entry = tk.Entry(attendance_window)
    clock_in_entry.pack()
    
    tk.Label(attendance_window, text="Clock Out Time (HH:MM):").pack()
    clock_out_entry = tk.Entry(attendance_window)
    clock_out_entry.pack()
    
    tk.Label(attendance_window, text="Attendance Status (Present/Absent):").pack()
    status_entry = tk.Entry(attendance_window)
    status_entry.pack()
    
    def save_attendance():
        employee_id = employee_id_entry.get()
        date = date_entry.get()
        clock_in = clock_in_entry.get()
        clock_out = clock_out_entry.get()
        status = status_entry.get()
        
        new_attendance = Attendance(employee_id, date, clock_in, clock_out, status)
        attendance_records.append(new_attendance)
        messagebox.showinfo("Success", "Attendance recorded successfully!")
        attendance_window.destroy()
    
    save_button = tk.Button(attendance_window, text="Save Attendance", command=save_attendance)
    save_button.pack(pady=10)
def open_view_attendance():
    view_window = tk.Toplevel(root)
    view_window.title("View Attendance")
    view_window.geometry("600x400")

    for record in attendance_records:
        attendance_info = f"Employee ID: {record.employee_id}, Date: {record.date}, Clock In: {record.clock_in}, Clock Out: {record.clock_out}, Status: {record.status}"
        tk.Label(view_window, text=attendance_info).pack()
root = tk.Tk()
root.title("EmployeeHub - Employee Management System")
root.geometry("800x600")
title_label = tk.Label(root, text="Welcome to EmployeeHub", font=("Arial", 24, "bold"))
title_label.pack(pady=20)
add_button = tk.Button(root, text="Add Employee", command=open_add_employee)
add_button.pack(pady=10)

view_button = tk.Button(root, text="View Employees", command=open_view_employees)
view_button.pack(pady=10)

update_button = tk.Button(root, text="Update Employee", command=open_update_employee)
update_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Employee", command=open_remove_employee)
remove_button.pack(pady=10)

search_button = tk.Button(root, text="Search Employee", command=open_search_employee)
search_button.pack(pady=10)

add_department_button = tk.Button(root, text="Add Department", command=open_add_department)
add_department_button.pack(pady=10)

view_department_button = tk.Button(root, text="View Departments", command=open_view_departments)
view_department_button.pack(pady=10)

attendance_button = tk.Button(root, text="Record Attendance", command=open_record_attendance)
attendance_button.pack(pady=10)

view_attendance_button = tk.Button(root, text="View Attendance", command=open_view_attendance)
view_attendance_button.pack(pady=10)

root.mainloop()