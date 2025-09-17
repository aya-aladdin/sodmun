from flask import Flask, render_template, request, jsonify
import os
import json
import urllib.request

app = Flask(__name__)

SODMUN_INFO_TEXT = """
SODMUN III (Oct 17–19, 2025) is the Largest Private Teen-Led MUN Conference with 500+ participants.
About: Made by MUNers for MUNers, helping delegates, chairs, and secretariat grow.
Team: Vishesh Shah, Andre Chitongco, Rayan Hussain, Vedant Katara, Aarav Mamtani, Pranav Nair.
Committees: GA1, UN Security Council, Economic & Social Council, UNHRC, UNCSW, ICJ, IMF, F1, Clash Royale Committee, Organization of Music Artists, Crisis Space Council, Council on AI Ethics, The White House.
Contact: sg.sodmun@gmail.com, vishesh@sodmun.com, Instagram @sod.mun, delegate applications and registration are out click below
"""


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

@app.route('/helpbot')
def helpbot():
    return render_template('helpbot.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "⚠️ Please type a message."})

    try:
        req = urllib.request.Request(
            "https://ai.hackclub.com/chat/completions",
            data=json.dumps({
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are SODDY, a helpful assistant for SODMUN (summit of diplomacy mun). Your responses must be concise, straightforward, and delivered as the final answer only. Do not include any reasoning, thoughts, or conversational filler. Your responses should be in Markdown format. Always include the registration link: [Delegate Applications & Registration](https://sodmun.com/index.html)"
                    },
                    {
                        "role": "user",
                        "content": SODMUN_INFO_TEXT + "\n" + user_message
                    }
                ],
                "max_tokens": 400
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                response_data = json.loads(response.read().decode('utf-8'))
                reply = response_data['choices'][0]['message']['content']
                
                return jsonify({"reply": reply})
            else:
                return jsonify({"reply": "⚠️ Error connecting to Hack Club AI API."})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "⚠️ Error connecting to Hack Club AI API."})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
