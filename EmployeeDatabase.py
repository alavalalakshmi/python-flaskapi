import pyodbc

class EmployeeDatabase:
    def __init__(self):
        self.server = 'DESKTOP-5FKBDPA\\SQL2014EXPRESS'
        self.database = 'DBForPython'
        self.conn = pyodbc.connect(r'DRIVER={ODBC Driver 11 for SQL Server};'
        r'SERVER=' + self.server + ';'
        r'DATABASE=' + self.database + ';'
        r'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor() 
    def get_employees(self) -> list:
        query = "SELECT * FROM employee"
        self.cursor.execute(query)
        employees = []
        for row in self.cursor.fetchall():
            emp_dict = {}
            emp_dict["id"] = row[0]
            emp_dict["name"] = row[1]
            emp_dict["salary"] = row[2]
            print(emp_dict)
            employees.append(emp_dict)
        return employees
    def add_employee(self, new_emp):
        query = f"insert into employee(name, salary) values('{new_emp['name']}','{new_emp['salary']}')"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def update_employee(self, emp):
        query = f"update employee set name = '{emp['name']}', salary = '{emp['salary']}' where id ='{emp['id']}' "
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
    def delete_employee(self, id):
        query = f"delete from employee where id ='{id}'"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()


# empdb = EmployeeDatabase()
# empdb.get_employees()