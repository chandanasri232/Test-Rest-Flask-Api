from flask_restful import Resource

Class Home(Resource):
    def get(self):
        return {'Home':"This is home page "}
