from flask import Flask, request
from ProjectDatabase import ProjectDatabase

def get_projects():
    projData = ProjectDatabase()
    ProjectList = projData.get_projects()
    return ProjectList

def get_project(id):
    projData = ProjectDatabase()
    ProjectList = projData.get_project(id)
    return ProjectList

def post_project():
    new_proj = request.get_json()
    projData = ProjectDatabase()
    projData.add_project(new_proj)
    print(new_proj)
    return {'message': 'Project created successfully'}

def put_project():
    proj = request.get_json()
    projData = ProjectDatabase()
    projData.update_project(proj)
    print(proj)
    return {'message': 'Project updated successfully'}

def delete_project(project_id):
    projData = ProjectDatabase()
    projData.delete_project(project_id)
    print(project_id)
    return {'message': 'Project deleted successfully'}