# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from rasa_sdk.forms import FormAction


# class SubscribeForm(FormAction):

#     def name(self):
#         return "subscribe_form"

#     @staticmethod
#     def required_slots(tracker):
#         return [
#             "name",
#             "email",
#         ]

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         name = tracker.get_slots('name')
#         email = tracker.get_slots('email')

#         # save users details in subscription_db

#         dispatcher.utter_message(
#             "Thanks for subscribing")
#         return []

import requests
from rasa_sdk import Action
import json

# events = {  # fetched from API
#     1: {
#         "title": "MLFiesta",
#         "link": "https://example.com/mlfiesta",
#     },
#     2: {
#         "title": "Hackathon",
#         "link": "https://example.com/hackathon",
#     },
#     3: {
#         "title": "Android Workshop",
#         "link": "https://example.com/android",
#     },
# }

fetched = requests.get(
    "https://us-central1-dsc-cgu.cloudfunctions.net/events/api/event-details")


fetched_events = json.loads(fetched.text)


# Action to utter all events
class FetchEventsAction(Action):

    def name(self):
        return "action_fetch_all_events"

    def run(self, dispatcher, tracker, domain):

        # some api stuff here

        dispatcher.utter_message("List of all events are as follows: ")
        # Display events
        for idx, event in enumerate(fetched_events):
            dispatcher.utter_message(f"{idx + 1}. {event['EventTitle']}")
            dispatcher.utter_message(
                f"Description: {event['EventDescription']}")

        return []

# Action to utter event link


class EventLinkAction(Action):
    def name(self):
        return "action_utter_event_link"

    def run(self, dispatcher, tracker, domain):

        event_id = tracker.get_slots("event_id")
        for event in fetched_events:
            if event['EventId'] == event_id:
                cur_event = event
                break
        dispatcher.utter_message(
            f"Link for {cur_event['EventTitle']}: {cur_event['EventLink']}")

        return []


class ContactAction(Action):
    def name(self):
        return "action_utter_contact_details"

    def run(self, dipatcher, tracker, domain):

        department = tracker.get_slots("department")
        core_mem_name = tracker.get_slot("core_member_name")

        # Search for contact details

        # Contact details not available yet


feedback_url = 'xyz'  # API endpoint for feedback


class FeedbackAction(Action):
    def name(self):
        return "action_utter_take_feedback"

    def run(self, dispatcher, tracker, domain):

        name = tracker.get_slots("name")
        email = tracker.get_slots("email")
        msg = tracker.latest_message.text

        requests.post(feedback_url, data={
                      "name": name, "email": email, "message": msg})
