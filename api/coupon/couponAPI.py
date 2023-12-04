from flask import Blueprint

couponBlueprint = Blueprint("coupon", __name__)

@couponBlueprint.route("/test", methods=["GET"])
def test():
    return {
        "msg": "Coupon Endpoint Available"
    }

@couponBlueprint.route("/add", methods=["POST"])
def add_coupon():
    pass


@couponBlueprint.route("/validate", methods=["POST"])
def read_records():
    pass

