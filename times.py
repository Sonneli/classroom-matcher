class TimeSlot:
	"""
    A class representing a time slot on a specific day.

    Attributes:
        day (str): The day of the week (e.g., "Monday", "Tuesday").
        start (int): The start time in hours (e.g., 14 for 2 PM).
        end (int): The end time in hours (e.g., 16 for 4 PM).

    Methods:
        __init__(day, start, end):
            Initializes a new TimeSlot with the specified day, start, and end times.

        __str__():
            Returns a human-readable string representation of the TimeSlot.

        __repr__():
            Returns a string representation of the TimeSlot, useful for debugging.

        __eq__(other):
            Compares two TimeSlot objects for equality based on day, start, and end.
    """
	def __init__(self,day,start,end):
		"""
        Initialize a new TimeSlot instance.

        Args:
            day (str): The day of the week
            start (int): The start time 
            end (int): The end time 
        """
		self.day = day
		self.start = start
		self.end = end

	def __str__(self):
		"""
        Return a user-friendly string

        Returns:
            str: A string like "TimeSlot('Tuesday', 14, 16)".
        """
		return f"TimeSlot('{self.day}', {self.start}, {self.end})"

	def __repr__(self): 
		"""
        Return the official string of the TimeSlot

        Returns:
            str: A string like "TimeSlot('Tuesday', 14, 16)".
        """
		return f"TimeSlot('{self.day}', {self.start}, {self.end})"

	def __eq__(self,other):
		"""
        Check if two TimeSlot instances are the same.

        Args:
            other (TimeSlot): The other TimeSlot object to compare with.

        Returns:
            bool: True if both have the same day, start, and end; False otherwise.
        """
		return(self.day == other.day 
			and self.start == other.start
			and self.end == other.end)