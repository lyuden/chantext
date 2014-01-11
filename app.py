from flask import Flask, request, jsonify,  render_template
from storage import find_messages,  get_message, update_message,  create_message
from validation import filter_search


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

@app.route("/api/message/<int:mes_id>")
def get_message_response(mes_id):
    if request.method == "GET":
        return jsonify(get_message(mes_id))

    


@app.route('/api/search', methods=['PUT'])
def search():
    if request.method == 'PUT':
        search_data = request.get_json(force=True)
        print(search_data)
        messages = find_messages(filter_search(search_data['words']))
        return jsonify({'citation': messages})


if __name__ == '__main__':
    app.run(debug=True)
