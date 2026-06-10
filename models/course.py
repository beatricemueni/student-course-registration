class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):

        if not course_id:
            raise ValueError("Course ID cannot be empty")

        if not course_name:
            raise ValueError("Course name cannot be empty")

        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a number greater than 0")

        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "trainer_name": self.trainer_name,
            "capacity": self.capacity,
        }

    def __str__(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Trainer: {self.trainer_name}\n"
            f"Capacity: {self.capacity}\n"
        )