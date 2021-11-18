"""Unit tests for User API."""
import unittest
import requests


class UserApiTest(unittest.TestCase):
    """Class for test User API of Flamby (Government Module)."""

    def test_get_user_by_citizen_id_was_successful(self):
        """
        Test Case ID: 1
        Description: Test that can get the user by citizen id was successful.
        """
        response = requests.get(
            "https://flamxby.herokuapp.com/user/0123456789012")
        response_body = response.json()
        response_content = {
            "user_id": 9,
            "name": "Pitchapa",
            "surname": "Sae-lim",
            "citizen_id": "0123456789012",
            "occupation": "Student",
            "address": "Home",
            "reservations": []
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.headers["Server"], "uvicorn")
        self.assertEqual(response_body["citizen_id"], "0123456789012")
        self.assertEqual(response_body, response_content)

    def test_get_user_with_citizen_id_was_not_enough_digits(self):
        """
        Test Case ID: 2
        Description: Test that can't get the user by citizen id was not enough digits.
        """
        response = requests.get(
            "https://flamxby.herokuapp.com/user/0123456789")
        response_body = response.json()
        details = {"detail": "No user with this citizen id"}

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.headers["Server"], "uvicorn")
        self.assertEqual(response_body, details)

    def test_get_user_with_citizen_id_is_string(self):
        """
        Test Case ID: 3
        Description: Test that can't get the user with citizen id is a string.
        """
        response = requests.get("http://flamxby.herokuapp.com/user/abc")
        response_body = response.json()
        details = {"detail": "No user with this citizen id"}

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.headers["Server"], "uvicorn")
        self.assertEqual(response_body, details)

    def test_get_user_with_citizen_id_more_than_required_digits(self):
        """
        Test Case ID: 4
        Description: Test that can't get the user with citizen id more than required digits.
        """
        response = requests.get(
            "https://flamxby.herokuapp.com/user/0123456789012123412345678")
        response_body = response.json()
        details = {"detail": "No user with this citizen id"}

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.headers["Server"], "uvicorn")
        self.assertEqual(response_body, details)


if __name__ == '__main__':
    unittest.main()
