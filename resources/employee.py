from flask import Flask, request
from EmployeeDatabase import EmployeeDatabase
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import GetEmployeeSchema
from schemas import GetResponseMessageSchema

eblp = Blueprint("Employee", __name__, description="API to view, add, update, delete")

@eblp.route("/employee")
class Employee(MethodView):
    @eblp.response(200, GetEmployeeSchema(many=True))
    def get(self):
        empData = EmployeeDatabase()
        employeeList = empData.get_employees()
        return employeeList
    @eblp.response(201,GetResponseMessageSchema())
    def post(self):
        new_emp = request.get_json()
        empData = EmployeeDatabase()
        empData.add_employee(new_emp)
        print(new_emp)
        return {'message': 'Employee created successfully'}
    @eblp.response(200,GetResponseMessageSchema())
    def put(self):
        emp = request.get_json()
        empData = EmployeeDatabase()
        empData.update_employee(emp)
        print(emp)
        return {'message': 'Employee updated successfully'}
    @eblp.response(200,GetResponseMessageSchema())
    def delete(self):
        id = request.args.get('id')
        empData = EmployeeDatabase()
        empData.delete_employee(id)
        print(id)
        return {'message': 'Employee deleted successfully'}