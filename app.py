from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        return jsonify(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
