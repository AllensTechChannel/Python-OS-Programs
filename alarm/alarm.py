import os
import time
from datetime import datetime
from playsound import playsound

# Ask for alarm time
alarm_time = input("Enter the time of alarm (HH:MM:SS AM/PM): ").strip()

try:
    alarm_dt = datetime.strptime(alarm_time, "%I:%M:%S %p")
    today = datetime.now().date()
    alarm_dt = datetime.combine(today, alarm_dt.time())
except ValueError:
    print("❌ Invalid format! Use HH:MM:SS AM/PM (example: 07:30:00 AM)")
    time.sleep(5)
    exit()

def countdown(t):
    """Simple countdown in seconds"""
    while t:
        mins, secs = divmod(t, 60)
        print(f"⏳ {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        t -= 1

print(f"✅ Alarm set for {alarm_dt.strftime('%I:%M:%S %p')}")

while True:
    now = datetime.now()
    if now >= alarm_dt:
        print("\n⏰ WAKE UP!")

        # Play short alarm once
        short_alarm = os.path.join("alarmsound", "wake_up_short.wav")
        if os.path.exists(short_alarm):
            playsound(short_alarm)
        else:
            print("❌ Short alarm file missing!")

        print("⚠️ Press Ctrl+C in the next 10 minutes or you will be faced with the LOUD REALY AND ANNOYING HORN SOUND EFFECT!")
        try:
            countdown(600)

            # Long alarm loops until user stops it
            long_alarm = os.path.join("alarmsound", "wake_up_long.wav")
            if os.path.exists(long_alarm):
                while True:
                    playsound(long_alarm)
            else:
                print("❌ Long alarm file missing!")
        except KeyboardInterrupt:
            print("\n😴 Alarm stopped by user.")
        break

    time.sleep(0.5)
