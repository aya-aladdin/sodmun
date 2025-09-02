from flask import Flask, render_template, request, jsonify
import openai
import os

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
            'name': 'UN Human Rights Council',
            'chairs': '???',
            'img': 'my-img/hrc.png'
        },
        {
            'name': 'UNCSW',
            'chairs': '???',
            'img': 'my-img/csw.png'
        },
        {
            'name': 'International Court of Justice ',
            'chairs': '???',
            'img': 'my-img/icj.png'
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
            'name': 'Formula 1 ',
            'chairs': '???',
            'img': 'my-img/f1.png'
        },
        {
            'name': 'Clash Royale Committee ',
            'chairs': '???',
            'img': 'my-img/crc.png'
        },
        {
            'name': 'Organization of Music Artists ',
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY", "FINAL_KEY_SHOULD_GO_HERE")

SODMUN_INFO_TEXT = """
SODMUN III (Oct 17–19, 2025) is the Largest Private Teen-Led MUN Conference with 500+ participants.
About: Made by MUNers for MUNers, helping delegates, chairs, and secretariat grow.
Team: Vishesh Shah, Andre Chitongco, Rayan Hussain, Vedant Katara, Aarav Mamtani, Pranav Nair.
Committees: GA1, UN Security Council, Economic & Social Council, UNHRC, UNCSW, ICJ, IMF, F1, Clash Royale Committee, Organization of Music Artists, Crisis Space Council, Council on AI Ethics, The White House.
Contact: sg.sodmun@gmail.com, vishesh@sodmun.com, Instagram @sod.mun, delegate applications and registration are out click below
"""

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "⚠️ Please type a message."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant trained on SODMUN information."},
                {"role": "user", "content": SODMUN_INFO_TEXT + "\nUser asks: " + user_message}
            ],
            max_tokens=400
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "⚠️ Error connecting to OpenAI API."})

if __name__ == "__main__":
    app.run(debug=True)
