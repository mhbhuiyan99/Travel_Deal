from flask import Blueprint
from flask import jsonify

from services.stats_service import (
    get_statistics,
    increment_total_requests,
    increment_successful_requests
)


stats_bp = Blueprint(
    "stats",
    __name__
)

@stats_bp.route("/stats",methods=["GET"])
def get_stats():

    increment_total_requests()

    statistics = get_statistics()

    increment_successful_requests()

    return jsonify(
        statistics
    ), 200