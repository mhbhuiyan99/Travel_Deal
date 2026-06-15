from database.db import db
from database.models import TravelDeal
from sqlalchemy import select
from sqlalchemy import asc
from sqlalchemy import desc

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
    query = select(TravelDeal)

    if filters.get('destination'):
        query = query.where(TravelDeal.destination.ilike(f"%{filters['destination']}%"))
    
    if filters.get('travel_type'):
        query = query.where(TravelDeal.travel_type.ilike(f"%{filters['travel_type']}%"))

    if filters.get('platform'):
        query = query.where(TravelDeal.platform.ilike(f"%{filters['platform']}%"))

    result = db.session.execute(query).scalars().all()

    return [deal.to_dict() for deal in result]

def filter_by_price(min_price = None, max_price = None):
    query = select(TravelDeal)

    if min_price is not None:
        query = query.where(
            TravelDeal.price >= float(min_price)
        )

    if max_price is not None:
        query = query.where(
            TravelDeal.price <= float(max_price)
        )

    deals = db.session.execute(query).scalars().all()

    return [deal.to_dict() for deal in deals]

def get_sorted_deals(order):
    query = select(TravelDeal)

    if order.lower() == 'desc':
        query = query.order_by(desc(TravelDeal.price))
    else:
        query = query.order_by(asc(TravelDeal.price))

    deals = db.session.execute(query).scalars().all()

    return [deal.to_dict() for deal in deals]