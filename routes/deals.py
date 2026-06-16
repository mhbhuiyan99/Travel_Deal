from flask import Blueprint
from flask import request
from flask import jsonify
import logging

from utils.validators import (
    validate_deal,
    validate_search,
    validate_filter,
    validate_sort
)

from services.travel_service import (
    create_deal, 
    get_all_deals,
    get_deal_by_id,
    search_by,
    filter_by_price,
    get_sorted_deals,
    update_deal_by_id,
    delete_deal_by_id,
    get_most_viewed_deals
)

from services.recent_service import ( 
    add_recent_view,
    get_recent_deals
)

from services.stats_service import (
    record_search,
)

from utils.responses import (
    success_response,
    error_response
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
        logging.warning(error)
        return error_response(
            error,
            400
        )

    deal = create_deal(data)

    logging.info(
        f"Create request: deal={deal}"
    )

    return success_response(
        data=deal,
        message="Deal created",
        status_code=201
    )

@deals_bp.route("/", methods=["GET"])
def get_deals():

    deals = get_all_deals()

    logging.info(
        "Get all deals request"
    )

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

@deals_bp.route("/<int:deal_id>", methods=["GET"])
def get_deal(deal_id):

    deal = get_deal_by_id(deal_id)

    if deal is None:
        return error_response(
            "Deal not found",
            404
        )

    logging.info(
        f"Get deal request: ID={deal_id}"
    )

    add_recent_view(deal_id)

    return success_response(
        data=deal
    )

@deals_bp.route("/search", methods=["GET"])
def search_deals():

    filters = {
        "destination": request.args.get("destination"),
        "platform": request.args.get("platform"),
        "travel_type": request.args.get("travel_type")
    }

    error = validate_search(filters)

    if error:
        logging.warning(error)

        return error_response(
            error,
            400
        )

    logging.info(
        f"Search request received: {filters}"
    )

    if filters.get("destination"):
        record_search(
            filters["destination"]
        )

    deals = search_by(filters)

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

@deals_bp.route("/filter", methods=["GET"])
def filter_deals():

    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")

    error = validate_filter(
        min_price,
        max_price
    )

    if error:
        logging.warning(error)

        return error_response(
            error,
            400
        )

    logging.info(
        f"Filter request: min_price={min_price}, max_price={max_price}"
    )

    deals = filter_by_price(
        min_price,
        max_price
    )

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

@deals_bp.route("/sort", methods=["GET"])
def sort_deals():

    sort_by = request.args.get("sort_by")
    order = request.args.get(
        "order",
        "asc"
    )

    error = validate_sort(
        sort_by,
        order
    )

    if error:
        logging.warning(error)

        return error_response(
            error,
            400
        )

    logging.info(
        f"Sort request: sort_by={sort_by}, order={order}"
    )

    deals = get_sorted_deals(order)

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

@deals_bp.route("/recent", methods=["GET"])
def recent_deals():

    deals = get_recent_deals()

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

@deals_bp.route("/<int:deal_id>", methods=["PUT"])
def update_deal(deal_id):

    data = request.get_json()

    error = validate_deal(data)

    if error:
        logging.warning(error)

        return error_response(
            error,
            400
        )

    logging.info(
        f"Update deal request: ID={deal_id}"
    )

    deal = update_deal_by_id(
        deal_id,
        data
    )

    if deal is None:
        return error_response(
            "Deal not found",
            404
        )

    return success_response(
        data=deal,
        message="Deal updated"
    )

@deals_bp.route("/<int:deal_id>", methods=["DELETE"])
def delete_deal(deal_id):

    deleted = delete_deal_by_id(
        deal_id
    )

    logging.info(
        f"Delete deal request: ID={deal_id}"
    )

    if not deleted:
        return error_response(
            "Deal not found",
            404
        )

    return success_response(
        message="Deal deleted successfully"
    )

@deals_bp.route("/popular", methods=["GET"])
def most_viewed():

    deals_limit = 10

    deals = get_most_viewed_deals(
        deals_limit
    )

    logging.info(
        f"Get popular deals request: limit={deals_limit}"
    )

    return success_response(
        data={
            "count": len(deals),
            "deals": deals
        }
    )

