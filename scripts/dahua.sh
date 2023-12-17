#!/bin/bash
#
# Description: Switch to day(0) or night(1) profiles on Dahua Cameras
# Argument(s): 0="day" or 1="night"
# Credit: https://community.home-assistant.io/t/dahua-cameras-switch-between-day-and-night-video-profiles/264458
# cameras.dat format: IP|PORT|CAM_TYPE|USERNAME|PASSWORD|CAM_NAME|NORMAL_OR_LOWLIGHT

# DAY or NIGHT
arg=$(echo ${1:-null} | tr [:lower:] [:upper:])

# NORMAL or LOWLIGHT
arg2=$(echo ${2:-null} | tr [:lower:] [:upper:])

if [ ${arg} = "DAY" ]; then
  MODE=0
fi

if [ ${arg} = "NIGHT" ]; then
  MODE=1
fi

grep ${arg2} /config/scripts/cameras.dat | awk -F\| '{printf "%s %s %s %s %s \"%s\"\n", $1, $2, $4, $5, $6, $7}' | while
  read IP PORT USERNAME PASSWORD DESCRIPTION ENABLED
do
  /usr/bin/curl -v -g --digest -u ${USERNAME}:${PASSWORD} "http://${IP}:${PORT}/cgi-bin/configManager.cgi?action=setConfig&VideoInMode[0].Config[0]=${MODE}"
done
