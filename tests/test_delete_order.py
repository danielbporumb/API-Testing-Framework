import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestDeleteOrder(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_delete_order_status_code(self): # ca sa fac delete, trebuie sa am deja o comanda, asa ca fac mai intai submit order, pt ca imi trebuie si order id
        book_id = 1
        customer_name = "TA41"
        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = place_order_response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Error, unexpected status code")

        order_id = place_order_response.json()["orderId"]

        delete_order_response = self.books_api.delete_order(self.access_token, order_id)

        expected_delete_order_status_code = 204
        actual_delete_order_status_code = delete_order_response.status_code
        self.assertEqual(expected_delete_order_status_code, actual_delete_order_status_code, "Error, unexpected status code for deleted order")