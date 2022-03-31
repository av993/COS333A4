class Class:

    def __init__(self, classes, depts, courses, profs):
        self._classes = classes
        self._depts = depts
        self._courses = courses
        self._profs = profs

    def __str__(self):
        output_string = f'Course Id: {self._classes[1]}\n\n'
        output_string += f'Days: {self._classes[2]}\n'
        output_string += f'Start time: {self._classes[3]}\n'
        output_string += f'End time: {self._classes[4]}\n'
        output_string += f'Building: {self._classes[5]}\n'
        output_string += f'Room: {self._classes[6]}\n\n'
        for _, value in enumerate(self._depts):
            output_string += f'Dept and Number: {value[1]} {value[2]}\n'
        output_string += '\n'
        output_string += f'Area: {self._courses[1]}\n\n'
        output_string += f'Title: {self._courses[2]}\n\n'

        output_string += f'Description: {self._courses[3]}\n\n'
        output_string += f'Prerequisites: {self._courses[4]}\n\n'
        for _, value in enumerate(self._profs):
            output_string += f'Professor: {value}\n'
        return output_string

    def set_classes(self, classes):
        self._classes = classes

    def get_classes(self):
        return self._classes

    def set_depts(self, depts):
        self._depts = depts

    def get_depts(self):
        return self._depts

    def set_courses(self, courses):
        self._courses = courses

    def get_courses(self):
        return self._courses

    def set_profs(self, profs):
        self._profs = profs

    def get_profs(self):
        return self._profs
