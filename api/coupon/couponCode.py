from collections import defaultdict
import datetime

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
    
    def user_validity_by_time(self, user_id: str) -> ():
        #check daily limit
        if user_id in self.user_usage_count:
            last_coupon_use_datetime = self.user_usage_datetime[user_id][-1]
            if (datetime.datetime.now() - last_coupon_use_datetime).total_seconds() > 0:
                pass
        return ()


    def can_user_use_daily(self, user_id: str) -> bool:
        if user_id in self.user_usage_count and self.user_usage_count[user_id] >= self.user_per_day_repeat_count:
            return False
        return True

    def can_user_use_weekly(self, user_id: str) -> bool:
        if user_id in self.user_usage_count and self.user_usage_count[user_id] >= self.user_per_week_repeat_count:
            return False
        return True

    def can_global_use(self) -> bool:
        if self.global_usage_count >= self.global_total_repeat_count:
            return False
        return True

    def update_usage_counts(self, user_id: str) -> None:
        if user_id not in self.user_usage_count:
            self.user_usage_count[user_id] = 1
            self.user_usage_datetime[user_id].append(datetime.datetime.now())
        else:
            self.user_usage_count[user_id] += 1
        self.global_usage_count += 1