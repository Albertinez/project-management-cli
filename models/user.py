from .person import Person

class User(Person):
    _id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)
        self.id = User._id_counter
        User._id_counter += 1
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"User {self.id}: {self.name}"