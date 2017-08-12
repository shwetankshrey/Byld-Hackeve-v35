from flask import Flask  
app = Flask(__name__)

@app.route("/")
def handle():  
    return "Doesn't matter if the work's incomplete."

if __name__ == "__main__":  
    app.run()