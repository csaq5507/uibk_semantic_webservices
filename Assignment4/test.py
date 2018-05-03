import os
import main
import unittest
import requests
import json

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get_events(self):
        response = self.app.get('/events')
        payload = json.loads(response.get_data())
        print(payload)

    def test_add_event(self):
        entry = json.dumps({"name": "test_event", "date": "test_date"})
        response = self.app.post('/events', data=entry, content_type='application/json')
        if response.status_code != 201:
            assert(False)
            
        payload = json.loads(response.get_data())
        print(payload)

if __name__ == "__main__":
    unittest.main()