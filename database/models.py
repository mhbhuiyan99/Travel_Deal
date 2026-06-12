from database.db import db

class TravelDeal(db.Model):
    __tablename = "travel_deals"

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    destination = db.Column(
        db.String(100),
        nullable = False
    )

    price = db.Column(
        db.Float,
        nullable = False
    )

    platform = db.Column(
        db.String(100),
        nullable = False
    )

    rating = db.Column(
        db.Float,
        nullable = False
    )

    travel_type = db.Column(
        db.String(50),
        nullable = False
    )