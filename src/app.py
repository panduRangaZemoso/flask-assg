from flask import Flask

from exts import db,marshmallow,migrate
from api.TaskApi import taskApi
from api.UserApi import userApi

import os

def registerExtensions(app):
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)


def createFlaskApp():
    app = Flask(__name__)

    # Add Config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register Extensions
    registerExtensions(app)

    # Blueprints
    app.register_blueprint(taskApi,url_prefix='/task')
    app.register_blueprint(userApi,url_prefix='/user')   

    return app  

app = createFlaskApp()

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
