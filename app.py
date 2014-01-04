from flask import Flask, request, jsonify
from storage import find_messages


app = Flask(__name__)


def to_db(value):
    with open('database.txt', 'w') as db:
        db.write(value)


def get_from_db():
    with open('database.txt') as db:
        data = db.read()
    return data


@app.route('/')
def index():
    return "Hello,world"


@app.route('/api',  methods=['GET', 'PUT'])
def api():
    if request.method == 'GET':
        return jsonify({"data": get_from_db()})
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        to_db(data['key'])
        return jsonify({"status": "Data updated"})


@app.route('/api/search', methods=['PUT'])
def search():
    if request.method == 'PUT':
        search_data = request.get_json(force=True)
        messages = find_messages(search_data)
        return jsonify({'citation': messages})


if __name__ == '__main__':
    app.run(debug=True)
