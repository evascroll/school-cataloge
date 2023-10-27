# school cataloge project
# example usage a
class School:
    def __init__(self, name, level, number_of_students):
        self.name = name
        self.level = level
        self._number_of_students = number_of_students

    @property
    def number_of_students(self):
        return self._number_of_students

    @number_of_students.setter
    def number_of_students(self, value):
        self._number_of_students = value
        """ or 
        if value >= 0:
            self._number_of_students = value
        else:
            print("Number of students cannot be negative")"""

    # repr to print relevant inff
    def __repr__(self):
        return f"A {self.level} School name {self.name} with {self.number_of_students} students!"

    # Example usage  b


class PrimarySchool(School):
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, "primary", number_of_students)
        self.pickup_policy = pickup_policy

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr} The pickup policy is {self.pickup_policy}"

    # example usage c


class HighSchool(School):
    def __init__(self, name, number_of_students, sports_team):
        super().__init__(name, "high", number_of_students)
        self.sports_team = sports_team

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr} The sport Team are {', '.join(self.sports_team)}"


# Example usages
a = School("codecademy", "high", 100)
print(a)
# print(a.name)
# print(a.level)
# a.numberOfStudents = 200
# print(a.numberOfStudents)
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
# print(b.pickupPolicy)
print(b)
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
# print(c.sportsTeam)
print(c)
