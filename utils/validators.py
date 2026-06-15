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

def validate_filter(min_price, max_price):

    try:
        min_value = float(min_price) if min_price is not None else None
        max_value = float(max_price) if max_price is not None else None
    except ValueError:
        return "Price values must be valid numbers"

    if min_value is not None and min_value < 0:
        return "Minimum price cannot be negative"

    if (
        min_value is not None and
        max_value is not None and
        max_value < min_value
    ):
        return "Maximum price cannot be smaller than minimum price"

    return None

def validate_sort(sort_by, order):
    allowed_orders = ["asc", "desc"]

    if sort_by != "price":
        return "Can only sort by 'price'"
    
    if order is not None and order not in allowed_orders:
        return "Order must be either 'asc' or 'desc'"

    return None