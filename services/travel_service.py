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

    db.session.add(deal)
    db.session.commit()
    
    return deal
