#!/usr/bin/env bash
# Start virtual display, window manager, VNC, and NoVNC Proxy in the background
Xvfb :1 -screen 0 1280x720x24 >/dev/null 2>&1 &
export DISPLAY=:1
fluxbox >/dev/null 2>&1 &
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 -bg >/dev/null 2>&1 &
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/dev/null 2>&1 &
echo "VNC display server running on port 6080"