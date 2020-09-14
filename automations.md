# Automations - Table of Contents
1.  [Security](#security) (70 automations)
1.  [Garage](#garage) (3 automations)
1.  [Nabu Casa](#nabu-casa) (2 automations)
1.  [Person Detection](#person-detection) (5 automations)
1.  [Port Forward](#port-forward) (4 automations)
1.  [HVAC](#hvac) (8 automations)
1.  [Vacation Mode](#vacation-mode) (5 automations)
1.  [Vacuum](#vacuum) (1 automations)
1.  [Christmas](#christmas) (6 automations)

⚠️ Total number of automations: **104** ⚠️

## [Security](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml)
### [Line crossing template - telegram & tv notify](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L3)
  When something crosses a line on the driveway or porch, notify via telegram and LG TV

*which uses:*
-   [sensor.db_pic](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L125)
-   [sensor.hik_driveway_pic](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L127)

### [Front door line crossing or doorbell rang - occupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L28)
  When its dark out & house occupied - foyer and exterior lights on

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L173)

### [Front door line crossing or doorbell rang - unoccupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L54)
  When its dark out & house unoccupied - foyer and exterior lights on for 10 min

*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L2)

### [Turn off foyer and exterior lights 10 minutes after trigger](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L77)
*which uses:*
-   [timer.front_door_motion_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L2)

### [Doorbell rang - play google home video](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L89)
  Play the front door video stream on the Google Home for 30 seconds

### [Doorbell rang - interrupt sonos master](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L105)
*which uses:*
-   [script.sonos_say](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L190)

### [Deck person & dark out - turn deck lights on](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L121)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L187)

### [Deck lights off when no person detected for 10min](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L136)
### [Deck motion light - timer start](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L147)
*which uses:*
-   [timer.deck_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L9)

### [Deck lights on when deck door opens (and the timer is running)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L155)
  Trigger shows direction of travel

*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)
-   [timer.deck_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L9)

### [Garage person/motion detected & dark out - garage lights on](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L172)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L187)

### [Garage lights off when no person detected for 15min](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L187)
### [Wake up (only between Oct-May) & turn on some lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L202)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)

### [Motion light template for foyer & basement & and bar](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L222)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L2)

### [Master blinds at dusk & only runs once (and after 1hr before sunset)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L258)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)

### [Close master blinds at sunset](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L276)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)

### [Open master blinds in the morning (after 45min of unoccupied bed)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L286)
*which uses:*
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)
-   [input_boolean.master_blinds_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L6)
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L298)

### [Reset run-once variables - noon](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L306)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L8)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L8)

### [Start sleeping & set HVAC fans on & turn off recirculation pump & all lights off if no guests (only exterior & lower & & main if guests) & and main tv off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L314)
*which uses:*
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L12)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [input_boolean.guests](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L12)

### [Start sleeping & check the garage doors](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L342)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)

### [Check the door locks](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L362)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [script.lock_doors](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L115)
-   [sensor.doors_unlocked](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L95)
-   [sensor.doors_unlocked_number](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L107)

### [Done sleeping & HVAC fan off & recirculation pump on](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L383)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)

### [Turn the HVAC fans on & recirculation pump and tvs off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L399)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [script.tvs_off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L133)

### [Away during the day & turn lights off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L416)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)

### [Return home & turn the HVAC fans off & the recirculation pump on & stop daisy cam timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L429)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L4)

### [Turn on sunset lights at dark or sunset](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L447)
*which uses:*
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L8)
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)
-   [input_boolean.sunset_run_once](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L8)

### [Turn on master fan at night (if AC is on)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L469)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Turn off master fan in the morning](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L486)
### [Check the front door lock when leaving](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L494)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L15)

### [Winter indoor humidity check & see if its below the high threshold](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L514)
*which uses:*
-   [sensor.target_humidity_max_winter](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L205)

### [Winter indoor humidity check & see if its above the low threshold](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L527)
*which uses:*
-   [sensor.target_humidity_min_winter](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L214)

### [If there is a water leak & notify & close the water valve & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L540)
*which uses:*
-   [binary_sensor.moisture_sensors](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L67)

### [Dog walker here between 9:30-2pm (while the alarm is not disarmed)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L556)
*which uses:*
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L15)
-   [sensor.armed_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L15)

