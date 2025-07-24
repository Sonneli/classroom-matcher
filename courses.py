class Course:
	"""
    A class representing a course.

    Attributes:
        module (str): The module to which the course belongs 
        course_name (str): The name of the course 
        size (int): The number of participants 

    Methods:
        __init__(module, course_name, size):
            Initializes a new Course with the given module, course name, and size.

        __str__():
            Returns a user-friendly string of the Course.

        __repr__():
            Returns an official string of the Course for debugging.

        __eq__(other):
            Compares two Course instances 
    """
	def __init__(self,module,course_name,size):
		"""
        Initialize a new Course instance.

        Args:
            module (str): The module name.
            course_name (str): The name of the course.
            size (int): The number of students.
        """
		self.module = module 
		self.course_name = course_name
		self.size = size

	def __str__(self):
		"""
        Return a user-friendly string of the Course.

        Returns:
            str: A string like "Course('IPKult', 'Lecture', 30)".
        """
		return f"Course('{self.module}','{self.course_name}' ,{self.size})"

	def __repr__(self): 
		"""
        Return the programmer-friendly string of the Course.

        Returns:
            str: A string like "Course('IPKult', 'Lecture', 30)".
        """
		return f"Course('{self.module}','{self.course_name}' ,{self.size})"

	def __eq__(self,other):
		"""
        Check if two Course instances are equal.

        Args:
            other (Course): Another Course instance to compare with.

        Returns:
            bool: True if all attributes are equal; otherwise, False.
        """
		return(self.module == other.module 
			and self.course_name == other.course_name
			and self.size == other.size)

class Project(Course):
	"""
    A subclass of Course that represents a project-based course.

    Attributes:
        module (str): Inherited from Course.
        course_name (str): Inherited from Course.
        size (int): Inherited from Course.
        requirements (list): A list of software tools required for the project.

    Methods:
        __init__(module, course_name, size): Initializes a Project instance 

        require(software): Adds a software to the project.
    """
	def __init__(self,module,course_name,size):
		self.requirements = []
		super().__init__(module,course_name,size)

	def require(self,software):
		self.requirements.append(software)


