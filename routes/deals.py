from flask import Blueprint

deals_bp = Blueprint(
    "deals",
    __name__
)

@deals_bp.route("/")
def get_deals():
    return {"message": "Deals endpoint"}