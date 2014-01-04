from flask import Flask, request, jsonify
from storage import Storage


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello,world"


@app.route('/api/search', methods=['PUT'])
def search():
    if request.method == 'PUT':
        search_data = request.get_json(force=True)
        storage = Storage()
        messages = storage.find_messages(search_data)
        return jsonify({'citation': messages})


if __name__ == '__main__':
    app.run(debug=True)
