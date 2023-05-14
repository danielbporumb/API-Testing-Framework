import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_update_order_status_code(self): # ca sa fac update, trebuie sa am deja o comanda, asa ca fac mai intai submit order, pt ca imi trebuie si order id
        book_id = 1
        customer_name = "TA41"
        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = place_order_response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Error, unexpected status code")

        order_id = place_order_response.json()["orderId"]

        new_customer_name = "TA41_updated"
        updated_order_response = self.books_api.update_order(self.access_token, order_id, new_customer_name)

        expected_update_order_status_code = 204
        actual_update_order_status_code = updated_order_response.status_code
        self.assertEqual(expected_update_order_status_code, actual_update_order_status_code, "Error, unexpected status code")
