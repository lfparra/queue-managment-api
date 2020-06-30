import os
from flask import Flask, request, jsonify, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Queue

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = os.environ.get('DEBUG')
app.config['ENV'] = os.environ.get('ENV')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
CORS(app)

queue = Queue()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/new', methods=['POST'])
def new_item():
    return jsonify({"msg" : "Hola desde new item"})

@app.route('/next', methods=['GET'])
def next_item():
    pass

@app.route('/all', methods=['GET'])
def all_items():
    res = queue.size()
    return jsonify({"msg" : f"Largo de la lista es {res}"})

if __name__ == '__main__':
    manager.run()