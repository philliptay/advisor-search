class Professor:
    def __init__(self, name, dept, areas, years, numAdvisees, projects, contact):
        self._name = name
        self._dept = dept
        self._areas = areas
        self._years = years
        self._advisees = advisees
        self._projects = projects
        self._contact = contact

    def getName(self):
        return self._name

    def getDept(self):
        return self._dept

    def getAreas(self):
        return self._areas

    def getYears(self):
        return self._years

    def getAdvisees(self):
        return self._advisees

    def getProjects(self):
        return self._projects

    def getContact(self):
        return self._contact