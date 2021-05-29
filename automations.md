# Automations - Table of Contents
1.  [Security](#security) (6 automations)
1.  [Automatic Lighting](#automatic-lighting) (14 automations)
1.  [Wake Mode](#wake-mode) (1 automations)
1.  [Blinds](#blinds) (3 automations)
1.  [Utility](#utility) (4 automations)
1.  [Night Mode](#night-mode) (3 automations)
1.  [Away Mode](#away-mode) (2 automations)
1.  [Home Mode](#home-mode) (1 automations)
1.  [Fans](#fans) (3 automations)
1.  [HVAC](#hvac) (10 automations)
1.  [Moisture](#moisture) (1 automations)
1.  [Alarm](#alarm) (3 automations)
1.  [Notification](#notification) (2 automations)
1.  [Presence](#presence) (1 automations)
1.  [Work](#work) (2 automations)
1.  [iOS Actions](#ios-actions) (2 automations)
1.  [Person Detection](#person-detection) (6 automations)
1.  [Frigate](#frigate) (2 automations)
1.  [Garage](#garage) (3 automations)
1.  [Location Awareness](#location-awareness) (1 automations)
1.  [Lutron Scene](#lutron-scene) (7 automations)
1.  [Monitor](#monitor) (6 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Nest](#nest) (1 automations)
1.  [Lutron Pico](#lutron-pico) (4 automations)
1.  [Rhasspy](#rhasspy) (2 automations)
1.  [Unifi](#unifi) (6 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (6 automations)

⚠️ Total number of automations: **110** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L113)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L115)

### [Front door line crossing or doorbell rang](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L28)
  When its dark out - foyer and exterior lights on - handles both occupied & unoccupied states

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L249)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L266)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L173)

### [Doorbell rang](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L58)
  send telegram & if master sonos is playing announce the doorbell & play video stream on the main display

*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L190)
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L113)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L90)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L179)

### [Deck lights on when deck door opens](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L105)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L266)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L124)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L179)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L139)
*which uses:*

-   Entity not defined in YAML

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L154)
  also checks if date is between Oct-May & turn on some lights

*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L266)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)

### [Motion light template](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L186)
  template for foyer & basement & bar & master toilet & evelyns lamp & storage & master toekick & office desk & gym

*which uses:*
-   [binary_sensor.evelyns_room_occupied](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L336)
-   [binary_sensor.loft_occupied](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L342)

### [Mbr lighting template - on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L265)
  dont trigger this between midnight and 6:00am

*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L24)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L24)

### [Mbr lighting template - off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L290)
*which uses:*

-   Entity not defined in YAML

### [Motion light template - scenes](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L312)
  Template to turn off basement & kitchen & deck

*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L45)

### [Enable motion light boolean 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L352)
*which uses:*

-   Entity not defined in YAML

### [Turn off lights between 11pm and 4am if alarm hasnt been set and no motion detected for 20 min on all motions](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L366)
*which uses:*
-   [binary_sensor.all_motions](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L80)

### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L388)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L14)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L403)
*which uses:*

-   Entity not defined in YAML

### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L418)
*which uses:*

-   Entity not defined in YAML

### [Fishtank lights](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L438)
*which uses:*

-   Entity not defined in YAML

### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L451)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L469)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L479)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L287)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L499)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off & recirc pump off & enable driveway notify](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L507)
  also check garage doors and locks - notify if they are open or unlocked

*which uses:*
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L12)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L93)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L101)

### [Turn the HVAC fans on & recirculation pump & tvs off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L569)
  also if its still bright inside, turn off all lights

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L249)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L266)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L133)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L593)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L249)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L611)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L266)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L8)

### [Turn on sunset2 lights at ten min after sunset](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L633)
*which uses:*

-   Entity not defined in YAML

### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L642)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L659)
*which uses:*

-   Entity not defined in YAML

### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L667)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L687)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L197)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L700)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L207)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L713)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L232)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L729)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L743)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L760)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L770)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L16)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L818)
*which uses:*

-   Entity not defined in YAML

### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L837)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L27)

### [General notifications](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L866)
*which uses:*
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L921)
*which uses:*

-   Entity not defined in YAML

### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L930)
*which uses:*

-   Entity not defined in YAML

### [Create all groups](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L943)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L954)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L173)

### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L969)
*which uses:*

-   Entity not defined in YAML

### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L986)
*which uses:*

-   Entity not defined in YAML

### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L998)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L274)

### [Acknowledge garage open](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L1010)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/alerts.yaml#L19)
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/alerts.yaml#L2)

### [Toggle garage - single](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L1030)
*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/covers.yaml#L4)

### [Unlock front door](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/automation.yaml#L1045)
*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L33)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L63)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L93)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L123)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Kitchen person detected](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L153)
  If nobody is home - send a video of the kitchen

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [shell_command.trim_video](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L12)

### [Disable driveway notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L266)
  options to mute notifications for 60m or the rest of the day

