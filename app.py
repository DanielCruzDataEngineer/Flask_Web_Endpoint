from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


GOOD_BOY_URL = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
    "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)
@app.route("/home")
def testes():
    return render_template('index.html')

@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():

    try:
        num_media = int(request.values.get("NumMedia"))
    except (ValueError, TypeError):
        return render_template('index.html')
    response = MessagingResponse()
    if not num_media:
        msg = response.message("Helloooo")
        
    else:
        msg = response.message("Thanks for the image. Here's one for you!")
        msg.media(GOOD_BOY_URL)
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
