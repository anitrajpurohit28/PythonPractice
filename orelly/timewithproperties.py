# timewithproperties.py

"""Class Time with read-write properties."""


class Time:
    """Class time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute"""
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        """Return the hour"""
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour <= 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._hour = hour

    @property
    def minute(self):
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute"""
        if not (0 <= minute <= 59):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        self._minute = minute

    @property
    def second(self):
        """Return second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second <= 59):
            raise ValueError(f'Second ({second}) must be 0-59')
        self._second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second})')

    def __str__(self):
        """Return the string in 12 hours format"""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of Hours, minute, and seconds"""
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def time(self):
        return (self.hour, self.minute, self.second)

    @time.setter
    def time(self, time_tuple):
        """Set time from a tuple containing hour, minute and second."""
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])







