from flask import Flask, request, jsonify
from utils import pred, load_artifacts
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/home")
def hello():
    return "<h1> Hello </h1>"

@app.route("/prediction", methods = ['GET', 'POST'])
def prediction():
    image_data = request.form['image_data']

    response = jsonify(pred(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("starting server")
    load_artifacts()
    app.run(port=5000)
