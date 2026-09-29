from enum import Enum
class Ticket:

    def __init__(self, id, title, description, assigned_to, priority):
        self.id = id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = Status.OPEN
        self.priority = priority

    def __str__(self):
        return f"""
        id: {self.id:03d}
        title: {self.title}
        description: {self.description}
        assigned_to: {self.assigned_to}
        status: {self.status.value}
        priority: {self.priority}   
        """



    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title
    @property
    def description(self):
        return self._description
    @property
    def assigned_to(self):
        return self._assigned_to
    @property
    def status(self):
        return self._status
    @property
    def priority(self):
        return self._priority


    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError("Ticket ID must be greater than 0")
        self._id = value
    @title.setter
    def title(self, value):
        self._title = value
    @description.setter
    def description(self, value):
        self._description = value
    @assigned_to.setter
    def assigned_to(self, value):
        self._assigned_to = value
    @status.setter
    def status(self, value):
        self._status = value
    @priority.setter
    def priority(self, value):
        self._priority = value

class Status(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"