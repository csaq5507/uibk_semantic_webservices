import os
import main
import unittest
import requests
import json

# run to test crud operations
class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get_events(self):
        response = self.app.get('/events')
        print(json.dumps(json.loads(response.data), indent=4))

    def test_add_event(self):
        entry = json.dumps({"title": "test_event", "date": "test_date"})
        response = self.app.post('/events', data=entry, content_type='application/json')
        if response.status_code != 201:
            print("bad response: {} \n{}".format(response.status_code, response.data))
            assert(False)
        print(json.dumps(json.loads(response.data), indent=4))

    def test_update_event(self):
        response = self.app.get('/events')
        existing_events = json.loads(response.data)["response"]
        ids = list(existing_events.keys())
        edit_event = existing_events[ids[0]]
        edit_event_id = ids[0]

        new_title = "rename that event"
        entry = json.dumps({"title": new_title})
        response = self.app.put('/events/{}'.format(edit_event_id), data=entry, content_type='application/json')
        if response.status_code != 200:
            print("bad response: {} \n{}".format(response.status_code, response.data))
            assert(False)

        renamed_event = json.loads(response.data)["response"]
        if renamed_event["title"] != new_title:
            print("Not renamed: {} \n{}".format(response.status_code, renamed_event))
            assert(False)

        print(json.dumps(json.loads(response.data), indent=4))
     
    def test_delete(self):
        response = self.app.get('/events')
        existing_events = json.loads(response.data)["response"]
        existing_event_count = len(existing_events)

        ids = list(existing_events.keys())
        edit_event = existing_events[ids[0]]
        edit_event_id = ids[0]

        response = self.app.delete('/events/{}'.format(edit_event_id))
        if response.status_code != 200:
            print("bad response: {} \n{}".format(response.status_code, response.data))
            assert(False)

        response = self.app.get('/events')
        new_event_count = len(json.loads(response.data)["response"])

        if existing_event_count != new_event_count + 1:
            print("Not deleted: {}".format(response.status_code))
            assert(False)



if __name__ == "__main__":
    unittest.main()