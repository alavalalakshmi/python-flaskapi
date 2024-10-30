import pyodbc

class ProjectDatabase:
    def __init__(self):
        self.server = 'DESKTOP-5FKBDPA\\SQL2014EXPRESS'
        self.database = 'DBForPython'
        self.conn = pyodbc.connect(r'DRIVER={ODBC Driver 11 for SQL Server};'
        r'SERVER=' + self.server + ';'
        r'DATABASE=' + self.database + ';'
        r'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor() 
    def get_projects(self) -> list:
        query = "SELECT * FROM dbo.project"
        self.cursor.execute(query)
        projects = []
        for row in self.cursor.fetchall():
            proj_dict = {}
            proj_dict["id"] = row[0]
            proj_dict["name"] = row[1]
            proj_dict["description"] = row[2]
            print(proj_dict)
            projects.append(proj_dict)
        return projects
    def get_project(self, id) -> dict:
        query = f"SELECT * FROM dbo.project where id = '{id}'"
        self.cursor.execute(query)
        project = {}
        row = self.cursor.fetchone()
        if row!= None:
            project["id"] = row[0]
            project["name"] = row[1]
            project["description"] = row[2]
        return project
    def add_project(self, new_proj):
        query = f"insert into project(name, description) values('{new_proj['name']}','{new_proj['description']}')"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def update_project(self, proj):
        query = f"update project set name = '{proj['name']}', description = '{proj['description']}' where id ='{proj['id']}' "
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def delete_project(self, id):
        query = f"delete from project where id ='{id}'"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()


# projdb = ProjectDatabase()
# projdb.get_projects()