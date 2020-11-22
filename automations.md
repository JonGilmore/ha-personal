# Automations - Table of Contents
1.  [Security](#security) (61 automations)
1.  [Garage](#garage) (3 automations)
1.  [Location Awareness](#location-awareness) (1 automations)
1.  [Lutron Scene](#lutron-scene) (6 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Person Detection](#person-detection) (5 automations)
1.  [Lutron Pico](#lutron-pico) (4 automations)
1.  [HVAC](#hvac) (8 automations)
1.  [Unifi](#unifi) (5 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (5 automations)

⚠️ Total number of automations: **106** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L113)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L115)

### [Front door line crossing or doorbell rang - occupied](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L28)
  When its dark out & house occupied - foyer and exterior lights on

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L251)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L173)

### [Front door line crossing or doorbell rang - unoccupied](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L54)
  When its dark out & house unoccupied - foyer and exterior lights on for 10 min

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L251)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/timers.yaml#L2)

### [Turn off foyer and exterior lights 10 minutes after trigger](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L77)
*which uses:*
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/timers.yaml#L2)

### [Doorbell rang - play google home video](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L89)
  Play the front door video stream on the Google Home for 30 seconds

### [Doorbell rang - interrupt sonos master](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L105)
*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L190)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L121)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L177)

### [Deck lights on when deck door opens](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L137)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L156)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L177)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L171)
### [Wake up (only between Oct-May) & turn on some lights](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L186)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)

### [Motion light template](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L206)
  template for foyer & basement & bar & master toilet & evelyns lamp & storage & master toekick & office desk & gym

*which uses:*
-   [binary_sensor.evelyns_room_occupied](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L338)

### [Lifx lighting template - on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L289)
### [Lifx lighting template - off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L308)
### [Motion light template - scenes](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L331)
  Template to turn off basement & kitchen & deck

*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L52)

### [Enable motion light boolean 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L368)
### [Turn off lights between 11pm and 4am if alarm hasnt been set and no motion detected for 20 min on all motions](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L382)
*which uses:*
-   [binary_sensor.all_motions](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L87)

### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L404)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L14)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L419)
### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L434)
### [Fishtank lights](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L454)
### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L467)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L485)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L495)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L285)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L515)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off & recirc pump off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L523)
*which uses:*
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L12)

### [Start sleeping & check the garage doors](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L551)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)

### [Check the door locks](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L571)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L93)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L101)

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L592)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)

### [Turn the HVAC fans on & recirculation pump and tvs off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L608)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L251)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L133)

### [Away during the day & turn lights off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L625)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L251)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L638)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L251)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L656)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L268)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L8)

### [Turn on sunset2 lights at ten min after sunset](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L678)
### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L687)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L704)
### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L712)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L732)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L195)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L745)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L205)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L758)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L234)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L774)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L788)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L805)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L815)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_booleans.yaml#L16)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L863)
### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L882)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L27)

### [Doorbell notification event capture and notify](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L894)
### [General notifications](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L920)
*which uses:*
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L966)
### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L975)
### [Create all groups](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L988)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L999)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L173)

### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1014)
### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1030)
### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1042)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L276)

### [Acknowledge garage single open](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1054)
*which uses:*
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/alerts.yaml#L2)

### [Acknowledge garage double open](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1065)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/alerts.yaml#L19)

### [Lights off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1076)
  all lights off from iOS widget

### [Toggle garage - single](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1092)
*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/covers.yaml#L4)

### [Toggle garage - double](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1116)
*which uses:*
-   [cover.garage_momentary_double](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/covers.yaml#L13)

### [Unlock front door](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/automation.yaml#L1131)[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/garage.yaml#L3)
### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/garage.yaml#L18)
### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/sensors.yaml#L45)
[^ toc](#automations---table-of-contents)

## [Location Awareness](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/location.yaml)
### [Leave home & single garage open](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/location.yaml#L2)
  Leave `home` zone with the single garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/covers.yaml#L4)
[^ toc](#automations---table-of-contents)

## [Lutron Scene](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml)
### [Master lamps on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L1)
  LED is off & the scene is triggered - turn on the lamps and enable the LED

### [Master lamps off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L32)
  LED is on & the scene is triggered - turn off the lamps and disable the LED

### [Either master lamp on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L60)
  Either master lamp is turned on - enable the scene LED

### [Both master lamps off - jon](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L74)
  Both master lamps off, turn off the scene LED

### [Both master lamps off - laura](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L89)
  Both master lamps off, turn off the scene LED

### [Master lamps off from scene activation](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/lutron_scenes.yaml#L105)[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L290)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L290)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)
[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [shell_command.cam_vid_doorbell](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L11)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml#L34)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [shell_command.cam_vid_driveway](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L12)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml#L65)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [shell_command.cam_vid_deck](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L13)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml#L96)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [shell_command.cam_vid_deckstairs](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L14)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/person.yaml#L127)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [shell_command.cam_vid_garage](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L15)
[^ toc](#automations---table-of-contents)

## [Lutron Pico](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/picos.yaml)
### [Lauras lamp on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/picos.yaml#L1)
### [Jons lamp on](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/picos.yaml#L14)
### [Lauras lamp off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/picos.yaml#L27)
### [Jons lamp off](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/picos.yaml#L38)[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)
[^ toc](#automations---table-of-contents)

## [Unifi](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml)
### [Port forward enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L290)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L9)

### [Port forward disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L290)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L9)

### [Port forward enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L9)

### [Port forward disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L9)

### [Garage camera force reboot weekly](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/unifi.yaml#L79)
  garage cam kinda sucks and needs to be rebooted pretty often

*which uses:*
-   [shell_command.unifi_powercycle](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/shell_commands.yaml#L10)
[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L247)
[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/scripts.yaml#L211)
[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml)
### [Roof lights on (only in december)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml#L3)
### [Trees on (only in december) if occupied](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml#L14)
### [Turn off at 11pm (only in december)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml#L28)
### [Turn off when sleeping starts (only in december)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml#L39)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/includes/binary_sensors.yaml#L263)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/c1a5d6b12399d7527307bdf79ae9c4d6929fb61e/automation/xmas.yaml#L52)[^ toc](#automations---table-of-contents)
