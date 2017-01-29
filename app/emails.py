from flask_mail import Message, render_template
from app import mail
from .decorator import async
from config import ADMINS
from app import app
@async
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,sender,recipients,text_body,html_body):
    msg=Message(subject,sender=sender,recipients=recipients)
    msg.body=text_body
    msg.html=html_body
    send_async_email(app,msg)

def follower_notification(followed,follower):
    send_email("[microblog] %s now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed,follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))