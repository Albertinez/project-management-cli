class Task:
    _id_counter = 1

    def __init__(self, title, assigned_to):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def complete(self):
        self.status = "Completed"

    def __repr__(self):
        return f"Task {self.id}: {self.title} [{self.status}]"