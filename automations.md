# Automations - Table of Contents
1.  [Security](#security) (68 automations)
1.  [Garage](#garage) (3 automations)
1.  [Location Awareness](#location-awareness) (2 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Person Detection](#person-detection) (5 automations)
1.  [HVAC](#hvac) (8 automations)
1.  [Unifi](#unifi) (5 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (6 automations)

⚠️ Total number of automations: **105** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L113)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L115)

### [Front door line crossing or doorbell rang - occupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L28)
  When its dark out & house occupied - foyer and exterior lights on

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L173)

### [Front door line crossing or doorbell rang - unoccupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L54)
  When its dark out & house unoccupied - foyer and exterior lights on for 10 min

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/timers.yaml#L2)

### [Turn off foyer and exterior lights 10 minutes after trigger](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L77)
*which uses:*
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/timers.yaml#L2)

### [Doorbell rang - play google home video](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L89)
  Play the front door video stream on the Google Home for 30 seconds

### [Doorbell rang - interrupt sonos master](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L105)
*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L190)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L121)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L175)

### [Deck lights off when no person detected for 10min](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L136)
### [Deck lights on when deck door opens](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L147)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L166)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L175)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L181)
### [Wake up (only between Oct-May) & turn on some lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L196)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)

### [Motion light template for foyer & basement & and bar](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L216)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L2)

### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L252)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L270)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L280)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L288)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L300)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & turn off recirculation pump & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L308)
*which uses:*
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L12)

### [Start sleeping & check the garage doors](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L336)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)

### [Check the door locks](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L356)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L93)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L101)

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L377)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)

### [Turn the HVAC fans on & recirculation pump and tvs off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L393)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L133)

### [Away during the day & turn lights off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L410)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L423)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L441)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L8)

### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L463)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L480)
### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L488)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L508)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L193)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L521)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L203)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L534)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L83)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L550)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L564)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L581)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L591)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L16)

### [Master entry motion light when master bed is unoccupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L606)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L288)

### [Master entry motion lights Off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L624)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L18)

### [Sitting motion light when master bed is unoccupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L646)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L288)

### [Sitting motion light off when master override is off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L662)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L18)

### [Sitting light off when bed occupied (& chair unoccupied)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L677)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L288)
-   [sensor.master_sitting_chair_occupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L277)

### [Sitting light off when chair unoccupied (& bed occupied)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L695)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L288)
-   [sensor.master_sitting_chair_occupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L277)

### [Kitchen lights off with no motion for 15 minutes](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L714)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L2)

### [Daisy cam photo every 45 minutes when armed away and kennel closed](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L729)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/timers.yaml#L4)

### [Daisy timer completed](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L744)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L100)
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L15)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/timers.yaml#L4)

### [Enable motion lights 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L762)
### [Disable motion lights 2hours sunrise](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L770)
### [Kitchen motion light](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L779)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)

### [Basement lights off with no motion](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L795)
*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L52)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L807)
### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L826)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_booleans.yaml#L14)

### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L841)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L27)

### [Doorbell notification event capture and notify](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L853)
### [General notifications](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L879)
*which uses:*
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L925)
### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L934)
### [Create all groups](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L947)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L958)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L173)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L973)
### [Storage & master toekick motion lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L988)
### [Office desk & gym lights motion on](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1019)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L117)

### [Office desk & gym lights motion off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1041)
### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1064)
### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1080)
### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1092)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L125)

### [Acknowledge garage single open](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1104)
*which uses:*
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/alerts.yaml#L2)

### [Acknowledge garage double open](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1115)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/alerts.yaml#L19)

### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1126)
### [Fishtank lights](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/automation.yaml#L1146)[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/garage.yaml#L3)
### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/garage.yaml#L18)
### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/sensors.yaml#L45)
[^ toc](#automations---table-of-contents)

## [Location Awareness](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/location.yaml)
### [Leave home & single garage open](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/location.yaml#L2)
  Leave `home` zone with the single garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_single](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/covers.yaml#L4)

### [Leave home & double garage open](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/location.yaml#L25)
  Leave `home` zone with the double garage open, send a photo notification & prompt to close

*which uses:*
-   [cover.garage_momentary_double](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/covers.yaml#L13)
[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L139)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L139)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)
[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [shell_command.cam_vid_doorbell](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L11)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml#L34)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [shell_command.cam_vid_driveway](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L12)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml#L65)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [shell_command.cam_vid_deck](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L13)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml#L96)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [shell_command.cam_vid_deckstairs](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L14)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/person.yaml#L127)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [shell_command.cam_vid_garage](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L15)
[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)
[^ toc](#automations---table-of-contents)

## [Unifi](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml)
### [Port forward enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L139)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L9)

### [Port forward disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L139)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L9)

### [Port forward enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L9)

### [Port forward disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L9)

### [Garage camera force reboot weekly](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/unifi.yaml#L79)
  garage cam kinda sucks and needs to be rebooted pretty often

*which uses:*
-   [shell_command.unifi_powercycle](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/shell_commands.yaml#L10)
[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L96)
[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/scripts.yaml#L211)
[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml)
### [Roof lights on (only in december)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L3)
### [Trees on (only in december) if occupied](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L14)
### [Turn off at 11pm (only in december)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L28)
### [Turn off when sleeping starts (only in december)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L39)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/includes/binary_sensors.yaml#L112)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L52)
### [Turn off when laura gets in bed (only in december)](https://github.com/jongilmore/ha-personal/blob/fad804d9236a0be9bbeccae72263648c2d3e8c5d/automation/xmas.yaml#L76)[^ toc](#automations---table-of-contents)
