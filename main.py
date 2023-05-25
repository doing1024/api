from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = a + b
    response = {
        'result': result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
