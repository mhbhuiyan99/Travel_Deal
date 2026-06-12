from flask import Blueprint
from flask import request
from flask import jsonify

from utils.validators import validate_deal

from services.travel_service import (
    create_deal, 
    get_all_deals,
    get_deal_by_id
)



deals_bp = Blueprint(
    "deals",
    __name__
)

@deals_bp.route("/", methods=["POST"])
def add_deals():
    data = request.get_json()

    error = validate_deal(data)
    if error:
        return jsonify({
            "error": error
        }), 400

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

@deals_bp.route("/", methods=["GET"])
def get_deals():
    deals = get_all_deals()
    return jsonify({
        "count": len(deals),
        "data": deals
    }), 200

@deals_bp.route("/<int:deal_id>", methods=["GET"])
def get_deal(deal_id):
    deal = get_deal_by_id(deal_id)

    if deal is None:
        return jsonify({
            "error": "Deal not found"
        }), 404

    return jsonify(
        deal
    ), 200