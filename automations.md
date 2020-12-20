# Automations - Table of Contents
1.  [Security](#security) (10 automations)
1.  [Automatic Lighting](#automatic-lighting) (15 automations)
1.  [Blinds](#blinds) (3 automations)
1.  [Utility](#utility) (4 automations)
1.  [Night Mode](#night-mode) (5 automations)
1.  [Wake Mode](#wake-mode) (1 automations)
1.  [Away Mode](#away-mode) (3 automations)
1.  [Home Mode](#home-mode) (1 automations)
1.  [Fans](#fans) (3 automations)
1.  [HVAC](#hvac) (10 automations)
1.  [Moisture](#moisture) (1 automations)
1.  [Alarm](#alarm) (3 automations)
1.  [Notification](#notification) (3 automations)
1.  [Presence](#presence) (1 automations)
1.  [Work](#work) (2 automations)
1.  [iOS Actions](#ios-actions) (4 automations)
1.  [Garage](#garage) (3 automations)
1.  [Location Awareness](#location-awareness) (1 automations)
1.  [Lutron Scene](#lutron-scene) (6 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Nest](#nest) (1 automations)
1.  [Person Detection](#person-detection) (7 automations)
1.  [Lutron Pico](#lutron-pico) (4 automations)
1.  [Rhasspy](#rhasspy) (2 automations)
1.  [Unifi](#unifi) (5 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (6 automations)

⚠️ Total number of automations: **112** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L113)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L115)

### [Front door line crossing or doorbell rang - occupied](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L28)
  When its dark out & house occupied - foyer and exterior lights on

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L286)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L173)

### [Front door line crossing or doorbell rang - unoccupied](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L54)
  When its dark out & house unoccupied - foyer and exterior lights on for 10 min

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L286)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/timers.yaml#L2)

### [Turn off foyer and exterior lights 10 minutes after trigger](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L77)
*which uses:*
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/timers.yaml#L2)

### [Doorbell rang - play google home video](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L89)
  Play the front door video stream on the Google Home for 30 seconds

*which uses:*

-   Entity not defined in YAML

### [Doorbell rang - interrupt sonos master](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L105)
*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L190)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L121)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L179)

### [Deck lights on when deck door opens](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L136)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L155)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L179)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L170)
*which uses:*

-   Entity not defined in YAML

### [Wake up (only between Oct-May) & turn on some lights](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L185)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)

### [Motion light template](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L205)
  template for foyer & basement & bar & master toilet & evelyns lamp & storage & master toekick & office desk & gym

*which uses:*
-   [binary_sensor.evelyns_room_occupied](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L373)

### [Lifx lighting template - on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L288)
*which uses:*

-   Entity not defined in YAML

### [Lifx lighting template - off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L307)
*which uses:*

-   Entity not defined in YAML

### [Motion light template - scenes](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L330)
  Template to turn off basement & kitchen & deck

*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L52)

### [Enable motion light boolean 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L370)
*which uses:*

-   Entity not defined in YAML

### [Turn off lights between 11pm and 4am if alarm hasnt been set and no motion detected for 20 min on all motions](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L384)
*which uses:*
-   [binary_sensor.all_motions](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L87)

### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L406)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L14)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L421)
*which uses:*

-   Entity not defined in YAML

### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L436)
*which uses:*

-   Entity not defined in YAML

### [Fishtank lights](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L456)
*which uses:*

-   Entity not defined in YAML

### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L469)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L487)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L497)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L287)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L517)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off & recirc pump off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L525)
*which uses:*
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L12)

### [Start sleeping & check the garage doors](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L553)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)

### [Check the door locks](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L573)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L93)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L101)

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L594)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)

### [Turn the HVAC fans on & recirculation pump and tvs off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L610)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L286)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L133)

### [Away during the day & turn lights off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L627)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L286)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L640)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L286)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L658)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L303)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L8)

### [Turn on sunset2 lights at ten min after sunset](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L680)
*which uses:*

-   Entity not defined in YAML

### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L689)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L706)
*which uses:*

-   Entity not defined in YAML

### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L714)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L734)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L197)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L747)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L207)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L760)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L269)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L776)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L790)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L807)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L817)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_booleans.yaml#L16)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L865)
*which uses:*

-   Entity not defined in YAML

### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L884)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L27)

### [Doorbell notification event capture and notify](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L896)
*which uses:*

-   Entity not defined in YAML

### [General notifications](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L922)
*which uses:*
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L974)
*which uses:*

-   Entity not defined in YAML

### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L983)
*which uses:*

-   Entity not defined in YAML

### [Create all groups](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L996)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1007)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L173)

### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1022)
*which uses:*

-   Entity not defined in YAML

### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1038)
*which uses:*

-   Entity not defined in YAML

### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1050)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L311)

### [Acknowledge garage single open](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1062)
*which uses:*
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/alerts.yaml#L2)

### [Acknowledge garage double open](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1073)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/alerts.yaml#L19)

### [Lights off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1084)
  all lights off from iOS widget

*which uses:*

-   Entity not defined in YAML

### [Toggle garage - single](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1100)
*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/covers.yaml#L4)

### [Toggle garage - double](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1124)
*which uses:*
-   [cover.garage_momentary_double](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/covers.yaml#L13)

### [Unlock front door](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/automation.yaml#L1139)
*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/garage.yaml#L3)
*which uses:*

-   Entity not defined in YAML

### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/garage.yaml#L18)
*which uses:*

-   Entity not defined in YAML

### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/sensors.yaml#L45)

[^ toc](#automations---table-of-contents)

## [Location Awareness](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/location.yaml)
### [Leave home & single garage open](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/location.yaml#L2)
  Leave `home` zone with the single garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/covers.yaml#L4)

[^ toc](#automations---table-of-contents)

## [Lutron Scene](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml)
### [Master lamps on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L1)
  LED is off & the scene is triggered - turn on the lamps and enable the LED

*which uses:*

-   Entity not defined in YAML

### [Master lamps off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L32)
  LED is on & the scene is triggered - turn off the lamps and disable the LED

*which uses:*

-   Entity not defined in YAML

### [Either master lamp on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L60)
  Either master lamp is turned on - enable the scene LED

*which uses:*

-   Entity not defined in YAML

### [Both master lamps off - jon](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L74)
  Both master lamps off, turn off the scene LED

*which uses:*

-   Entity not defined in YAML

### [Both master lamps off - laura](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L89)
  Both master lamps off, turn off the scene LED

*which uses:*

-   Entity not defined in YAML

### [Master lamps off from scene activation](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/lutron_scenes.yaml#L105)
*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L325)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L325)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

[^ toc](#automations---table-of-contents)

## [Nest](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/nest.yaml)
### [Testing](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/nest.yaml#L2)
  Testing nest events

*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_doorbell](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L11)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L34)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_driveway](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L12)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L65)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_deck](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L13)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L96)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_deckstairs](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L14)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L127)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_garage](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L15)

### [Kitchen person detected](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L158)
  If nobody is home - send a video of the kitchen

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [shell_command.cam_vid_kitchen](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L16)

### [Testing person picture](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/person.yaml#L189)
*which uses:*
-   [binary_sensor.deck_person](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L115)
-   [binary_sensor.deckstairs_person](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L120)
-   [binary_sensor.doorbell_person](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L125)

[^ toc](#automations---table-of-contents)

## [Lutron Pico](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/picos.yaml)
### [Lauras lamp on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/picos.yaml#L1)
*which uses:*

-   Entity not defined in YAML

### [Jons lamp on](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/picos.yaml#L14)
*which uses:*

-   Entity not defined in YAML

### [Lauras lamp off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/picos.yaml#L27)
*which uses:*

-   Entity not defined in YAML

### [Jons lamp off](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/picos.yaml#L38)
*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Rhasspy](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/rhasspy.yaml)
### [Lights](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/rhasspy.yaml#L2)
  Testing rhasspy local voice processing

*which uses:*

-   Entity not defined in YAML

### [Scenes](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/rhasspy.yaml#L27)
  Testing rhasspy local voice processing

*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

[^ toc](#automations---table-of-contents)

## [Unifi](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml)
### [Port forward enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L325)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L9)

### [Port forward disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L325)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L9)

### [Port forward enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L9)

### [Port forward disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L9)

### [Garage camera force reboot weekly](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/unifi.yaml#L79)
  garage cam kinda sucks and needs to be rebooted pretty often

*which uses:*
-   [shell_command.unifi_powercycle](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/shell_commands.yaml#L10)

[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L282)

[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_selects.yaml#L2)
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/scripts.yaml#L211)

[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml)
### [Roof lights on (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L3)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)

### [Trees on (only when xmas boolean on) if occupied](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L15)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)

### [Turn off at 11pm (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L30)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)

### [Turn off when sleeping starts (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L42)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L298)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L56)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)

### [Turn off when laura gets in bed (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/automation/xmas.yaml#L81)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/21789f7fcc11561220972d6253a94e9635e77f44/includes/binary_sensors.yaml#L379)

[^ toc](#automations---table-of-contents)
