from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*.*"}})

# ROTAS

@app.route("/", methods=['GET']) 
@cross_origin()
def home(): 
    return jsonify({
        "api": "API FLASK",
        "version": "1.0.0"
    })
    
@app.route("/upload", methods=['POST']) 
@cross_origin()
def upload(): 
    js = request.get_json()
    print(js)
    return jsonify(js)
    

    
if __name__ == '__main__':
    app.run(debug=True, port=5001)