"""
Object-Oriented Programming (OOP) Module.
Illustrates class declarations, attributes, methods, inheritance, and magic/dunder methods.
"""


class Person:
    """Represents a general person with a name and age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_role(self) -> str:
        """Return the role of the person."""
        return "General Person"

    def __str__(self) -> str:
        """String representation of the person."""
        return f"{self.name} ({self.age} years old)"


class Student(Person):
    """Represents a student, inheriting from Person."""

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list[str] = []

    def enroll(self, course_name: str) -> None:
        """Enroll the student in a course."""
        if course_name not in self.courses:
            self.courses.append(course_name)

    def get_role(self) -> str:
        """Override get_role for a student."""
        return "Student"

    def __str__(self) -> str:
        """Override __str__ representation."""
        return f"Student {self.name} [ID: {self.student_id}]"


def introduce_person(person: Person) -> str:
    """Demonstrates polymorphism by calling get_role() and str() on any Person subclass."""
    return f"Role: {person.get_role()} | Info: {str(person)}"
