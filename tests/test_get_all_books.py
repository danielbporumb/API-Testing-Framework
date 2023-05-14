import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestGetAllBooks(unittest.TestCase):

    def setUp(self):
        self.books_api = SimpleBooksRequests()

    def test_get_all_books_status_code_without_filter(self):
        response = self.books_api.get_all_books()
        expected_response_code = 200
        actual_response_code = response.status_code

        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_books_number_of_results_without_filter(self):
        response = self.books_api.get_all_books()
        expected_number_of_results = 6
        actual_number_of_results = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, unexpected number of results")

    def test_get_all_books_filter_by_valid_limit(self):
        response = self.books_api.get_all_books(limit=3)
        expected_number_of_results = 3
        actual_number_of_results = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, unexpected number of results")

    def test_get_all_books_filter_by_invalid_limit_greater_than_20(self):
        response = self.books_api.get_all_books(limit=25)

        expected_response_code = 400
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected response code")

        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_error_message = response.json()["error"]
        self.assertEqual(expected_error_message, actual_error_message, "Error, unexpected error message")

    def test_get_all_books_filter_by_invalid_limit_less_than_0(self):
        response = self.books_api.get_all_books(limit=-5)

        expected_response_code = 400
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected response code")

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()["error"]
        self.assertEqual(expected_error_message, actual_error_message, "Error, unexpected error message")

    def test_get_all_books_filter_by_type_fiction(self):
        response = self.books_api.get_all_books(book_type="fiction")
        for i in range(len(response.json())): # iterez prin dictionar, de la 0 la lungimea dictionarului
            expected_type = "fiction" # ma astept la valoarea asta
            actual_type = response.json()[i]["type"] # sunt la pozitia i din dict si imi trebuie pt fiecare pozitie i, valoarea cheii "type"
            name = response.json()[i]["name"]
            self.assertEqual(expected_type, actual_type, f"Error, unexpected type for book '{name}' ")

    def test_get_all_books_filter_by_type_non_fiction(self):
        response = self.books_api.get_all_books(book_type="non-fiction")
        for i in range(len(response.json())):
            expected_type = "non-fiction"
            actual_type = response.json()[i]["type"]
            name = response.json()[i]["name"]
            self.assertEqual(expected_type, actual_type, f"Error, unexpected type for book '{name}' ")