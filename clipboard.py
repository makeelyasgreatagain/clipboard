import pyperclip
import time

print("Clipboard saver running... Press Ctrl + C to stop.")

last_text = ""

while True:
    try:
        text = pyperclip.paste()
        log_time = str(round(time.time()))
        if text != last_text and text.strip() != "":
            with open("clipboard.txt", "a", encoding="utf-8") as f:
                f.write(log_time + ": " + text + "\n")
            print(f"Saved: {log_time}: {text[:40]}...")
            last_text = text
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting Keyboard Saver.")
        break