### [Fire active & unlock locks & send videos & lights set to 25% & hvac off & repeat notifications](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L570)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L16)
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L23)

### [Burglar active & lights on & send videos & repeat notifications](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L587)
*which uses:*
-   [script.alarm](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L82)
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L23)

### [Turn off alarm notifications because of user interaction](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L597)
*which uses:*
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L16)
-   [input_boolean.alarm_notifier](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L16)

### [Master entry motion light when master bed is unoccupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L612)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L298)

### [Master entry motion lights Off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L630)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L18)

### [Sitting motion light when master bed is unoccupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L652)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L298)

### [Sitting motion light off when master override is off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L668)
*which uses:*
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L18)
-   [input_boolean.master_override](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L18)

### [Sitting light off when bed occupied (& chair unoccupied)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L683)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L298)
-   [sensor.master_sitting_chair_occupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L287)

### [Sitting light off when chair unoccupied (& bed occupied)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L701)
*which uses:*
-   [sensor.master_bed_people](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L298)
-   [sensor.master_sitting_chair_occupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L287)

### [Kitchen lights off with no motion for 15 minutes](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L720)
*which uses:*
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L2)
-   [input_boolean.block_all_motion_lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L2)

### [Daisy cam photo every 45 minutes when armed away and kennel closed](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L735)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L4)

### [Daisy timer completed](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L750)
*which uses:*
-   [binary_sensor.alarm_occupancy_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L84)
-   [script.video_daisy](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L15)
-   [timer.daisy_cam_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L4)

### [Enable motion lights 2hours before sunset & disable 2hour after sunrise](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L768)
### [Disable motion lights 2hours sunrise](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L776)
### [Kitchen motion light](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L785)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)

### [Basement lights off with no motion](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L801)
*which uses:*
-   [binary_sensor.basement_motions](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L36)

