from flask import Flask
from config import Config
from database.db import db
from routes.deals import deals_bp
from routes.stats import stats_bp
from database.models import TravelDeal
import logging

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

    app.register_blueprint(
        stats_bp
    )


    @app.route("/")
    def health():
        """
        Health Check API
        """

        return {
            "message": "Welcome to Travel Deal"
        }

    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
