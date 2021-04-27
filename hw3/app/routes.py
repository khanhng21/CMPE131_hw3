from flask import render_template, redirect
from flask_login import current_user, login_user

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods = ('GET','POST'))
def home():
    '''Returns the template of the app
        Parameters:
            user(str): a string of the name of user
            author (str): a string of the name of author
            messages (str): a string of messages
        Return:
            render_template: return to the template of the app'''
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database
        user = User.query.filter_by(author = form.author.data).first()
        if user is None or not user.check_author(form.author.data):
            user = User(author = form.author.data)
            db.session.add(user)
            db.session.commit()
        db.session.refresh(user)
        message = Messages(user_id = user.id, message = form.message.data)   
        db.session.add(message)
        db.session.commit()
        return redirect('/')
        db.session.refresh(message) 
    messageList = (db.session.query(User, Messages).join(User)).all()    
    posts = []
    for item in messageList:
        posts.append({'author': item.User.author, 'message': item.Messages.message})
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    return render_template('home.html', posts=posts, form=form)

