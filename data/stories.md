## fallback
 - utter_unclear

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_did_that_help
* deny
  - utter_goodbye

## Fetch events 1
* ask_which_events
  - action_fetch_all_events
* mood_great
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_thanks

## Fetch events 2
* ask_which_events
  - action_fetch_all_events
* affirm
  - utter_next_help
* deny
  - utter_thanks

## Fetch events 3
* greet
  - utter_greet
* ask_which_events
  - action_fetch_all_events
* bye OR thank
  - utter_goodbye

## say goodbye
* thank
  - utter_thanks
* bye
  - utter_goodbye

## Event registration
* register_for_event
  - action_utter_event_link
* bye
  - utter_goodbye

## Story 3
* greet
  - utter_greet
* registration_details
  - action_utter_event_link
* bye
  - utter_goodbye

<!-- commented out
	## subscribe story happy
	* greet
	  - utter_greet
	* subscribe
	  - subscribe_form
	  - form{"name": "subscribe_form"}
	  - form{"name": null}
	  - utter_subscribe_slot_values
	*thank OR bye
	  - utter_goodbye
-->
