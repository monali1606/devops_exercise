from flask import Flask
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    #clock=str(datetime.now())
    data={"message":"hello from containerB"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')