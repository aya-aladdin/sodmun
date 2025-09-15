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
    committees = [
        {
            'name': 'The First General Assembly',
            'chairs': '???',
            'img': 'my-img/ga1.png'
        },
        {
            'name': 'United Nations Human Rights Council',
            'chairs': '???',
            'img': 'my-img/hrc.png'
        },
        {
            'name': 'United Nations Security Council',
            'chairs': '???',
            'img': 'my-img/sc.png'
        },
        {
            'name': 'Economic & Social Council',
            'chairs': '???',
            'img': 'my-img/ecosoc.png'
        },
        {
            'name': 'UNCSW',
            'chairs': '???',
            'img': 'my-img/csw.png'
        },
        {
            'name': 'International Court of Justice',
            'chairs': '???',
            'img': 'my-img/icj.png'
        },
        {
            'name': 'UN Environment Programme',
            'chairs': '???',
            'img': 'my-img/sc.png'
        },
        {
            'name': 'UN Development Programme',
            'chairs': '???',
            'img': 'my-img/ecosoc.png'
        },
        {
            'name': 'UNESCO',
            'chairs': '???',
            'img': 'my-img/caie.png'
        },
        {
            'name': 'Futuristic Crisis Committee',
            'chairs': '???',
            'img': 'my-img/fcc.png'
        },
        {
            'name': 'International Monetary Fund',
            'chairs': '???',
            'img': 'my-img/imf.png'
        },
        {
            'name': 'Office on Drugs and Crime (Jr)',
            'chairs': '???',
            'img': 'my-img/unodc.png'
        },
        {
            'name': 'Formula 1',
            'chairs': '???',
            'img': 'my-img/f1.png'
        },
        {
            'name': 'Clash Royale Committee',
            'chairs': '???',
            'img': 'my-img/crc.png'
        },
        {
            'name': 'Organization of Music Artists',
            'chairs': '???',
            'img': 'my-img/oma.png'
        },
        {
            'name': 'Crisis Space Council',
            'chairs': '???',
            'img': 'my-img/csc.png'
        },
        {
            'name': 'Council on AI Ethics',
            'chairs': '???',
            'img': 'my-img/caie.png'
        },
        {
            'name': 'The White House',
            'chairs': '???',
            'img': 'my-img/twh.png'
        }
    ]
    return render_template('committees.html', committees=committees)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/incubator')
def incubator():
    return render_template('incubator.html')

@app.route('/secretariat')
def secretariat():
    return render_template('secretariat.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
