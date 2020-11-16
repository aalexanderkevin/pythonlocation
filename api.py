from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import psycopg2

# Initialize Flask
app = Flask(__name__)
api = Api(app)
# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('latitude')
parser.add_argument('longitude')

class Location(Resource):

    def get(self):
        args = parser.parse_args()

        latitude = args['latitude']
        longitude = args['longitude']
        connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="host.docker.internal",
                                port="5432",
                                database="geocoding")
        try:
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM location WHERE latitude=" + latitude + " AND longitude=" + longitude
            cursor.execute(postgreSQL_select_Query)
            result = cursor.fetchall()
            return{"location": result[0][2], "status": result[0][3]}

        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

        finally:
            if(connection):
                cursor.close()
                connection.close()

class Coordinate(Resource):

    def get(self, name):
        connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="host.docker.internal",
                                port="5432",
                                database="geocoding")
        try:
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM location WHERE name ='" + name + "'"
            
            cursor.execute(postgreSQL_select_Query)
            result = cursor.fetchall()
            return{"latitude": result[0][1], "longitude": result[0][1], "location": result[0][2]}

        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

        finally:
            if(connection):
                cursor.close()
                connection.close()

api.add_resource(Coordinate, "/api/coordinate/<string:name>")
api.add_resource(Location, "/api/location")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

