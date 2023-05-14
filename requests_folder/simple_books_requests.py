import requests
import random

class SimpleBooksRequests:
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _ORDERS_ENDPOINT = "/orders"

    def generate_token(self):
        random_number = random.randint(1, 99999999999999999)

        request_body = {
            "clientName": "Postman",
            "clientEmail": f"testautomation{random_number}@example.com"
        }

        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT
        response = requests.post(auth_url, json=request_body)
        token = response.json()["accessToken"]

        return token

    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_all_books(self, book_type="",limit=""):  # parametrii default, nu sunt obligat sa ii definesc daca nu vreau sa-i folosesc
        # situatia in care vrem toate cartile de la URL-ul https://simple-books-api.glitch.me/books
        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT

        # situatia in care vrem cartile cu type=ceva de la URL-ul https://simple-books-api.glitch.me/books?type=fiction
        if book_type != "" and limit == "":
            get_all_books_url = get_all_books_url + f"?type={book_type}"

        # situatia in care vrem cartile cu limit=ceva de la URL-ul https://simple-books-api.glitch.me/books?limit=2
        elif book_type == "" and limit != "":
            get_all_books_url = get_all_books_url + f"?limit={limit}"

        # situatia in care vrem cartile cu type=ceva si limit=ceva de la URL-ul https://simple-books-api.glitch.me/books?type=fiction&limit=2
        elif book_type != "" and limit != "":
            get_all_books_url = get_all_books_url + f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)

        return response

    def submit_order(self, access_token, book_id, customer_name):
        submit_orders_url = self._BASE_URL + self._ORDERS_ENDPOINT

        header_params = {
            "Authorization": access_token
        }

        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        response = requests.post(submit_orders_url, json=request_body, headers=header_params)

        return response

    def update_order(self, access_token, order_id, new_customer_name):
        update_order_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {
            "Authorization": access_token
        }

        request_body = {
            "customerName": new_customer_name
        }
        response = requests.patch(update_order_url, json=request_body, headers=header_params)

        return response

    def delete_order(self, access_token, order_id):
        delete_order_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {
            "Authorization": access_token
        }
        response = requests.delete(delete_order_url, headers=header_params)

        return response
