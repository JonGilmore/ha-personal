#!/bin/sh

cookie=$(mktemp)
curl_cmd="curl --tlsv1 --silent --cookie ${cookie} --cookie-jar ${cookie} --insecure"

portfwd() {
  # authenticate against unifi controller
  ${curl_cmd} -d "{\"username\":\"$1\", \"password\":\"$2\"}" https://${3}:8443/api/login

  # enable/disable firewall rule
  ${curl_cmd} -k -X PUT https://${3}:8443/api/s/default/rest/portforward/${10} -H "Content-Type: application/json" -d @- <<-EOF
  {
    "name":"$4",
    "enabled":$5,
    "src":"any",
    "dst_port":"$6",
    "fwd":"$7",
    "fwd_port":"$8",
    "proto":"$9",
    "log":false,
    "_id":"$10",
    "site_id":"$11"
  }
EOF
}

powercycleport() {
  # authenticate against unifi controller
  ${curl_cmd} -d "{\"username\":\"$1\", \"password\":\"$2\"}" https://${3}:8443/api/login

  # cycle unifi port
  ${curl_cmd} -k -X POST https://${3}:8443/api/s/default/cmd/devmgr -H "Content-Type: application/json" -d @- <<-EOF
    {
        "mac":"$4",
        "port_idx":$5,
        "cmd":"$6"
    }
EOF
}

"$@"
