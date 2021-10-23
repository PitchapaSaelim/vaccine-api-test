"""Unit tests for User API."""
import unittest
import requests


class UserApiTest(unittest.TestCase):
    """Class for test User API of Flamby (Government Module)."""

    def test_get_user_by_citizen_id_was_successful(self):
        """Test that can get the user by citizen id was successful."""
        response = requests.get(
            "https://flamxby.herokuapp.com/user/1132267849564")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_get_user_with_citizen_id_was_not_enough_digits(self):
        """Test that can't get the user by citizen id was not enough digits."""
        response = requests.get(
            "https://flamxby.herokuapp.com/user/11322678495")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_get_user_with_citizen_id_is_string(self):
        """Test that can't get the user with citizen id is a string."""
        response = requests.get("http://flamxby.herokuapp.com/user/abc")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_get_user_with_citizen_id_more_than_required_digits(self):
        """Test that can't get the user with citizen id more than required digits."""
        response = requests.get(
            "http://flamxby.herokuapp.com/user/11322678495641132267849564")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")


if __name__ == '__main__':
    unittest.main()
