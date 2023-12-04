from flask import Blueprint, request, jsonify
from .couponCodeService import CouponCodeService

couponBlueprint = Blueprint("coupon", __name__)

coupon_service = CouponCodeService()

@couponBlueprint.route("/add", methods=["POST"])
def add_coupon():
    data = request.json
    try:
        coupon_service.add_coupon(
            data['code'],
            data['user_total_repeat_count'],
            data['user_per_day_repeat_count'],
            data['user_per_week_repeat_count'],
            data['global_total_repeat_count']
        )
        return jsonify({'message': 'Coupon added successfully'}), 201
    except:
        return jsonify({'message': 'Coupon not added successfully. Please make sure the input data is correct.'}), 500


@couponBlueprint.route("/validate", methods=["POST"])
def validate_coupon():
    data = request.json
    result, message = coupon_service.verify_coupon_validity(data['code'], data['user_id'])
    return jsonify({'valid': result, 'message': message})


@couponBlueprint.route('/apply', methods=['POST'])
def apply_coupon():
    data = request.json
    result, message = coupon_service.apply_coupon(data['code'], data['user_id'])
    return jsonify({'success': result, 'message': message})


@couponBlueprint.route('/details', methods=['POST'])
def coupon_details():
    data = request.json
    result = coupon_service.coupon_details(data['code'])
    return jsonify(result)

