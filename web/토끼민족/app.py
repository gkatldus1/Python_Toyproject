from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    
    db.init_app(app)
    Migrate().init_app(app, db)

    from views import main_view
    import model

    app.register_blueprint(main_view.bp)

    app.secret_key = "dfadsfdgsdfhktknbcrwpf"
    app.config['SESSION_TYPE'] = 'filesystem'



    return app

if __name__ == "__main__":
    create_app().run()

