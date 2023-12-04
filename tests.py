import unittest
from app import app


class TestCouponCodeAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_coupon(self):
        response = self.app.post('/coupon/add', json={
            'code': 'TEST123',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        self.assertEqual(response.status_code, 201)

    def test_verify_coupon(self):
        self.app.post('/coupon/add', json={
            'code': 'TEST456',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/validate', json={'code': 'TEST456', 'user_id': 'user1'})
        data = response.get_json()
        self.assertTrue(data['valid'])
        self.assertEqual(response.status_code, 200)

    def test_apply_coupon(self):
        self.app.post('/coupon/add', json={
            'code': 'TEST789',
            'user_total_repeat_count': 2,
            'user_per_day_repeat_count': 1,
            'user_per_week_repeat_count': 1,
            'global_total_repeat_count': 5
        })
        response = self.app.post('/coupon/apply', json={'code': 'TEST789', 'user_id': 'user2'})
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
