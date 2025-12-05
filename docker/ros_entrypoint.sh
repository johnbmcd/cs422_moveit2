#!/bin/bash
set -e

# setup ros2 environment
source "/root/ws_moveit/install/setup.sh" --
[ -f "/root/cs422_planning/install/setup.bash" ] && source "/root/cs422_planning/install/setup.bash"
exec "$@"
