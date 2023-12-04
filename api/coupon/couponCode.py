from collections import defaultdict
import datetime

daily_seconds = 24*60*60
weekly_seconds = 7*daily_seconds

class CouponCode:
    def __init__(self, code: str, user_total_repeat_count: int, user_per_day_repeat_count: int, user_per_week_repeat_count: int, global_total_repeat_count: int) -> None:
        self.code = code
        self.user_total_repeat_count = user_total_repeat_count
        self.user_per_day_repeat_count = user_per_day_repeat_count
        self.user_per_week_repeat_count = user_per_week_repeat_count
        self.global_total_repeat_count = global_total_repeat_count
        self.user_usage_count = {}
        self.user_usage_datetime = defaultdict(list)
        self.global_usage_count = 0

    def user_validity_by_total_count(self, user_id: str) -> bool:
        if user_id in self.user_usage_count and self.user_usage_count[user_id] >= self.user_total_repeat_count:
            return False
        return True

    def user_validity_by_daily_limit(self, user_id: str) -> bool:
        if user_id in self.user_usage_count and self.user_usage_count[user_id] >= self.user_per_day_repeat_count:
            last_coupon_use_datetime = self.user_usage_datetime[user_id][-self.user_per_day_repeat_count]
            daily_first_use_timediff = (datetime.datetime.now() - last_coupon_use_datetime).total_seconds()
            if daily_first_use_timediff < daily_seconds:
                return False
        return True

    def user_validity_by_weekly_limit(self, user_id: str) -> bool:
        if user_id in self.user_usage_count and self.user_usage_count[user_id] >= self.user_per_week_repeat_count:
            last_coupon_use_datetime = self.user_usage_datetime[user_id][-self.user_per_week_repeat_count]
            weekly_first_use_timediff = (datetime.datetime.now() - last_coupon_use_datetime).total_seconds()
            if weekly_first_use_timediff < weekly_seconds:
                return False
        return True

    def validity_by_global_limit(self) -> bool:
        if self.global_usage_count >= self.global_total_repeat_count:
            return False
        return True

    def update_usage_counts(self, user_id: str) -> None:
        if user_id not in self.user_usage_count:
            self.user_usage_count[user_id] = 1
        else:
            self.user_usage_count[user_id] += 1
        self.user_usage_datetime[user_id].append(datetime.datetime.now())
        self.global_usage_count += 1

    def coupon_to_dict(self) -> dict:
        return {
            "code": self.code,
            "user_total_repeat_count": self.user_total_repeat_count,
            "user_per_day_repeat_count": self.user_per_day_repeat_count,
            "user_per_week_repeat_count": self.user_per_week_repeat_count,
            "global_total_repeat_count": self.global_total_repeat_count,
            "user_usage_count": self.user_usage_count,
            "user_usage_datetime": self.user_usage_datetime,
            "global_usage_count": self.global_usage_count,
        }