*which uses:*
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)

### [Driveway notification](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/frigate.yaml#L300)
  only notify for `new` events with a 90s rate limit, optionally mute notifications for 60m with telegram callback

*which uses:*
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)
-   [input_boolean.frigate_driveway_notifier](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_booleans.yaml#L20)

[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/garage.yaml#L3)
*which uses:*

-   Entity not defined in YAML

### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/garage.yaml#L18)
*which uses:*

-   Entity not defined in YAML

### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/sensors.yaml#L45)

[^ toc](#automations---table-of-contents)

## [Location Awareness](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/location.yaml)
### [Leave home & single garage open](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/location.yaml#L2)
  Leave `home` zone with the single garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/covers.yaml#L4)

[^ toc](#automations---table-of-contents)

## [Lutron Scene](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml)
### [Master lamps on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L1)
  LED is off & the scene is triggered - turn on the lamps and enable the LED

*which uses:*

-   Entity not defined in YAML

### [Master lamps off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L32)
  LED is on & the scene is triggered - turn off the lamps and disable the LED

*which uses:*

-   Entity not defined in YAML

### [Either master lamp on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L60)
  Either master lamp is turned on - enable the scene LED

*which uses:*

-   Entity not defined in YAML

### [Both master lamps off - jon](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L74)
  Both master lamps off, turn off the scene LED

*which uses:*

-   Entity not defined in YAML

### [Both master lamps off - laura](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L89)
  Both master lamps off, turn off the scene LED

*which uses:*

-   Entity not defined in YAML

### [Master lamps off from scene activation](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L105)
*which uses:*

-   Entity not defined in YAML

### [Jons keypad all off pressed](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/lutron_scenes.yaml#L191)
  the `all off` scene is triggered on jons keypad - also turn off the master motion lamps

*which uses:*
-   [script.master_off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L463)

[^ toc](#automations---table-of-contents)

## [Monitor](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml)
### [Jon occupancy on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L6)
*which uses:*

-   Entity not defined in YAML

### [Jon occupancy off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L17)
*which uses:*

-   Entity not defined in YAML

### [Laura occupancy on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L28)
*which uses:*

-   Entity not defined in YAML

### [Laura occupancy off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L39)
*which uses:*

-   Entity not defined in YAML

### [Restart Monitor service on HA startup](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L51)
*which uses:*

-   Entity not defined in YAML

### [Departure scan](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/monitor.yaml#L129)
*which uses:*
-   [binary_sensor.front_door](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L158)
-   [binary_sensor.garage_doors](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L218)
-   [script.scan_bt_depart](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L425)

[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L288)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L288)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

[^ toc](#automations---table-of-contents)

## [Nest](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/nest.yaml)
### [Testing](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/nest.yaml#L2)
  Testing nest events

*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Lutron Pico](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/picos.yaml)
### [Lauras lamp on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/picos.yaml#L1)
*which uses:*

-   Entity not defined in YAML

### [Jons lamp on](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/picos.yaml#L14)
*which uses:*

-   Entity not defined in YAML

### [Lauras lamp off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/picos.yaml#L27)
*which uses:*

-   Entity not defined in YAML

### [Jons lamp off](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/picos.yaml#L38)
*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [Rhasspy](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/rhasspy.yaml)
### [Lights](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/rhasspy.yaml#L2)
  Testing rhasspy local voice processing

*which uses:*

-   Entity not defined in YAML

### [Scenes](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/rhasspy.yaml#L27)
  Testing rhasspy local voice processing

*which uses:*

-   Entity not defined in YAML

[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

[^ toc](#automations---table-of-contents)

## [Unifi](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml)
### [Port forward enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L288)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L9)

### [Port forward disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L288)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L9)

### [Port forward enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L9)

### [Port forward disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L9)

### [Garage camera force reboot weekly](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L79)
  garage cam kinda sucks and needs to be rebooted pretty often

*which uses:*
-   [shell_command.unifi_powercycle](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L10)

### [Theatre ap reboot](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/unifi.yaml#L98)
  testing an access point reboot

*which uses:*
-   [shell_command.unifi_powercycle_device](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/shell_commands.yaml#L11)

[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L245)

[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_selects.yaml#L2)
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/scripts.yaml#L211)

[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml)
### [Roof lights on (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L3)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)

### [Trees on (only when xmas boolean on) if occupied](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L15)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)

### [Turn off at 11pm (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L30)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)

### [Turn off when sleeping starts (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L42)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L261)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L56)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)

### [Turn off when laura gets in bed (only when xmas boolean on)](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/automation/xmas.yaml#L81)
*which uses:*
-   [binary_sensor.christmas_season](https://github.com/jongilmore/ha-personal/blob/7b5483f4829102eb1094f671679dc870647c9440/includes/binary_sensors.yaml#L356)

[^ toc](#automations---table-of-contents)
