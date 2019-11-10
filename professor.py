class Professor:
    def __init__(self, name, bio, areas, projects, contact):
        self._name = name
        self._bio = bio
        self._areas = areas
        self._projects = projects
        self._contact = contact

    def getName(self):
        return self._name

    def getBio(self):
        return self._bio

    def getAreas(self):
        return self._areas

    def getProjects(self):
        return self._projects

    def getContact(self):
        return self._contact
