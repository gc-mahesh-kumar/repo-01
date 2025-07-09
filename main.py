from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello World from Google Cloud - Automated Deployment - Cloud Run +  Cloud Build</h1>"

@app.route("/version")
def version():
  return "Helloworld 2.0\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)