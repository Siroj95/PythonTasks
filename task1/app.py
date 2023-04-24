from flask import Flask, request
from flask_restful import Resource, Api
from utils import fibonacci, save_fibonacci_number
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class Fibonacci(Resource):
    def get(self, n: int):

        result = fibonacci(n)
        save_fibonacci_number(n, result)
        return result

api.add_resource(Fibonacci, '/fibonacci/<int:n>')

if __name__ == '__main__':
    app.run(debug=True)
