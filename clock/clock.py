import time
import os
import sys
import winsound

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ask for time input
time_input = input("Enter amount of seconds for timer (60 sec = 1 min): ").strip()
try:
    t = int(time_input)
    if t <= 0:
        raise ValueError
except ValueError:
    print("Please enter a positive whole number of seconds.")
    sys.exit(1)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r", flush=True)
        time.sleep(1)
        seconds -= 1

# Run countdown
countdown(t)

clear_screen()
print(f"{t} seconds is up!")

# Path to alarm sound
long_alarm = os.path.join("clocksound", "alarm.wav")

if not os.path.exists(long_alarm):
    print(f"Alarm sound not found: {long_alarm}")
    sys.exit(1)

# Play alarm continuously, stop with Ctrl+C
try:
    # Start playing in the background and loop until stopped
    winsound.PlaySound(long_alarm, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    print("Press Ctrl + C to stop the alarm...")
    while True:
        time.sleep(0.2)  # keep the process alive and responsive to Ctrl+C
except KeyboardInterrupt:
    # Stop any async sound that is currently playing
    winsound.PlaySound(None, winsound.SND_PURGE)
    print("\n Alarm stopped by user.")
    time.sleep(1)
