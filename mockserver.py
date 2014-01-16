from flask import Flask, request, jsonify,  render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/message',  methods=['PUT', ])
def api():
    if request.method == 'PUT':
        return jsonify({"status": "Message created"})

@app.route("/api/message/<int:mes_id>")
def get_message_response(mes_id):
    if request.method == "GET":

        if mes_id == 1:
            return jsonify({'id':1,
                            'message':  'First message'
                        })

        if mes_id == 2:
            return jsonify({'id':1,
                            'message':  'Second message citing fist >>1{3:10} end of second message'
                        })

        if mes_id == 3:
            return jsonify({'id':1,
                            'message':  'Third message citing second >>2{1:14} end of third'
                        })

        if mes_id == 4:
            return jsonify({'id':1,
                            'message':  'Fourth message citing first >>1{1:3} end of fourth'
                        })

        if mes_id == 5:
            return jsonify({'id':5,
                            'message':  'Fifth message citing first >>1{1:3}  and fourth  >>4{1:20} end of fifth'
                        })


@app.route('/api/search', methods=['PUT'])
def search():
    if request.method == 'PUT':
        return jsonify({'citation': [1, 2, 3, 4, 5]})


if __name__ == '__main__':
    app.run(debug=True)
