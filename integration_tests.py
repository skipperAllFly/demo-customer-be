import unittest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class TestAPIIntegration(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000"
        self.duffel_api_key = os.getenv('DUFFEL_API_KEY')

    def test_home_endpoint(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the backend!", response.json().get("message"))

    def test_duffel_flights_list_offers(self):
        if not self.duffel_api_key:
            self.skipTest("Duffel API key not set in environment variables")
        
        payload = {
            "slices": [
                {
                    "origin": "JFK",
                    "destination": "LAX",
                    "departure_date": "2023-12-01"
                }
            ],
            "passengers": [
                {
                    "type": "adult"
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/duffel-flights-list-offers", json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("offers", response.json())

    def test_fetch_flight_data(self):
        params = {
            "acid": "AA100",
            "outdate": "2023-12-01",
            "indate": "2023-12-02"
        }
        response = requests.get(f"{self.base_url}/fetch-flight-data", params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIn("flights", response.json())

if __name__ == "__main__":
    unittest.main()