from flask import Flask, request
from DepartmentDatabase import DepartmentDatabase
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import GetDepartmentSchema
from schemas import GetResponseMessageSchema

dblp = Blueprint("Department", __name__, description="API to view, add, update, delete")

@dblp.route("/department")
class Department(MethodView):
    @dblp.response(200, GetDepartmentSchema(many=True))
    def get(self):
        deptData = DepartmentDatabase()
        departmentList = deptData.get_departments()
        return departmentList
    @dblp.response(201,GetResponseMessageSchema())
    def post(self):
        new_dept = request.get_json()
        deptData = DepartmentDatabase()
        deptData.add_department(new_dept)
        print(new_dept)
        return {'message': 'Department created successfully'}
    @dblp.response(200,GetResponseMessageSchema())
    def put(self):
        dept = request.get_json()
        deptData = DepartmentDatabase()
        deptData.update_department(dept)
        print(dept)
        return {'message': 'Department updated successfully'}
    
@dblp.route('/department/<int:id>')
class DepartmentParameterized(MethodView):
    def get(self, id):
        deptData = DepartmentDatabase()
        dept = deptData.get_department(id)
        return dept
    def delete(self,id):
        deptData = DepartmentDatabase()
        deptData.delete_department(id)
        print(id)
        return {'message': 'Department deleted successfully'}