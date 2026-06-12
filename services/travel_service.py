from database.db import db
from database.models import TravelDeal

def create_deal(data):
    deal = TravelDeal(
        destination = data["destination"],
        price = data["price"],
        platform = data["platform"],
        rating = data["rating"],
        travel_type = data["travel_type"]
    )

    try:
        db.session.add(deal)
        db.session.commit()

    except Exception:
        db.session.rollback()

        return jsonify({
            "error": "Failed to create deal"
        }), 500

    return deal

def get_deals():
    deals = 
