from .couponCode import CouponCode

class CouponCodeService:
    def __init__(self):
        self.coupons = {}

    def add_coupon(self, code, user_total_repeat_count, user_per_day_repeat_count, user_per_week_repeat_count, global_total_repeat_count):
        coupon = CouponCode(code, user_total_repeat_count, user_per_day_repeat_count, user_per_week_repeat_count, global_total_repeat_count)
        self.coupons[code] = coupon

    def verify_coupon_validity(self, code, user_id):
        if code not in self.coupons:
            return False, "Coupon does not exist"

        coupon = self.coupons[code]

        if not coupon.user_validity_by_total_count(user_id):
            return False, "User total limit reached"
        if not coupon.user_validity_by_daily_limit(user_id):
            return False, "User daily limit reached"
        if not coupon.user_validity_by_weekly_limit(user_id):
            return False, "User weekly limit reached"
        if not coupon.validity_by_global_limit():
            return False, "Global limit reached"

        return True, "Coupon is valid"

    def apply_coupon(self, code, user_id):

        is_valid, message = self.verify_coupon_validity(code, user_id)
        if not is_valid:
            return False, message

        coupon = self.coupons[code]
        coupon.update_usage_counts(user_id)

        return True, "Coupon applied successfully"

    def coupon_details(self, code):
        if code in self.coupons:
            coupon = self.coupons[code]
            return coupon.coupon_to_dict()
        return {
            "error": "Coupon does not exist"
        }