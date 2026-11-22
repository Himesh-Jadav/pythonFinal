from datetime import datetime

class TimeConverter:
    def to_24(self, time):
        return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")

    def to_12(self, time):
        return datetime.strptime(time, "%H:%M").strftime("%I:%M %p")
