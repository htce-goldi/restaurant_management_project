import os
from datetime import datetime

log_file = os.path.join("src", "log", "system_logs.txt")

def log_event(event_type, message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{event_type.upper()}] {message}\n"

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    try:
        with open(log_file, "a") as f:
            f.write(entry)
    except IOError as e:
        print(f"Logging failed: {e}")
