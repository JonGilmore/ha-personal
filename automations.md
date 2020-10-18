# Automations - Table of Contents
1.  [Security](#security) (67 automations)
1.  [Garage](#garage) (3 automations)
1.  [Location Awareness](#location-awareness) (1 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Person Detection](#person-detection) (5 automations)
1.  [HVAC](#hvac) (8 automations)
1.  [Unifi](#unifi) (5 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (6 automations)

⚠️ Total number of automations: **103** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L113)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L115)

### [Front door line crossing or doorbell rang - occupied](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L28)
  When its dark out & house occupied - foyer and exterior lights on

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L117)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L173)

### [Front door line crossing or doorbell rang - unoccupied](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L54)
  When its dark out & house unoccupied - foyer and exterior lights on for 10 min

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L117)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/timers.yaml#L2)

### [Turn off foyer and exterior lights 10 minutes after trigger](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L77)
*which uses:*
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/timers.yaml#L2)

### [Doorbell rang - play google home video](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L89)
  Play the front door video stream on the Google Home for 30 seconds

### [Doorbell rang - interrupt sonos master](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L105)
*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L190)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L121)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L175)

### [Deck lights off when no person detected for 10min](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L136)
### [Deck lights on when deck door opens](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L147)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L166)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L175)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L181)
### [Wake up (only between Oct-May) & turn on some lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L196)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)

### [Motion light template for foyer & basement & and bar](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L216)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L2)

### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L252)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L270)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L280)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L288)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L300)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L308)
*which uses:*
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L12)

### [Start sleeping & check the garage doors](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L334)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)

### [Check the door locks](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L354)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L93)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L101)

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L375)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)

### [Turn the HVAC fans on & recirculation pump and tvs off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L391)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L117)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L133)

### [Away during the day & turn lights off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L408)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L117)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L421)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L117)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L439)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L8)

### [Turn on sunset2 lights at ten min after sunset](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L461)
### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L470)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L487)
### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L495)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L515)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L193)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L528)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L203)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L541)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L100)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L557)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L571)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L588)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L598)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L16)

### [Master entry motion light when master bed is unoccupied](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L613)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L288)

### [Master entry motion lights Off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L631)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L18)

### [Sitting motion light](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L653)
### [Sitting motion light off when master override is off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L667)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L18)

### [Sitting light off when chair unoccupied (& bed occupied)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L700)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L288)
-   [sensor.master_sitting_chair_occupied](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L277)

### [Kitchen lights off with no motion for 30 minutes](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L719)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L2)

### [Enable motion lights 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L767)
### [Disable motion lights 2hours sunrise](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L775)
### [Turn off lights between 10pm and 4am if alarm hasnt been set and no motion detected for 20 min on all motions](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L784)
*which uses:*
-   [binary_sensor.all_motions](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L71)

### [Kitchen motion light](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L799)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)

### [Basement lights off with no motion](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L817)
*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L52)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L829)
### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L848)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_booleans.yaml#L14)

### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L863)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L27)

### [Doorbell notification event capture and notify](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L875)
### [General notifications](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L901)
*which uses:*
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L947)
### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L956)
### [Create all groups](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L969)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L980)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L173)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L995)
### [Storage & master toekick motion lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1010)
### [Office desk & gym lights motion on](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1041)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L134)

### [Office desk & gym lights motion off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1063)
### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1086)
### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1102)
### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1114)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L142)

### [Acknowledge garage single open](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1126)
*which uses:*
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/alerts.yaml#L2)

### [Acknowledge garage double open](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1137)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/alerts.yaml#L19)

### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1148)
### [Fishtank lights](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/automation.yaml#L1168)[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/garage.yaml#L3)
### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/garage.yaml#L18)
### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/sensors.yaml#L45)
[^ toc](#automations---table-of-contents)

## [Location Awareness](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/location.yaml)
### [Leave home & single garage open](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/location.yaml#L2)
  Leave `home` zone with the single garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/covers.yaml#L4)
[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L156)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L156)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)
[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [shell_command.cam_vid_doorbell](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L11)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml#L34)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [shell_command.cam_vid_driveway](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L12)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml#L65)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [shell_command.cam_vid_deck](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L13)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml#L96)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [shell_command.cam_vid_deckstairs](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L14)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/person.yaml#L127)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [shell_command.cam_vid_garage](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L15)
[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)
[^ toc](#automations---table-of-contents)

## [Unifi](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml)
### [Port forward enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L156)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L9)

### [Port forward disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L156)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L9)

### [Port forward enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L9)

### [Port forward disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L9)

### [Garage camera force reboot weekly](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/unifi.yaml#L79)
  garage cam kinda sucks and needs to be rebooted pretty often

*which uses:*
-   [shell_command.unifi_powercycle](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/shell_commands.yaml#L10)
[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L113)
[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/scripts.yaml#L211)
[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml)
### [Roof lights on (only in december)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L3)
### [Trees on (only in december) if occupied](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L14)
### [Turn off at 11pm (only in december)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L28)
### [Turn off when sleeping starts (only in december)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L39)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/includes/binary_sensors.yaml#L129)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L52)
### [Turn off when laura gets in bed (only in december)](https://github.com/jongilmore/ha-personal/blob/2110267044f27182e3bbd41e11a94ebba44ca071/automation/xmas.yaml#L76)[^ toc](#automations---table-of-contents)
