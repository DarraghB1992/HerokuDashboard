from flask import Flask, render_template
from pymongo import MongoClient
import json


app = Flask(__name__)

MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017

MONGODB_URI = 'mongodb://darragh:5nXloxwh@ds049104.mlab.com:49104/heroku_x1p2b3j6'

DBS_NAME = 'heroku_x1p2b3j6'
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False
          }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donorsUS/projects')
def donor_projects():
    connection = MongoClient(MONGODB_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=87000)

    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects



if __name__ == '__main__':
    app.run(debug=True)
