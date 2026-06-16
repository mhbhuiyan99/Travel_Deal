from sqlalchemy import desc

from database.db import db
from database.models import (
    ApiStats,
    SearchStats,
    TravelDeal
)

from services.travel_service import (
    get_most_viewed_deals
)

def get_stats_row():
    """
    Retrieve the API statistics record.
    Creates a new record if none exists.
    Returns:
        ApiStats: The API statistics object.
    """
    stats = ApiStats.query.first()

    if not stats:
        stats = ApiStats()

        db.session.add(stats)
        db.session.commit()

    return stats

def increment_total_requests():
    """
    Increment the total API request count.
    Returns:
        None
    """
    stats = get_stats_row()

    stats.total_requests += 1

    db.session.commit()

def increment_successful_requests():
    """
    Increment the successful API request count.
    Returns: None
    """
    stats = get_stats_row()

    stats.successful_requests += 1

    db.session.commit()

def increment_failed_requests():
    """
    Increment the failed API request count.
    Returns: None
    """
    stats = get_stats_row()

    stats.failed_requests += 1

    db.session.commit()

def record_search(destination):
    """
    Record a destination search.
    Args:
        destination (str): The searched destination.
    Returns: None
    """
    
    search = SearchStats.query.filter_by(
        destination=destination.lower()
    ).first()

    if search:
        search.search_count += 1

    else:
        search = SearchStats(
            destination=destination.lower(),
            search_count=1
        )

        db.session.add(search)

    db.session.commit()

def get_most_searched_destination():
    """
    Record a destination search.
    Args:
        destination (str): The searched destination.
    Returns: None
    """

    search = (
        SearchStats.query
        .order_by(
            desc(SearchStats.search_count)
        )
        .first()
    )

    if not search:
        return None

    return search.destination   

def get_statistics():
    """
    Retrieve application statistics.
    Includes:
        - Total API requests
        - Successful requests
        - Failed requests
        - Most searched destination
        - Most viewed deal
    Returns:
        dict: A dictionary containing all application statistics.
    """
    stats = get_stats_row()
    most_viewed = get_most_viewed_deals(1)

    return {
        "total_requests":
            stats.total_requests,

        "successful_requests":
            stats.successful_requests,

        "failed_requests":
            stats.failed_requests,

        "most_searched_destination":
            get_most_searched_destination(),

        "most_viewed_deal":
            most_viewed[0] if most_viewed else None
    }