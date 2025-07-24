from courses import Project

class Room:
	"""
    A class representing a room that can be reserved for courses.

    Attributes:
        name (str): The name of the room.
        capacity (int): The maximum number of people the room can accept.
        reservations (list): A list of tuples (TimeSlot, Course) and show the reservations

    Methods:
        __init__(name, capacity):
            Initializes a new Room with the given name and capacity.

        __str__():
            Returns a user-friendly string of the Room.

        __repr__():
            Returns the programmer-friendly string of the Room for debugging.

        __eq__(other):
            Compares two Room instances and want to know if they are the same

        suitable_for(course):
            Returns True if the room is suitable for the given course (not a Project).

        available_at(slot):
            Checks whether the room is available at the given TimeSlot.

        reserve(slot, course):
            Reserves the room for the given TimeSlot and Course if available.
    """
	def __init__(self, name, capacity):
		"""
        Initialize a new Room.

        Args:
            name (str): The name of the room.
            capacity (int): The room's capacity.
        """
		self.name = name
		self.capacity = capacity
		self.reservations = []

	def __str__(self):
		"""
        Return a user-friendly string of the Room.

        Returns:
            str: Example: "Room('A202', 187)".
        """
		return f"Room('{self.name}',{self.capacity})"

	def __repr__(self): 
		"""
        Return the programmer-friendly string of the Room.

        Returns:
            str: Example: "Room('B222', 150)".
        """
		return f"Room('{self.name}',{self.capacity})"

	def __eq__(self,other):
		"""
        Compare two Rooms for equality.

        Args:
            other (Room): Another Room instance.

        Returns:
            bool: True if name, capacity, and reservations are equal.
        """
		return(self.name == other.name
			and self.capacity == other.capacity
			and self.reservations == other.reservations)

	def suitable_for(self,course):
		"""
        Check if the room is suitable for the given course.

        Args:
            course (Course): the given course

        Returns:
            bool: False if course is a Project. Otherwise, True if course size fits capacity.
        """
		if isinstance(course,Project):
			return False
		else:
			if course.size <= self.capacity:
				return True
			else:
				return False

	def available_at(self,slot):
		"""
        Check if the room is available at a specific time.

        Args:
            slot (TimeSlot): The time to check.

        Returns:
            bool: True if no reservation exists at that slot; False otherwise.
        """
		for reserved_slot, _ in self.reservations:
	    # "reserved_slot, _" means that only the first element of the tuple will be considered
			if reserved_slot == slot:
				return False
		return True

	def reserve(self,slot,course):
		"""
        Attempt to reserve the room for a given TimeSlot and Course.

        Args:
            slot (TimeSlot): time
            course (Course): The course that will reserve the room

        Returns:
            bool: True if reservation was successful; False if time is already booked.
        """
		if self.available_at(slot):
			self.reservations.append((slot,course))
			return True
		else:
			return False

class ComputerRoom(Room):
	"""
    A subclass of Room representing a computer room with software installations.

    Attributes:
        name (str): Inherited from Room.
        capacity (int): Inherited from Room.
        reservations (list): Inherited from Room.
        software (list): A list of installed software.

    Methods:
        install(software):
            Installs software in the computer room.

        provides(software):
            Checks whether the room provides a specific software.

        provides_all(software_list):
            Checks whether all software in the list are installed.

        suitable_for(course):
            Checks if the room is suitable for the given course, including software and sits
    """
	def __init__(self,name,capacity):
		"""
        Initialize a new ComputerRoom instance.

        Args:
            name (str): The name of the computer room.
            capacity (int): The capacity of the room.
        """
		super().__init__(name,capacity)
		self.software = []


	def install(self,software):
		"""
        Install a piece of software into the computer room.

        Args:
            software (str): The name of the software 
        """
		if software not in self.software:
			self.software.append(software)

	def provides(self,software):
		"""
        Check if the room provides a required software.

        Args:
            software (str): The name of the software.

        Returns:
            bool: True if the software is installed.
        """
		if software in self.software:
			return True
		else:
			return False

	def provides_all(self,software_list):
		"""
        Check if all software in the list are installed.

        Args:
            software_list (list of str): List of required software.

        Returns:
            bool: True if all are installed; False otherwise.
        """
		for i in range(len(software_list)):
			if not self.provides(software_list [i]):
				return False
		return True

	def suitable_for(self,course):
		"""
        Determine if the computer room is suitable for a given course.

        For Project courses, the room must have all required software besides capacity.
        For other courses, only the capacity will be considered.

        Args:
            course (Course): The given course that will use a room.

        Returns:
            bool: True if suitable; False otherwise.
        """
		if isinstance(course,Project):
			if not self.provides_all(course.requirements):
				return False
			else:
				return course.size <= self.capacity
		else:
			return course.size <= self.capacity




