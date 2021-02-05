from flask import Flask, Blueprint, current_app, request, jsonify
from flask_mail import Message, Mail
from os import getenv
from app.db import get_db
from app.models import User
# Show error messages.
import sys

bp = Blueprint('email', __name__, url_prefix='/email')

@bp.route('/')
def email():

    # Configure flask mail.
    current_app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    current_app.config['MAIL_PORT'] = 465
    current_app.config['MAIL_USE_SSL'] = True
    current_app.config['MAIL_USERNAME'] = getenv('EMAIL_ADDRESS')
    current_app.config['MAIL_PASSWORD'] = getenv('EMAIL_PASSWORD')

    # Use the current app instance to create instance of Mail object.
    mail= Mail(current_app)

    # Configure email message. 
    msg = Message()
    msg.subject = "Sent from route"
    msg.recipients = ['michaeledwardhanson@gmail.com']
    msg.sender = getenv('EMAIL_ADDRESS')
    msg.body = 'Email body'
    mail.send(msg)

    # Temp output message.
    return 'Email Sent'
