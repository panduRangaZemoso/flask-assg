from exts import db, marshmallow

# Task Model
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    done=db.Column(db.Boolean)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def setName(self, name):
        self.name = name

    def setDone(self, done):
        self.done = done

    def setUserId(self, user_id):
        self.user_id = user_id    

    def __init__(self, name, user_id, done=False):
        self.name=name
        self.done=done
        self.user_id=user_id
        
    def __repr__(self):
        return '<Task %r done: %r user_id: %r>' % self.name % self.done % self.user_id


# Task Schema
class TaskSchema(marshmallow.Schema):
    class Meta:
        fields=('id','name','done','user_id')        