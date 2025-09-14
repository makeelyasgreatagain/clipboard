import pyperclip
import time
from datetime import datetime
import os

LOG_FILE = "clipboard.txt"

print("Clipboard saver running... Press Ctrl + C to stop.")

last_text = ""

while True:
    try:
        text = pyperclip.paste()
        if isinstance(text, str) and text.strip() and text != last_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{timestamp}: {text}\n")

            print(f"Saved: {timestamp}: {text[:40]}{'...' if len(text) > 40 else ' '}")
            last_text = text
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nExiting Keyboard Saver.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
