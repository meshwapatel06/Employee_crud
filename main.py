from fastapi import FastAPI
from routes.employee_routes import EmployeeRouter

app = FastAPI()
app.include_router(EmployeeRouter)