from flask import Flask

def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
