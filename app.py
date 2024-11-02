from flask import Flask
from resources.employee import eblp as EmployeeBluePrint
from resources.department import dblp as DepartmentBluePrint
from resources.project import get_projects,post_project,put_project,delete_project,get_project
from flask_smorest import Api
from flask_restful import Api as api_restful, Resource
# from fastapi import FastAPI

app = Flask(__name__)

# fastapi_app = FastAPI()

# app.register_blueprint(fastapi_app)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Employee API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)
api.register_blueprint(EmployeeBluePrint)
api.register_blueprint(DepartmentBluePrint)

# flask API routes end points to access
@app.route('/projects')
def get_projects_wrapper():
    return get_projects()

@app.route('/projects/<int:project_id>')
def get_project_wrapper(project_id):
    return get_project(project_id)

@app.route('/projects', methods=['POST'])
def post_project_wrapper():
    return post_project()

@app.route('/projects', methods=['PUT'])
def put_project_wrapper():
    return put_project()

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project_wrapper(project_id):
    return delete_project(project_id)

#fast API routes
# @fastapi_app.get("/hello")
# def read_root():
#     return {"Hello": "World"}
    
if __name__ == '__main__':
    app.run()
    # app.run(debug=True, host='0.0.0.0')


# cmd to run flask api project 
# python app.py