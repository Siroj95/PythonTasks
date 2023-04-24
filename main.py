from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy as db 
from flask_marshmallow import Marshmallow as ma
from sqlalchemy  import func
from PythonTasks.tables import User, Transaction
from PythonTasks.schema import UserSchema, TransactionSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Adventureworks2012.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_schema = UserSchema()
    user = user_schema.load(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.json
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.email = data['email']
    db.session.commit()
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    transaction_schema = TransactionSchema(many=True)
    return jsonify(transaction_schema.dump(transactions))

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    transaction_schema = TransactionSchema()
    transaction = transaction_schema.load(data)
    db.session.add(transaction)
    db.session.commit()
    return jsonify(transaction_schema.dump(transaction))

