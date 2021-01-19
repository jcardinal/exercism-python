class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        while self.minute >= 60:
            self.hour += 1
            self.minute -= 60
        while self.minute < 0:
            self.hour -= 1
            self.minute += 60
        if self.hour >= 24:
            self.hour %= 24
        while self.hour < 0:
            self.hour += 24

    def __repr__(self):
        return f"{self.hour:02}" + ":" + f"{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
