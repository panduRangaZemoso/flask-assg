from exts import db, marshmallow

# User Model
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(30), nullable=False)
    tasks=db.relationship('Task',backref='user',lazy=True)

    def setUsername(self, username):
        self.username = username

    def __init__(self, username):
        self.username=username

    def __repr__(self):
        return '<User id: %r username: %r>' % self.id % self.username    

# User Schema
class UserSchema(marshmallow.Schema):
    class Meta:
        fields=('id','username')