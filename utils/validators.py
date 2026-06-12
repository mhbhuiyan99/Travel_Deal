def validate_deal(data):

    if not data:
        return "Request body is required"

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

    if data["rating"] < 1 or data["rating"] > 5:
        return "Rating must be between 1 and 5"

    valid_travel_types = [
        "Budget",
        "Luxury",
        "Adventure",
        "Family"
    ]

    if data["travel_type"] not in valid_travel_types:
        return (
            "Travel type must be one of: "
            "Budget, Luxury, Adventure, Family"
        )

    return None