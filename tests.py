import unittest
from app import app


class TestCouponCodeAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_coupon_success(self):
        response = self.app.post('/coupon/add', json={
            'code': 'test_add_coupon_success',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        self.assertEqual(response.status_code, 201)

    def test_add_coupon_failure(self):
        response = self.app.post('/coupon/add', json={
            'code': 'test_add_coupon_failure',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
        })
        self.assertEqual(response.status_code, 500)

    def test_verify_coupon_valid(self):
        self.app.post('/coupon/add', json={
            'code': 'test_verify_coupon_valid',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/validate', json={'code': 'test_verify_coupon_valid', 'user_id': 'test_verify_coupon_valid'})
        data = response.get_json()
        self.assertTrue(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_verify_coupon_invalid_total(self):
        self.app.post('/coupon/add', json={
            'code': 'test_verify_coupon_invalid_total',
            'user_total_repeat_count': 0,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/validate', json={'code': 'test_verify_coupon_invalid_total', 'user_id': 'test_verify_coupon_invalid_total'})
        data = response.get_json()
        self.assertFalse(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_verify_coupon_invalid_daily(self):
        self.app.post('/coupon/add', json={
            'code': 'test_verify_coupon_invalid_daily',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 0,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/validate', json={'code': 'test_verify_coupon_invalid_daily', 'user_id': 'test_verify_coupon_invalid_daily'})
        data = response.get_json()
        self.assertFalse(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_verify_coupon_invalid_weekly(self):
        self.app.post('/coupon/add', json={
            'code': 'test_verify_coupon_invalid_weekly',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 0,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/validate', json={'code': 'test_verify_coupon_invalid_weekly', 'user_id': 'test_verify_coupon_invalid_weekly'})
        data = response.get_json()
        self.assertFalse(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_verify_coupon_invalid_global(self):
        self.app.post('/coupon/add', json={
            'code': 'test_verify_coupon_invalid_global',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 0
        })
        response = self.app.post('/coupon/validate', json={'code': 'test_verify_coupon_invalid_global', 'user_id': 'test_verify_coupon_invalid_global'})
        data = response.get_json()
        self.assertFalse(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_apply_coupon(self):
        self.app.post('/coupon/add', json={
            'code': 'test_apply_coupon',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/apply', json={'code': 'test_apply_coupon', 'user_id': 'test_apply_coupon'})
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
