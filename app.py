from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #host='0.0.0.0' accetta connessioni da qualsiasi ip
    #port=5000 porta su cui il server rimane in ascolto
