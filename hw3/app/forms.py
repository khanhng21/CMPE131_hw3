from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    '''MessageFrorm class is to create the form when user want to send a message
    ...
    Parameters:
    ----
    author: string
        The name of author
    message: string
        message that is required to enter
    submit: button
        A button for user to send their meessage'''
    # add
    # author (string) validator should make this textbox required
    # message (string) validator should make this textbox required
    # submit (button) text should say 'Send' 
    author = StringField('author', validators = [DataRequired()])
    message = StringField('message', validators = [DataRequired()])
    submit = SubmitField('Send')
