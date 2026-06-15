from sqlalchemy import select
from database.db import db
from database.models import RecentView
from database.models import TravelDeal


def add_recent_view(deal_id):

    recent = RecentView(
        deal_id=deal_id
    )

    db.session.add(recent)
    db.session.commit()


def get_recent_deals(limit=5):

    query = (
        select(RecentView)
        .order_by(RecentView.viewed_at.desc())
        .limit(limit)
    )

    recent_views = db.session.execute(
        query
    ).scalars().all()

    deals = []

    for recent in recent_views:

        deal = TravelDeal.query.get(
            recent.deal_id
        )

        if deal:
            deals.append(
                deal.to_dict()
            )

    return deals