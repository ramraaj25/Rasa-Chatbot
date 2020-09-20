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

from rasa_sdk import action

events = {  # fetched from API
    1: {
        "title": "MLFiesta",
        "link": "https://example.com/mlfiesta",
    },
    2: {
        "title": "Hackathon",
        "link": "https://example.com/hackathon",
    },
    3: {
        "title": "Android Workshop",
        "link": "https://example.com/android",
    },
}


# Action to utter all events
class FetchEventsAction(Action):

    def name(self):
        return "action_fetch_all_events"

    def run(self, dispatcher, tracker, domain):

        # some api stuff here

        dispatcher.utter_message("List of all events are as follows: ")
        # Display events
        for idx, event_id in enumerate(events):
            dispatcher.utter_message(f"{idx + 1}. {events[event_id]['title']}")

        return []

# Action to utter event link


class EventLinkAction(Action):
    def name(self):
        return "action_utter_event_link"

    def run(self, dispatcher, tracker, domain):

        event_id = tracker.get_slots("event_id")
        event = events[event_id]
        dispatcher.utter_message(f"Link for {event['title']}: {event['link']}")

        return []
