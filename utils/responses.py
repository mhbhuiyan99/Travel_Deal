from flask import jsonify

from services.stats_service import (
    increment_successful_requests,
    increment_failed_requests,
    increment_total_requests
)

def success_response(data=None, message=None, status_code=200):

    increment_successful_requests()
    increment_total_requests()

    response = {}

    if message:
        response["message"] = message

    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


def error_response(message, status_code=400):

    increment_failed_requests()
    increment_total_requests()

    return jsonify({
        "error": message
    }), status_code