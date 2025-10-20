import os
import subprocess
import signal
import time
import sys

# ---------- CONFIG ----------
MYSQL_SERVICE_NAME = "MySQL80"  # change if your service name is different
FLASK_APP_PATH = r"D:\CDAC\Python\labour-management-system\app.py"  # replace with path to your Flask app
FLASK_PORT = 5000

# ---------- START MYSQL ----------
print("Starting MySQL service...")
os.system(f'net start {MYSQL_SERVICE_NAME}')
time.sleep(2)  # small delay to ensure MySQL starts

# ---------- RUN FLASK APP ----------
print(f"Starting Flask app on port {FLASK_PORT}...")
flask_process = subprocess.Popen([sys.executable, FLASK_APP_PATH], shell=True)

try:
    # Wait for Flask process to exit
    flask_process.wait()
except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Stopping Flask...")

# ---------- STOP FLASK ----------
print("Stopping Flask app...")
flask_process.send_signal(signal.SIGINT)
time.sleep(1)

# ---------- STOP MYSQL ----------
print("Stopping MySQL service...")
os.system(f'net stop {MYSQL_SERVICE_NAME}')

print("All done. MySQL stopped, Flask terminated.")

