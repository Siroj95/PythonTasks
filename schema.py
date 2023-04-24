from flask_marshmallow import Marshmallow
from PythonTasks.tables import User, Transaction

ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        model = User

class TransactionSchema(ma.Schema):
    class Meta:
        model = Transaction
