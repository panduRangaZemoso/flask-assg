from datetime import datetime

# Error Model
class Error:
    def __init__(self, message, timestamp, statuscode)
        self.message=message
        self.timestamp=timestamp
        self.statuscode=statuscode
    def __repr__(self):
        return '<Error message: %r timestamp: %r statuscode: %r>' % self.message % self.timestamp % self.statuscode  


# Error Schema
class ErrorSchema(marshmallow.Schema):
    class Meta:
        fields=('message','timestamp','statuscode')         