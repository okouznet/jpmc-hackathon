from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        mac_address = request.form.get('macaddress')
        song = request.form.get('song')
        print(mac_address, song)
        #backend prsocessing
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
