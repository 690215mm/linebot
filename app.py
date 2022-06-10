from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('A3v8IPxjoZQf0n1nDOwpeazNdOjZb4a8BRb/+zXDVfznIRWp7n93+huFVftVhrJp5RRZ0VLxUbj1j+se6uEGjOL51Q4cex7ii0HRFXlfgSaGC8RR6+/v1O6oFVKIi8TiYJxxspBssluhIXaYIACutQdB04t89/1')
handler = WebhookHandler('493998fd4269cb967e08b8d3b3ce6415')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問甚麼"

    if msg == 'hi':
       r = 'hi'
    elif msg == '吃飽沒':
       r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r)


if __name__ == "__main__":
    app.run()