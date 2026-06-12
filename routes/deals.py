from flask import Blueprint
from flask import request
from flask import jsonify
from services.travel_service import create_deal

deals_bp = Blueprint(
    "deals",
    __name__
)

@deals_bp.route("/", methods=["POST"])
def add_deals():
    data = request.get_json()

    deal = create_deal(data)

    return jsonify({
        "message": "Deal created",
        "deal": {
            "id": deal.id,
            "destination": deal.destination,
            "price": deal.price,
            "platform": deal.platform,
            "rating": deal.rating,
            "travel_type": deal.travel_type
        }
    }), 201