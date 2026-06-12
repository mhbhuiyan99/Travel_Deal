def validate_deal(data):

    required_fields = [
        "destination",
        "price",
        "platform",
        "rating",
        "travel_type"
    ]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

    if not data["destination"].strip():
        return "Destination cannot be empty"

    if not data["platform"].strip():
        return "Platform cannot be empty"

    if not data["travel_type"].strip():
        return "Travel type cannot be empty"

    if data["price"] <= 0:
        return "Price must be greater than 0"

    if data["rating"] < 0 or data["rating"] > 5:
        return "Rating must be between 0 and 5"

    return None