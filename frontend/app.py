from flask import Flask , render_template , jsonify , request , session
import requests

app = Flask(__name__)
app.secret_key = b'\x88\xbc\xb4'

@app.route('/')
def index():
    return render_template('index.html',name="Hello")

@app.route('/get_name_from_bakcend')
def get_name_from_bakcend():
    domain_link='http://127.0.0.1:8000'
    data = requests.get(domain_link + '/send_name')
    return jsonify({'name':data.json()['demo']})
