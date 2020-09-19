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

## say goodbye
* bye
  - utter_goodbye

## Story 1
* greet
  - utter_greet
* ask_which_events
  - action_fetch_all_events
* bye OR thank
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