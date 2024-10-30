from marshmallow import Schema,fields

class GetEmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    salary = fields.Int(required=True)

class GetDepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class GetResponseMessageSchema(Schema):
    message = fields.Str(dump_only=True)