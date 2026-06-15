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

    if not isinstance(data["destination"], str) or not data["destination"].strip():
        return "Destination must be a non-empty string"

    if not isinstance(data["platform"], str) or not data["platform"].strip():
        return "Platform must be a non-empty string"

    if not isinstance(data["travel_type"], str) or not data["travel_type"].strip():
        return "Travel type must be a non-empty string"

    try:
        price = float(data["price"])
        if price <= 0:
            return "Price must be greater than 0"
    except (ValueError, TypeError):
        return "Price must be a valid number"

    try:
        rating = float(data["rating"])
        if rating < 1 or rating > 5:
            return "Rating must be between 1 and 5"
    except (ValueError, TypeError):
        return "Rating must be a valid number"

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

def validate_search(filters):
    if not any(filters.values()):
        return "At least one search parameter is required."
    
    return None