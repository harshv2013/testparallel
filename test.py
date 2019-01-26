from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)




@app.route('/', methods=['POST'])
def hello_world():

    a = request.form.get('name')
    b = request.form.get('email')
    return jsonify({ 'name': a,'email':b})



if __name__ == "__main__":
    app.run(debug=True)