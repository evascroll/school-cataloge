# school cataloge project
# example usage a
class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents  # private variable

        # getter

    def name(self):
        return self.name

        # getter

    def level(self):
        return self.level

        # getter

    def numberOfStudents(self):
        return self.numberOfStudents

        # setter

    def numberOfStudents(self, value):
        self.numberOfStudents = value

        """ other option
        if value >= 0:self.numberOfStudents = value
        else:
            print("number of student cannot be negative")"""

    # repr to print relevant inff
    def __repr__(self):
        return f"A {self.level} School name {self.name} with {self.numberOfStudents} students!"

    # Example usage b


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

        # getter

    def pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr} The pickup policy is {self.pickupPolicy}"

    # example usage c


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeam):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeam = sportsTeam

    # getter
    def sportsTeam(self):
        return self.sportsTeam

    def __repr__(self):
        parent_name = super().__repr__()
        return f"{parent_name} The sport Team are {', '.join(self.sportsTeam)}"


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
