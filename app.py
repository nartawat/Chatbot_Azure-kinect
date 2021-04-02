from flask import Flask, request
from linebot import *
from linebot.models import *

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://chatbotazure:8ZDhcwsPc05AHYSr@cluster0.angf9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Chatbot
col = db["Azure"]


app = Flask(__name__)

line_bot_api = LineBotApi('Lb5v+X5Hr1gdHa+6yFkWcxpPLlfCXVMqG+QXUIvjCN0HmftdNNl8NixyyDBmOGzVjNGzNGiB2koW10I8SEzSxijriRGZR1/G9n6FgqDvsLXrT2h++Y8LyYUYGadiOGixYj30nBHYnRAXwRmpdiU2FAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('97ea021104b6a2182af981ae780d0fb0')

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route("/calltae", methods=['POST'])
def calltae():
    body = request.get_json(silent=True, force=True)
    col.update_one({'_id': ObjectId("606714605bf23384453618dd")},  {'$set': {"number": body["number"]}})
    print(body["number"])
    
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
        num = col.find_one()
        number = str(num["number"])
        text = "แจ้งเตือน"+number+"ครั้ง"
        text_message = TextSendMessage(text=text)
        line_bot_api.reply_message(reply_token,text_message)

        
if __name__ == "__main__":
    app.run()