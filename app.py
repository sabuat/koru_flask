import gspread
from flask import Flask, render_template,request

gc = gspread.service_account(filename='koru-flask.json')
sp = gc.open('contactos_aquarelas')

spContacts = sp.get_worksheet(0)

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        spContacts.append_row([request.form['Nome'],request.form['Email'], request.form['menssagem']])

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/store')
def store():
    return render_template('store.html')

if __name__ == "__main__":
    app.run(debug=True)