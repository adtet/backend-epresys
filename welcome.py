import flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/welcome', methods=['POST'])
def welcome():
    result = {"message": "welcome"}
    return jsonify(result)


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=4000)
    app.run(port=4000, debug=True)