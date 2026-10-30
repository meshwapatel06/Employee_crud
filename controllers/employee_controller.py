from fastapi import APIRouter, Response
from models.employee_model import Employee


employees = []
id = 0


## BONUS : Search student
def search_employee(search: str, response: Response):
    try:
        response.status_code = 200
        search = search.lower()

        result = [
            employee for employee in employees
            if search in str(employee.id).lower()
            or search in employee.name.lower()
            or search in employee.email.lower()
            or search in employee.department.lower()
            or search in str(employee.salary).lower()
        ]

        if result:
            return {'isSuccess': True,'message': 'Employees found','employee': result}
        return {'isSuccess': False,'message': 'No employee found','employee': []}

    except Exception as e:
            print(e)
            response.status_code = 500
            return {'isSuccess': False,'message':str(e)}

### Create employee
def create_employee_controller(employee: Employee, response: Response):
    global id
    try:
        id+=1
        employee.id = id
        employees.append(employee)
        response.status_code = 201
        return {'isSuccess':True, 'message':'Employee created successfully','employee':employee}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message':str(e)}
    

### Get employee
def get_employee_controller(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'Employee Display Successfully', 'employees': employees}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}

### Get by ID
def get_employeeID_controller(employeeid: int, response: Response):
    try:
        response.status_code = 200
        for employee in employees:
            if employee.id == employeeid:
                return {'isSuccess':True,  'employee': employee}

        response.status_code = 404
        return {'message' : 'Employee not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}


### Delete employee
def delete_employee_controller(employeeid:int, response:Response):
    try:
        response.status_code = 200
        for employee in employees:
            if employee.id == employeeid:
                employees.remove(employee)
                return {'isSuccess' : True, 'messege' : 'Employee deleted successfully'}
        response.status_code = 404
        return {'message' : 'Employee not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}


### Update employee
def update_employee_controller(employeeid: int, employee: Employee, response: Response):
    try:
        response.status_code = 200

        for e in employees:
            if e.id == employeeid:
                e.name = employee.name
                e.email = employee.email
                e.department = employee.department
                e.salary = employee.salary

                return {'isSuccess': True,'message': 'Employee updated successfully','employee': e}

        response.status_code = 404
        return {'message': 'Employee not found','isSuccess': False}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message': 'Error updating Employee'}


### Pagination
def pagination_employee_controller(page: int, limit: int, response: Response):
    try:
        start = (page - 1) * limit
        end = start + limit

        result = employees[start:end]
        response.status_code = 200
        return {'isSuccess': True,'message': 'Employees displayed successfully','page': page,'limit': limit,'employee': result}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message': str(e)}


