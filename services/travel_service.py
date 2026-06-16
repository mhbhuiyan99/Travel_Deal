from database.db import db
from database.models import TravelDeal
from sqlalchemy import select
from sqlalchemy import asc
from sqlalchemy import desc
import logging

def create_deal(data):
    """
    Create a new travel deal and save it to the database.
    Args:
        data (dict): Travel deal information received from the request.
    Returns:
        dict: The newly created travel deal as a dictionary.
    Raises:
        RuntimeError: If database insertion fails.
    """

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
        return deal.to_dict()
    except Exception as e:
        logging.error(
            f"Database insertion failed: {e}"
        )
        db.session.rollback()
        raise RuntimeError(
            "Database insertion failed"
        ) from e
  

def get_all_deals():
    """
    Retrieve all travel deals from the database.
    Returns:
        list: A list of travel deals as dictionaries.
    """

    deals = TravelDeal.query.all()
    return [deal.to_dict() for deal in deals]


def get_deal_by_id(deal_id):
    """
    Retrieve a travel deal by its ID.
    Args:
        deal_id (int): The ID of the travel deal.
    Returns:
        dict | None:
            Travel deal as a dictionary if found,
            otherwise None.
    """
    deal = TravelDeal.query.get(deal_id)
    if not deal:
        return None
    
    deal.view_count += 1
    try:
        db.session.commit()
        return deal.to_dict()
    except Exception as e:
        logging.error(
            f"Database updation failed for view count"
        )
        db.session.rollback()
        raise RuntimeError(
            "Update view count failed"
        )
    

def search_by(filters):
    """
    Search travel deals using optional filters.
    Supports partial and case-insensitive matching.
    Args:
        filters (dict): Search criteria containing
            destination, platform, and/or travel_type.
    Returns:
        list: A list of matching travel deals as dictionaries.
    """

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
    """
    Filter travel deals by price range.
    Args:
        min_price (float | None):
            Minimum allowed price.
        max_price (float | None):
            Maximum allowed price.
    Returns:
        list: A list of matching travel deals as dictionaries.
    """

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
    """
    Sort travel deals by price.
    Args:
        order (str):
            Sorting order.
            'asc' for ascending,
            'desc' for descending.
    Returns:
        list: A list of sorted travel deals as dictionaries.
    """

    query = select(TravelDeal)

    if order.lower() == 'desc':
        query = query.order_by(desc(TravelDeal.price))
    else:
        query = query.order_by(asc(TravelDeal.price))

    deals = db.session.execute(query).scalars().all()

    return [deal.to_dict() for deal in deals]


def update_deal_by_id(deal_id, data):
    """
    Update travel deals by id.
    Args:
        deal_id (int): The ID of travel deal.
        data (dict): Travel deal information received from the request.
    Returns:
        dict: The updated travel deal as a dictionary.

    """
    deal = TravelDeal.query.get(deal_id)

    if not deal:
        return None

    deal.destination = data["destination"]
    deal.price = data["price"]
    deal.platform = data["platform"]
    deal.rating = data["rating"]
    deal.travel_type = data["travel_type"]

    try:
        db.session.commit()
        return deal.to_dict()
    except Exception as e:
        logging.error(
            f"Database update failed: {e}"
        )
        db.session.rollback()
        raise RuntimeError(
            "Database update failed"
        ) from e


def delete_deal_by_id(deal_id):
    """
    Delete deal by id.
    Args:
        deal_id (int): The ID of travel deal.
    Returns:
        bool: 
            True if the deal was deleted successfully, 
            False if the deal was not found.
    """

    deal = TravelDeal.query.get(deal_id)

    if not deal:
        return None
    
    try:
        db.session.delete(deal)
        db.session.commit()
        return True
    except Exception as e:
        logging.error(
            f"Database deletion failed: {e}"
        )
        db.session.rollback()
        raise RuntimeError(
            "Database deletion failed"
        ) from e


def get_most_viewed_deals(limit_count=10):
    """
    Get the most viewed travel deals.
    Args:
        limit_count (int): Maximum number of deals to return.
    Returns:
        deal (dict): Most viewed deals ordered by view count.
    """

    query = (
        select(TravelDeal)
        .order_by(desc(TravelDeal.view_count))
        .limit(limit_count)
    )

    try:
        deals = db.session.execute(query).scalars().all()
        return [deal.to_dict() for deal in deals]
        
    except Exception as e:
        logging.error(
            f"Database selection failed: {e}"
        )
        db.session.rollback()
        raise RuntimeError(
            "Database selection failed"
        ) from e
