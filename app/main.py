from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is an update that will be deployed in a bit by the CI-CD pipeline (:"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
