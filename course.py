class Course:

    def __init__(self, args):
        self._idnum = args[0]
        self._dept = args[1]
        self._num = args[2]
        self._area = args[3]
        self._title = args[4]

    def __str__(self):
        # return "{:<7}{:<5}{:<7}{:<5}{:<5}".format(self._idnum,
        #                                           self._dept,
        #                                           self._num,
        #                                           self._area,
        #                                           self._title)
        output = f"<tr><td>{self._idnum}</td>"
        output += f"<td>{self._dept}</td>"
        output += f"<td>{self._num}</td>"
        output += f"<td>{self._area}</td>"
        output += f"<td>{self._title}</td></tr>"
        return output

    def set_id(self, id_num):
        self._idnum = id_num

    def get_id(self):
        return self._idnum

    def set_dept(self, dept):
        self._dept = dept

    def get_dept(self):
        return self._dept

    def set_num(self, num):
        self._num = num

    def get_num(self):
        return self._num

    def set_area(self, area):
        self._area = area

    def get_area(self):
        return self._area

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title
