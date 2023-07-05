from flask import Flask
from flask_cors import CORS 
import stt as stt

app=Flask(__name__)
CORS(app)

@app.route("/api/home", methods=['GET'])
def return_home():
    return stt.data()   

if __name__ == "__main__":
    app.run(debug=True, port=8080)

    