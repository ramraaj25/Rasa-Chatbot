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

## help 1
* ask_which_events
  - utter_next_help
* mood_great
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_thanks

## help 2
* ask_which_events
  - utter_next_help
* mood_unhappy
  - utter_did_that_help
* deny
  - utter_sorry

## say goodbye
* thank
  - utter_thanks
* bye
  - utter_goodbye

## Story 1
* greet
  - utter_greet
* ask_which_events
  - action_fetch_all_events
* bye OR thank
  - utter_goodbye

## Story 2
* greet
  - utter_greet
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
