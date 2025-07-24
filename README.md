# classroom-matcher
This project simulates a university course scheduling system by implementing classes for courses (Course), time slots (TimeSlot), and rooms (Room), including their interactions and logic.Specifically:

Data Classes:

TimeSlot: Represents a weekly time period (e.g., Tuesday from 2–4 PM).

Course: Represents a course with a module name, course name, and expected number of students.

Room: Represents a classroom with a room number and capacity; also manages reservations.

Inheritance and Extensions:

Project: A subclass of Course that requires specific software (project-based course).

ComputerRoom: A subclass of Room with additional software support.

Scheduling Logic:

Check whether a room is suitable for a course (e.g., enough seats, software availability);

Determine room availability at a specific time;

Reserve the room and record the booking if available.

The final objective is to run the provided test module scheduling.py to validate the implementation.



