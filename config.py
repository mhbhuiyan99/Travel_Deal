class Config:
    """
    Application Configuration
    """

    # SQLAlchemy: 
    # a Python library that lets you work with databases using Python objects instead of writing raw SQL all the time.

    # SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite:///travel_deal.db" #The database file will be created automatically if it doesn't exist.

    # Disable unnecessary tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable debug mode
    DEBUG = True