# , time, toggle, set_time
class AlarmClock:
    def __init__(self):
        self.current_time = ""
        self.alarm_toggle = ""
        self.alarm_set_time = ""

    def current(self):
        time = input("What is the current time in HH:MM:SS AM/PM format?\n")
        self.current_time = time
        print(f"The current time is {self.current_time}")

    def toggle(self):
        toggle = input("Would you like to turn an alarm on/off? Y/N\n")
        self.alarm_toggle = toggle

    def set_time(self):
        if self.alarm_toggle == "Y":
            set_time = input("What time do you want to set the alarm in HH:MM:SS AM/PM format?\n")
            self.alarm_set_time = set_time
            print(f"Alarm has been set for {self.alarm_set_time}")
    

