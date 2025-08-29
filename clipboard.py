import pyperclip
import time

print("Clipboard saver running... Press Ctrl + C to stop.")

last_text = ""

while True:
    try:
        text = pyperclip.paste()
        if text != last_text and text.strip() != "":
            with open("clipboard.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")
            print(f"Saved: {text[:40]}...")
            last_text = text
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting Keyboard Saver.")
        break
