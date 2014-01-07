from flask import Flask, request, jsonify,  render_template
from storage import find_messages,  get_message, update_message,  create_message



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/message',  methods=['PUT', ])
def api():
    if request.method == 'PUT':
        data = request.get_json(force=True)
        create_message(data['key'])
        return jsonify({"status": "Message created"})



@app.route('/api/search', methods=['PUT'])
def search():
    if request.method == 'PUT':
        search_data = request.get_json(force=True)
        print(search_data)
        messages = find_messages(search_data['words'])
        return jsonify({'citation': messages})


if __name__ == '__main__':
    app.run(debug=True)
