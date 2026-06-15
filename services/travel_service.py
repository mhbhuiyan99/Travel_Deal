from database.db import db
from database.models import TravelDeal
from sqlalchemy import select

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
        return deal
    except Exception as e:
        db.session.rollback()
        raise RuntimeError("Database insertion failed") from e
  

def get_all_deals():
    deals = TravelDeal.query.all()
    return [deal.to_dict() for deal in deals]


def get_deal_by_id(deal_id):
    deal = TravelDeal.query.get(deal_id)
    if not deal:
        return None
    return deal.to_dict()


def search_by(filters):
    stmt = select(TravelDeal)

    if filters.get('destination'):
        stmt = stmt.where(TravelDeal.destination.ilike(f"%{filters['destination']}%"))
    
    if filters.get('travel_type'):
        stmt = stmt.where(TravelDeal.travel_type.ilike(f"%{filters['travel_type']}%"))

    if filters.get('platform'):
        stmt = stmt.where(TravelDeal.platform.ilike(f"%{filters['platform']}%"))

    result = db.session.execute(stmt).scalars().all()

    return [deal.to_dict() for deal in result]

def filter_by_price(min_price = None, max_price = None):
    stmt = select(TravelDeal)

    if min_price is not None:
        stmt = stmt.where(
            TravelDeal.price >= float(min_price)
        )

    if max_price is not None:
        stmt = stmt.where(
            TravelDeal.price <= float(max_price)
        )

    deals = db.session.execute(stmt).scalars().all()

    return [deal.to_dict() for deal in deals]