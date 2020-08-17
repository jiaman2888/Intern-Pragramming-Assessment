import sys
import math

class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "[%d %d]" % (self.x, self.y)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False

class Person(object):
    def __init__(self, name, bday, location):
        self.name = name
        self.bday = bday
        self.location = location

    def toString(self):
        return "%s %s %s" % (self.name, self.bday, self.location.toString())

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Person):
            return self.name == other.name and self.bday == other.bday and self.location == other.location
        return False

def findNearestPerson(target, people):
    ans = None
    dis = sys.maxint
    for p in people:
        if target == p:
            continue
        d = (p.location.x - target.location.x) ** 2 + (p.location.y - target.location.y) ** 2
        if dis > d:
            ans = p
            dis = d
    return ans

if __name__ == '__main__':
    people = [
        Person("Alice", "1990-01-01", Location(0, 0)),
        Person("Bob", "1991-01-01", Location(4, 5)),
        Person("Celina", "1992-01-01", Location(3, 7)),
        Person("David", "1994-01-01", Location(-3, -17)),
        Person("Ethan", "1994-01-01", Location(-3, 25)),
    ]
    print(findNearestPerson(Person("Alice", "1990-01-01", Location(0, 0)), people).toString())
    print(findNearestPerson(Person("Frank", "1990-01-01", Location(10, 10)), people).toString())