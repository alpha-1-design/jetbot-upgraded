#!/usr/bin/env python3
"""
Simple modern web dashboard for JetBot.

Indie-friendly features:
- Drive from phone or laptop browser
- Live camera stream
- Big friendly buttons + virtual joystick
- Works on the local network (no cloud)

Run:
    python3 demos/web_dashboard.py

Then open http://<jetson-ip>:8080 on any device on the same Wi-Fi.
"""

import io
import time
import threading
from flask import Flask, Response, render_template_string, request, jsonify
import cv2

import sys
sys.path.insert(0, "..")
from jetbot.modern_robot import Robot

app = Flask(__name__)
robot = Robot()
camera = None
camera_lock = threading.Lock()

# Simple HTML dashboard (single file, no build step)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
  <title>JetBot Dashboard</title>
  <style>
    body { font-family: system-ui, sans-serif; background: #111; color: #eee; margin: 0; padding: 12px; text-align: center; }
    h1 { font-size: 1.4rem; margin: 8px 0; }
    #stream { width: 100%; max-width: 640px; border-radius: 12px; background: #222; }
    .controls { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 16px; }
    button { 
      font-size: 1.1rem; padding: 14px 20px; border: none; border-radius: 12px; 
      background: #2a6; color: white; min-width: 90px; cursor: pointer;
    }
    button:active { background: #184; }
    button.stop { background: #c33; }
    button.stop:active { background: #a22; }
    .row { display: flex; gap: 10px; justify-content: center; width: 100%; }
    #status { margin-top: 12px; font-size: 0.9rem; color: #aaa; }
  </style>
</head>
<body>
  <h1>JetBot Upgraded</h1>
  <img id="stream" src="/video_feed" alt="Camera">
  <div class="controls">
    <div class="row">
      <button ontouchstart="send('forward')" onmousedown="send('forward')" 
              ontouchend="send('stop')" onmouseup="send('stop')">↑ Forward</button>
    </div>
    <div class="row">
      <button ontouchstart="send('left')" onmousedown="send('left')"
              ontouchend="send('stop')" onmouseup="send('stop')">← Left</button>
      <button class="stop" onclick="send('stop')">STOP</button>
      <button ontouchstart="send('right')" onmousedown="send('right')"
              ontouchend="send('stop')" onmouseup="send('stop')">Right →</button>
    </div>
    <div class="row">
      <button ontouchstart="send('backward')" onmousedown="send('backward')"
              ontouchend="send('stop')" onmouseup="send('stop')">↓ Back</button>
    </div>
  </div>
  <div id="status">Ready</div>

  <script>
    function send(cmd) {
      fetch('/cmd/' + cmd, {method: 'POST'});
      document.getElementById('status').innerText = 'Last: ' + cmd;
    }
    // Prevent scrolling on mobile while pressing buttons
    document.querySelectorAll('button').forEach(b => {
      b.addEventListener('touchstart', e => e.preventDefault(), {passive: false});
    });
  </script>
</body>
</html>
"""


def get_camera():
    global camera
    with camera_lock:
        if camera is None:
            camera = cv2.VideoCapture(0)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        return camera


def generate_frames():
    while True:
        cam = get_camera()
        success, frame = cam.read()
        if not success:
            time.sleep(0.1)
            continue
        # Optional: draw a simple crosshair
        h, w = frame.shape[:2]
        cv2.drawMarker(frame, (w//2, h//2), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20)
        ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)


@app.route('/')
def index():
    return render_template_string(DASHBOARD_HTML)


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/cmd/<command>', methods=['POST'])
def command(command):
    speed = 0.3
    if command == 'forward':
        robot.forward(speed)
    elif command == 'backward':
        robot.backward(speed)
    elif command == 'left':
        robot.left(speed)
    elif command == 'right':
        robot.right(speed)
    elif command == 'stop':
        robot.stop()
    return jsonify({"ok": True, "cmd": command})


if __name__ == '__main__':
    print("Starting JetBot Web Dashboard...")
    print("Open http://<this-device-ip>:8080 on your phone or laptop")
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False)
