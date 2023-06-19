import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play sound
            frequency = 3000 # Set frequency (range: 37 to 32767 Hz)
            duration = 14000  # Set duration in milliseconds
            winsound.Beep(frequency, duration)
            break
        time.sleep(1)

# Get the alarm time from the user
alarm_input = input("Enter the alarm time in HH:MM format: ")
alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M").strftime("%H:%M:%S")

# Set the alarm
set_alarm(alarm_time)
