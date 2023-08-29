from flask import Flask , render_template , request , jsonify

app = Flask(__name__)
app.secret_key = b'\x88\xbc\xb4'


@app.route('/send_name')
def send_name():
    name = "Demo Name"
    return jsonify({'demo':name})
