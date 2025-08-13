from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/committees')
def committees():
    return render_template('committees.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/incubator')
def incubator():
    return render_template('incubator.html')

@app.route('/secretariat')
def secretariat():
    return render_template('secretariat.html')

if __name__ == '__main__':
    app.run(debug=True)
