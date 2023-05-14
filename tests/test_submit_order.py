import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "": # se va genera doar la primul test, la urmatoarele nu va mai fi 'gol'
            self.access_token = self.books_api.generate_token()

    def test_submit_order_status_code(self):
        book_id = 1
        customer_name = "TA41"
        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_response_code = 201
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

        expected_created_message = True
        actual_created_message = response.json()["created"]
        self.assertEqual(expected_created_message, actual_created_message, "Error, 'created' json value is not True")

    def test_submit_order_with_invalid_book_id(self):
        book_id = -545
        customer_name = "TA41"
        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_response_code = 400
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

        expected_response_message = "Invalid or missing bookId."
        actual_response_message = response.json()["error"]
        self.assertEqual(expected_response_message, actual_response_message, "Error, unexpected error message")
