from i3pystatus import Status

status = Status(standalone=True)

# Global setup
globInterval = 5

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
status.register("clock",
    interval=globInterval,
    format="%a %-d %b %H:%M",)

# This would look like this:
# Discharging 6h:51m
status.register("battery",
    interval=globInterval,
    format="{status} {percentage:02.0f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    status={
        "DIS":  "DIS",
        "CHR":  "CHR",
        "FULL": "FULL",
    },)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    interval=globInterval,
    path="/",
    format="{used}/{total}G",)

# Show uptime
status.register("uptime",
    interval=globInterval,
    format="UP {hours}h:{mins}m",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}%",)

# Show backlight percentage
status.register("backlight",
    interval=globInterval,
    format="☀{percentage}%",
    base_path="/sys/class/backlight/intel_backlight/",)

# Note: the network module requires PyPI package netifaces
status.register("network",
    interval=globInterval,
    interface="enp0s25",
    format_up="{v4cidr}",)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interval=globInterval,
    interface="wlp4s0",
    format_up="{essid} {quality:02.0f}%",)

# Show active VPN connections
for vpn in ["KIT", "Datenfestung"]:
    status.register("openvpn",
        interval=globInterval,
        vpn_name=vpn,
        status_command="bash -c 'nmcli connection show --active | grep %(vpn_name)s'",)

status.run()
