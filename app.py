from flask import Flask
from config import Config
from database.db import db
from routes.deals import deals_bp
from database.models import TravelDeal

def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)

    # Load Config
    app.config.from_object(
        Config
    )

    # Initialize DB
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register Blueprint
    app.register_blueprint(
        deals_bp,
        url_prefix="/deals"
    )


    @app.route("/")
    def health():
        """
        Health Check API
        """

        return {
            "message": "Welcome to Travel Deal"
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
