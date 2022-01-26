from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template
import requests
from googletrans import Translator

app = Flask(__name__, template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

translator = Translator(service_urls=['translate.googleapis.com'])
old_mess = ""


@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")


@app.route("/api", methods=['POST'])
@cross_origin()
def main():
    global old_mess
    contents = request.json
    webhook = "https://discord.com/api/webhooks/935794459839459338/q13g2ISGnr5WfOxdAqyAZ3_u5fDW5CwHDX-bSrpQL7eW0jB61BzZBnmHI1-HroEZUNMf"
    username = "Stupid bot"
    avatar_url = "https://pics.me.me/lm-a-stupid-bot-me-irl-34192545.png"
    # content = contents["content"] + \
    #    " ||Sent by https://dinhgiabao.codes/control_agof.html||"
    content = contents["content"]

    trans = translator.translate(content, dest="en")
    content = trans.text

    result = content.lower()

    #swearing = ["fuck", "dm", "mje", "ƒuck",
    #            "|<", "|=", "dit", "xuka blyat", "djt", "d1t", "dpt", "lon", "@hat suck", "hat suck", "f#ck", "địt", "lồn", "bitch", "fck", "f*ck","f u c k","b i t c h"]

    swearing =["hat","h a t","h at", "ha t"]
    for word in swearing:
        if word in result:
            content ="Hat insult detect :)"

    data = {'username': username,
            'avatar_url': avatar_url,
            'content': content, }

    if(old_mess != contents["content"]):
        r = requests.post(url=webhook, data=data)

    old_mess = contents["content"]
    return "ok"


if __name__ == '__main__':
    app.run()
