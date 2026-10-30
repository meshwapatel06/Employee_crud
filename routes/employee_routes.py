from fastapi import APIRouter, Response
from models.employee_model import Employee
from controllers.employee_controller import pagination_employee_controller, search_employee,create_employee_controller, get_employee_controller, get_employeeID_controller, delete_employee_controller, update_employee_controller


EmployeeRouter = APIRouter(
    prefix='/employees',   
    tags=['employees']  
)

# Search employee
@EmployeeRouter.get('/search')
def search_employees(search: str, response: Response):
    return search_employee(search, response)

# Create employee
@EmployeeRouter.post('/employees')
def create_employees(employee: Employee, response: Response):
    return create_employee_controller(employee,response)

# Get employee
@EmployeeRouter.get('/employees')
def get_employees(response: Response):
    return get_employee_controller(response)

# Get by ID
@EmployeeRouter.get('/employees/{employeeid}')
def get_employee_by_id(employeeid: int, response: Response):
    return get_employeeID_controller(employeeid, response)

# Delete employee
@EmployeeRouter.delete('/employees/{employeeid}')
def delete_employee(employeeid: int, response: Response):
    return delete_employee_controller(employeeid, response)

# Update employee
@EmployeeRouter.put('/employees/{employeeid}')
def update_employee(employeeid: int, employee: Employee, response: Response):
    return update_employee_controller(employeeid, employee, response)

@EmployeeRouter.get("/pagination")
def pagination_employee(page: int, limit: int, response: Response):
    return pagination_employee_controller(page, limit, response)