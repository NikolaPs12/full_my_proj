from flask import Flask
from .extensions import db, login_manager, migrate
from .config import Config
from .routes.user import user
from .routes.main import main_bp
from .routes.post import posts

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(Config)

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(posts, url_prefix='/post')
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
     
    # sets in login_manager
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Пожалуйста, войдите в систему, чтобы получить доступ к этой странице.' 
    with app.app_context():
        db.create_all()


    return app 