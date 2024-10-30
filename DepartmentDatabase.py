import pyodbc

class DepartmentDatabase:
    def __init__(self):
        self.server = 'DESKTOP-5FKBDPA\\SQL2014EXPRESS'
        self.database = 'DBForPython'
        self.conn = pyodbc.connect(r'DRIVER={ODBC Driver 11 for SQL Server};'
        r'SERVER=' + self.server + ';'
        r'DATABASE=' + self.database + ';'
        r'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor() 
    def get_departments(self) -> list:
        query = "SELECT * FROM department"
        self.cursor.execute(query)
        departments = []
        for row in self.cursor.fetchall():
            dept_dict = {}
            dept_dict["id"] = row[0]
            dept_dict["name"] = row[1]
            dept_dict["description"] = row[2]
            print(dept_dict)
            departments.append(dept_dict)
        return departments
    def get_department(self, id) -> dict:
        query = f"SELECT * FROM dbo.department where id = '{id}'"
        self.cursor.execute(query)
        department = {}
        row = self.cursor.fetchone()
        if row!= None:
            department["id"] = row[0]
            department["name"] = row[1]
            department["description"] = row[2]
        return department
    def add_department(self, new_dept):
        query = f"insert into department(name, description) values('{new_dept['name']}','{new_dept['description']}')"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def update_department(self, dept):
        query = f"update department set name = '{dept['name']}', description = '{dept['description']}' where id ='{dept['id']}' "
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def delete_department(self, id):
        query = f"delete from department where id ='{id}'"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()


# deptdb = DepartmentDatabase()
# deptdb.get_departments()