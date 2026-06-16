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

    view_count = db.Column(
        db.Integer,
        default = 0,
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

    id = db.Column(
        db.Integer, 
        primary_key = True
    )

    deal_id = db.Column(
        db.Integer,
        db.ForeignKey("travel_deals.id"),
        nullable=False
    )

    viewed_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

class ApiStats(db.Model):
    __tablename__ = "api_stats"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    total_requests = db.Column(
        db.Integer,
        default=0
    )

    successful_requests = db.Column(
        db.Integer,
        default=0
    )

    failed_requests = db.Column(
        db.Integer,
        default=0
    )

class SearchStats(db.Model):
    __tablename__ = "search_stats"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    destination = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    search_count = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

