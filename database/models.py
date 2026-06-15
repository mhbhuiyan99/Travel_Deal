from database.db import db

class TravelDeal(db.Model):
    __tablename__ = "travel_deals"

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

    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "platform": self.platform,
            "rating": self.rating,
            "travel_type": self.travel_type
        }

class RecentView(db.Model):
    __tablename__ = "recent_views"

    id = db.Column(db.Integer, primary_key=True)

    deal_id = db.Column(
        db.Integer,
        db.ForeignKey("travel_deals.id"),
        nullable=False
    )

    viewed_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )