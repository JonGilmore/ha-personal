#!/bin/sh

cookie=$(mktemp)
headers=$(mktemp)
curl_cmd="curl --silent --output /dev/null --cookie ${cookie} --cookie-jar ${cookie} --insecure"

portfwd() {
  # authenticate against unifi controller
  ${curl_cmd} -H 'Content-Type: application/json' -D ${headers} -d "{\"username\":\"$1\", \"password\":\"$2\"}" https://${3}/api/auth/login

  # grab the `x-csrf-token` and strip the newline (added when upgraded to controller 6.1.26)
  csrf="$(awk -v FS=': ' '/^x-csrf-token/{print $2}' "${headers}" | tr -d '\r')"

  # enable/disable firewall rule
  ${curl_cmd} -k -X PUT https://${3}/proxy/network/api/s/default/rest/portforward/${10} -H "Content-Type: application/json" -H "x-csrf-token: ${csrf}" -d @- <<-EOF
  {
    "name":"${4}",
    "enabled":${5},
    "src":"${12}",
    "dst_port":"${6}",
    "fwd":"${7}",
    "fwd_port":"${8}",
    "proto":"${9}",
    "log":false,
    "_id":"${10}",
    "site_id":"${11}",
    "pfwd_interface":"wan",
    "destination_ip":"any"
  }
EOF
}

powercycleport() {
  # authenticate against unifi controller
  ${curl_cmd} -d "{\"username\":\"$1\", \"password\":\"$2\"}" https://${3}/api/login

  # cycle unifi port
  ${curl_cmd} -k -X POST https://${3}/api/s/default/cmd/devmgr -H "Content-Type: application/json" -d @- <<-EOF
    {
        "mac":"$4",
        "port_idx":$5,
        "cmd":"$6"
    }
EOF
}

powercycledevice() {
  # authenticate against unifi controller
  ${curl_cmd} -H 'Content-Type: application/json' -D ${headers} -d "{\"username\":\"$1\", \"password\":\"$2\"}" https://${3}/api/auth/login

  # grab the `x-csrf-token` and strip the newline (added when upgraded to controller 6.1.26)
  csrf="$(awk -v FS=': ' '/^x-csrf-token/{print $2}' "${headers}" | tr -d '\r')"

  # cycle unifi device
  ${curl_cmd} -k -X POST https://${3}/proxy/network/api/s/default/cmd/devmgr -H "Content-Type: application/json" -H "x-csrf-token: ${csrf}" -d @- <<-EOF
    {
        "mac":"$4",
        "reboot_type":"$5",
        "cmd":"$6"
    }
EOF
}

"$@"
