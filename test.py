import os
import main
import unittest
import requests
import json

# run to test crud operations
class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()


    #################################################################################
    # Test fetch all events
    # -------------------------------------------------------------------------------
    # Steps:
    #  1) get all events
    #################################################################################
    def test_get_events(self):
        response = self.app.get('/events')
        print(json.dumps(json.loads(response.data), indent=4))


    #################################################################################
    # Test add event
    # -------------------------------------------------------------------------------
    # Steps:
    #  1) get all events
    #  2) add event
    #  2) get all events and check if added
    #################################################################################
    def test_add_event(self):

        response = self.app.get('/events')
        events_before = json.loads(response.data)["response"]

        entry = json.dumps({"title": "test_event", "date": "test_date"})
        response = self.app.post('/events', data=entry, content_type='application/json')
        if response.status_code != 201:
            print("bad response: {} \n{}".format(response.status_code, response.data))
            assert(False)
        print(json.dumps(json.loads(response.data), indent=4))

        
        response = self.app.get('/events')
        events_after = json.loads(response.data)["response"]
        if len(events_after) != len(events_before) + 1:
            print("bad response: add failed{} \n{}")
            assert(False)



    #################################################################################
    # Test update
    # -------------------------------------------------------------------------------
    # Steps:
    #  1) get all events
    #  2) change title of first event
    #  2) fetch first event and compare title
    #################################################################################
    def test_update_event(self):
        response = self.app.get('/events')
        existing_events = json.loads(response.data)["response"]

        edit_event = existing_events[0]
        edit_event_id = edit_event["id"]

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
     



    #################################################################################
    # Test deletion
    # -------------------------------------------------------------------------------
    # Steps:
    #  1) get all events
    #  2) delete one event
    #  3) get all events
    #  4) check if exactly one element got deleted
    #################################################################################
    def test_delete(self):
        response = self.app.get('/events')
        existing_events = json.loads(response.data)["response"]
        existing_event_count = len(existing_events)

        edit_event = existing_events[0]

        response = self.app.delete('/events/{}'.format(edit_event["id"]))
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