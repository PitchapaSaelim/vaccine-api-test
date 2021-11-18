# Vaccine Api Test
> Unit tests for User API of Flamby (Government Module).
> *https://flamxby.herokuapp.com/docs*

| Project Group Name | Project Module Name | Endpoint(s) |
|--------------------|---------------------|-------------|
| Flamby             | Government Module   | `GET` Users |

## Test Cases for User API of Flamby
| Test Case ID | Test Case Name | Description | Expected Result | Status |
|--------------|----------------|-------------|-----------------|--------|
|1| `test_get_user_by_citizen_id_was_successful` | Test that can get the user by citizen id was successful.| The user can get the user by citizen id.|✔️:PASS |
|2| `test_get_user_with_citizen_id_was_not_enough_digits` | Test that can't get the user by citizen id was not enough digits.| The user can't get the user by citizen id.|✔️:PASS |
|3| `test_get_user_with_citizen_id_is_string` | Test that can't get the user with citizen id is a string.| The user can't get the user by citizen id.|✔️:PASS |
|4| `test_get_user_with_citizen_id_more_than_required_digits` | Test that can't get the user with citizen id more than required digits.| The user can't get the user by citizen id.|✔️:PASS |