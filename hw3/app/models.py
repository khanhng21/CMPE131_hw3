from app import db

class User(db.Model):
    '''User class is used to organize user's information (id, author, message)
following column order.
        ...
        Attributes
        -----
        id: int
            the id of user
        author: string
            the name of user
        message: string
            messages of user
        '''
    # have the following columns
    # id (int)
    # author (string, unique, can't be null)
    # message (linkd to Messages table)
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String, nullable = False, unique = True)
    message = db.relationship('Messages', backref = 'author', lazy = 'dynamic')

    def check_author(self,author):
        '''Check if author matches the login user, return whether it is true or false'''
        if author != self.author:
            return False
        return True
    def __repr__(self):
        '''Return a string of "User" and the author'''
        return f'<User {self.author}>'

class Messages(db.Model):
    '''Messgaes class is used to organize the messages from author following
    column order
     ...
    Attributes
    -----
    id: int
        the id of user
    user_is: int
        link to id
    message: string
        messages of user'''
    # have the following columns
    # id (int)
    # message (string, not unique, can't be null)
    # user_id link to id (int)
    __tablename__ = 'message'
    id = db.Column(db.Integer,primary_key = True)
    message = db.Column(db.String, unique = False, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message
    def __repr__(self):
        return f'<Message {self.message}>'
db.create_all()
db.session.commit()        
