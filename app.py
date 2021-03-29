from flask import Flask, request
from linebot import *
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('Lb5v+X5Hr1gdHa+6yFkWcxpPLlfCXVMqG+QXUIvjCN0HmftdNNl8NixyyDBmOGzVjNGzNGiB2koW10I8SEzSxijriRGZR1/G9n6FgqDvsLXrT2h++Y8LyYUYGadiOGixYj30nBHYnRAXwRmpdiU2FAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('97ea021104b6a2182af981ae780d0fb0')

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route("/calltae", methods=['POST'])
def calltae():
    body = request.get_json(silent=True, force=True)
    text_file = open("sample.txt", "w")
    n = text_file.write(body["number"])
    x = text_file.write(body["text"])
    text_file.close()
    print(body["number"])
    print(body["text"])
    return body

@app.route("/callback", methods=['POST'])
def callback():
    # body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'
 

def reply(intent,text,reply_token,id,disname):
    if intent == 'intent 3':
        text_message = TextSendMessage(text="Hello wolrd")
        line_bot_api.reply_message(reply_token,text_message)

        
if __name__ == "__main__":
    app.run()