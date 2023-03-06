class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.set_time(hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        if hours <= Time.max_hours and minutes <= Time.max_minutes and seconds <= Time.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        else:
            raise ValueError("Invalid time value")

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        elif self.minutes < Time.max_minutes:
            self.seconds = 0
            self.minutes += 1
        elif self.hours < Time.max_hours:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
        else:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        return self.get_time()




time = Time(9, 30, 59)
print(time.next_second())