### [Patio fan off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L813)
### [Backyard party lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L832)
*which uses:*
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L14)
-   [input_boolean.party](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_booleans.yaml#L14)

### [Elk Alarm trouble notification](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L847)
*which uses:*
-   [sensor.alarm_trouble](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L27)

### [Doorbell notification event capture and notify](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L859)
### [Victorops notification - turn on light](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L868)
*which uses:*
-   [sensor.period_of_day](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L187)

### [General notifications](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L885)
*which uses:*
-   [sensor.alarm_state](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L23)

### [UPS notifications](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L931)
### [Important date (birthday & anniversary)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L940)
### [Create all groups](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L953)
*which uses:*
-   [script.group_set](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L145)

### [Popup camera](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L964)
*which uses:*
-   [script.popup_camera](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L173)

### [Basement stairs motion - timer start](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L979)
*which uses:*
-   [timer.basement_stairs_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L7)

### [Basement lights on after stairs motion](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L987)
*which uses:*
-   [timer.basement_stairs_timer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/timers.yaml#L7)

### [Storage & master toekick motion lights](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1000)
### [Office desk & gym lights motion on](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1031)
*which uses:*
-   [binary_sensor.light_inside](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L101)

### [Office desk & gym lights motion off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1053)
### [Office speakers on/off with presence](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1076)
### [Wfh turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1092)
### [Wfh turn on recirculation pump (only when somebody is home)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1104)
*which uses:*
-   [binary_sensor.anybody_home](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L109)

### [Acknowledge garage single open](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1116)
*which uses:*
-   [alert.garage_door_single](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/alerts.yaml#L2)

### [Acknowledge garage double open](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1127)
*which uses:*
-   [alert.garage_door_double](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/alerts.yaml#L20)

### [Toilet off when bathroom off](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/automation.yaml#L1138)[^ toc](#automations---table-of-contents)

## [Garage](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/garage.yaml)
### [Single is open - close](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/garage.yaml#L3)
### [Double is open - close](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/garage.yaml#L18)
### [Either door is open for 10min & notify & kill heat if it is on](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/garage.yaml#L33)
*which uses:*
-   [sensor.garage_temperature](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/sensors.yaml#L45)
[^ toc](#automations---table-of-contents)

## [Nabu Casa](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/nabu_casa.yaml)
### [Sleep starting & all home & nabu casa disconnect](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/nabu_casa.yaml#L7)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L123)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)

### [Anybody leaves OR vacation on OR sleep off & nabu casa connect](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/nabu_casa.yaml#L19)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L123)
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)
[^ toc](#automations---table-of-contents)

## [Person Detection](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml)
### [Doorbell person detected](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml#L3)
  If nobody is home or were sleeping - send a video of the doorbell

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [shell_command.cam_vid_doorbell](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L10)

### [Driveway person detected](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml#L34)
  If nobody is home or were sleeping - send a video of the driveway

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [shell_command.cam_vid_driveway](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L11)

### [Deck person detected](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml#L65)
  If nobody is home or were sleeping - send a video of the deck

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [shell_command.cam_vid_deck](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L12)

### [Deckstairs person detected](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml#L96)
  If nobody is home or were sleeping - send a video of the deckstairs

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [shell_command.cam_vid_deckstairs](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L13)

### [Garage person detected](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/person.yaml#L127)
  If nobody is home or were sleeping - send a video of the garage

*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [shell_command.cam_vid_garage](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L14)
[^ toc](#automations---table-of-contents)

## [Port Forward](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/port_forward.yaml)
### [Enable wireguard port forward if anybody leaves](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/port_forward.yaml#L3)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L123)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L9)

### [Disable wireguard port forward when we get home](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/port_forward.yaml#L22)
*which uses:*
-   [binary_sensor.anybody_away](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L123)
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L9)

### [Enable NAS port forward for nightly backup at 1:58am](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/port_forward.yaml#L42)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L9)

### [Disable NAS port forward for backup](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/port_forward.yaml#L60)
*which uses:*
-   [shell_command.unifi_portfwd](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/shell_commands.yaml#L9)
[^ toc](#automations---table-of-contents)

## [HVAC](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml)
### [Set cooling temps in the morning (if were not on vacation and somebody is home](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L2)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Set heating temps in the morning (if we're not on vacation and somebody is home)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L24)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Set back cooling temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L48)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Set back heating temps at 8am only if were not on vacation and nobody is home](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L70)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Home from work (4pm) & set cooling temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L94)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Home from work (4pm) & set heating temps to normal (only when were not on vacation)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L108)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [When we start sleeping set the thermostats back (for cooling)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L124)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [When we start sleeping set the thermostats back (for heating)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/thermostats.yaml#L139)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)
[^ toc](#automations---table-of-contents)

## [Vacation Mode](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml)
### [While on vacation & turn off all lights at 23:30](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml#L3)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Summer (main tstat isn't heating) & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml#L15)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Return from vacation (summer) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml#L43)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Winter time & close the main water valve & set temperatures back & set water heater to vacation & & turn off recirculation pump](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml#L69)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)

### [Return from vacation (winter) & open the main water valve & remove the rheem water heater vacation hold & set temps back](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacation.yaml#L106)
*which uses:*
-   [binary_sensor.vacation_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L80)
[^ toc](#automations---table-of-contents)

## [Vacuum](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacuum.yaml)
### [Start cleaning kitchen](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/vacuum.yaml#L3)
*which uses:*
-   [input_select.vacuum_room](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/input_selects.yaml#L2)
-   [script.vacuum_foyer](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L220)
-   [script.vacuum_kitchen](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/scripts.yaml#L211)
[^ toc](#automations---table-of-contents)

## [Christmas](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml)
### [Roof lights on (only in december)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L3)
### [Trees on (only in december) if occupied](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L14)
### [Turn off at 11pm (only in december)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L28)
### [Turn off when sleeping starts (only in december)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L39)
*which uses:*
-   [binary_sensor.sleep_status](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/includes/binary_sensors.yaml#L96)

### [Lights off/on with geolocation presence (only in Dec)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L52)
### [Turn off when laura gets in bed (only in december)](https://github.com/jongilmore/ha-personal/blob/c38cd881e9052cd3bfa0a757e9e7180a74f31d92/automation/xmas.yaml#L76)[^ toc](#automations---table-of-contents)
