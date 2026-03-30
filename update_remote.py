import subprocess
import sys

cmd_widget = "sed -i \"s|http://64.118.142.181:8000||g\" /opt/livekit/client/widget.js && systemctl restart widget"
subprocess.run(["ssh", "root@64.118.142.181", cmd_widget])

cmd_dashboard = "sed -i \"s|http://64.118.142.181:8000|https://dashboard.thefarmtodoor.com|g\" /opt/livekit/dashboard/.env.local && cd /opt/livekit/dashboard && npm run build && systemctl restart dashboard"
subprocess.run(["ssh", "root@64.118.142.181", cmd_dashboard])
